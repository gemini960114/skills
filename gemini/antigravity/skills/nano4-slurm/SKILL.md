---
name: nano4-slurm
description: Complete guide for Slurm job dispatch on the NCHC HPC (hpc cluster, 25a-* nodes) — CPU/MPN/GPU partitions, QoS limits, templates, and troubleshooting. Extends nchc-slurm-helper with verified GPU QoS, multi-CPU partitions (ngs248c/ngs496c), and account/partition access rules confirmed on 2026-06-12.
tool_type: cli
primary_tool: slurm
measurable_outcome: Dispatch, monitor, and troubleshoot CPU/GPU Slurm jobs on NCHC HPC without QoS, account, or log-directory failures.
allowed-tools:
  - Bash
---

# nano4-slurm — NCHC HPC Slurm Complete Reference

**Cluster**: `hpc` (login node `25a-lgn02`, RHEL 9.6)  
**Verified**: 2026-06-12 against live `sinfo`, `sacctmgr`, `scontrol`.  
**Companion skill**: `nchc-slurm-helper` (same environment; this skill adds GPU QoS detail, multi-CPU partitions, and account access rules that were missing).

---

## 0. Interactive Job Submission Workflow (FOLLOW THIS ORDER)

> [!IMPORTANT]
> When a user asks to submit a Slurm job **without fully specifying account, partition, and resources**, always follow this workflow. Do NOT silently pick defaults.

### Step 1 — Discover and display available accounts

Run this and present results to the user:

```bash
# List all accounts available to the current user
sacctmgr show user $USER withassoc format=User,Account -n | awk '{print $2}' | sort -u
```

**Present as a numbered list.** Example output to show the user:
```
您的可用計畫帳號 (Accounts)：
 1. acd109001     ← 學術研究計畫 (acd)
 2. gov109028     ← 政府計畫 (gov)
 3. mst109178     ← 一般計畫 (mst)
 4. mst113173     ← GPU 計畫 (mst，需確認是否有 GPU partition 權限)
 ... (依實際輸出列出，帳號前綴說明類別)
```

**Account type naming convention on this cluster:**
- `mst*` — 一般科技部/國科會計畫
- `gov*` — 政府機關計畫
- `acd*` — 學術研究計畫
- `ent*` — 企業計畫
- `edu*` — 教育計畫

> [!IMPORTANT]
> Each user may have **multiple accounts**. Always ask the user which account to charge, or present the list and let them choose. Never assume an account.

### Step 2 — Discover and display available partitions

```bash
# Show all partitions with status and time limit
sinfo --format="%P %a %l %D %C %G" | column -t
```

Then cross-reference with the partition→account rules in Section 2 & 3:
- **CPU/MPN partitions** (`ngs*`): require an account that has access — verify with `sacctmgr show partition <partition>` or check `AllowAccounts` in `scontrol show partition <partition>`
- **GPU partitions** (`8gpus`, `16gpus`, etc.): require a GPU-enabled account (typically a different account than CPU). Verify by attempting submission or checking `AllowAccounts`.
- **Special partitions** (`taide`, `slinky`): restricted to specific accounts only (see Section 3)

**Present as a filtered table** (skip `inactive` partitions):
```
可用的 Partition 列表：
類型  Partition      時間限制     最大 CPU  最大記憶體
────────────────────────────────────────────────────
CPU   ngs8g          2 天         1         8G
CPU   ngs16g         2 天         2         16G
CPU   ngs32g         4 天         4         32G
CPU   ngs62g         4 天         8         62G
CPU   ngs125g        無限制       16        125G
CPU   ngs250g        無限制       32        250G
CPU   ngs500g        無限制       64        500G
CPU   ngs1000g       無限制       124       1000G
MPN   ngs1500g       無限制       32        1500G
MPN   ngs2t          無限制       42        2000G
MPN   ngs3t          無限制       64        3000G
MPN   ngs6t          無限制       124       6000G
GPU   8gpus          2 天         112       1900G  (需 GPU 帳號，見 Section 3)
GPU   16gpus         2 天         112×2     1900G×2(需 GPU 帳號，見 Section 3)
```

### Step 3 — Accept user's choice and confirm resource spec

After user selects account + partition, **always confirm the resource spec**:

| 用戶說 | Agent 行為 |
| :--- | :--- |
| 「最大規格」/「不要浪費」/「full」 | 填入 Section 2E 的 QoS 天花板 |
| 指定 CPU 數量（如「8 cores」） | 使用用戶指定值，但驗證不超過 QoS 上限 |
| 沒說 CPU，只說 partition | **詢問用戶**：「您需要幾個 CPU？最大可申請 N 個」 |
| 沒說記憶體 | 按比例分配（e.g. 16 CPU on ngs250g → mem=125G）或填天花板 |

> [!WARNING]
> **Never silently default to `--cpus-per-task=1`** on large-memory partitions (`ngs125g` and above). Always ask or fill the ceiling.

### Step 4 — Verify QoS limits before writing the script

```bash
# 驗證指定 partition 的 QoS 限制（將 ngs250g 換成目標 partition）
sacctmgr show qos p_ngs250g format=Name,MaxTRESPerUser -n
# 輸出範例: p_ngs250g  cpu=32,mem=256000M  → cpus-per-task=32, mem=250G
```

### Step 5 — Generate and submit

Generate the script using the correct template from Section 4, fill in all fields, then:
```bash
mkdir -p logs
sbatch <script_name>.slurm
```

Confirm submission by showing the Job ID and running `squeue -j <JOB_ID>`.

---

## 1. Hardware Summary

| Node Class | Hostnames | Count | CPU Cores | Memory | GPU |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CPU (CPN)** | `25a-cpn[01-10,16-18]` | 13 | 124 | ~1 TB (1,031 GB) | — |
| **Memory (MPN)** | `25a-mpn[01-02]` | 2 | 124 | ~6.1 TB (6,224 GB) | — |
| **GPU (HGPN)** | `25a-hgpn[001-220]` | 220 | 112 | ~1.9 TB (1,900 GB) | 8× NVIDIA H200 |

> [!NOTE]
> `25a-cpn[01-02]` and `25a-mpn01` are currently `drain` — do not target them explicitly. Slurm will skip drained nodes automatically.

---

## 2. CPU & Memory Partitions

All partitions below target CPN or MPN nodes. Use `--account=<YOUR_CPU_ACCOUNT>` where `<YOUR_CPU_ACCOUNT>` is obtained from Step 1 of the Interactive Workflow (Section 0).

```bash
# To find which accounts are allowed on a specific partition:
scontrol show partition ngs250g | grep AllowAccounts
```

### 2A. Standard CPU Partitions (CPN, `25a-cpn*`)

| Partition | Time Limit | Max `--cpus-per-task` | Max `--mem` | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `ngstest` | 10 min | 1 | 8 GB | Quick sanity tests only |
| `ngsconsole` | Infinite | 1 | 8 GB | Long-running light tasks |
| `ngs8g` | 2 days | 1 | 8 GB | |
| `ngs16g` | 2 days | 2 | 16 GB | |
| `ngs32g` | 4 days | 4 | 32 GB | Most common for pipelines |
| `ngs62g` | 4 days | 8 | 62 GB | |
| `ngs125g` | Infinite | 16 | 125 GB | |
| `ngs250g` | Infinite | 32 | 250 GB | |
| `ngs500g` | Infinite | 64 | 500 GB | |
| `ngs1000g` | Infinite | 124 | 1000 GB | Full node memory |

### 2B. Multi-CPU Partitions (CPN, `25a-cpn*`) — NOT in original skill

These partitions have **no memory cap** — only CPU cap. Use for CPU-bound parallel workloads that need >124 cores (across multiple nodes).

| Partition | Time Limit | Max `--cpus-per-task` | Max `--mem` | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `ngs248c` | Infinite | **248** | Unlimited | Spans 2 CPN nodes |
| `ngs496c` | Infinite | **496** | Unlimited | Spans 4 CPN nodes |

> [!WARNING]
> `ngs248c` / `ngs496c` have no memory QoS limit but the underlying CPN nodes each cap at ~1 TB. If you need >1 TB per node, use MPN partitions instead.

### 2C. Memory (MPN) Partitions (`25a-mpn[01-02]`)

| Partition | Time Limit | Max `--cpus-per-task` | Max `--mem` |
| :--- | :--- | :--- | :--- |
| `ngs1500g` | Infinite | 32 | 1500 GB |
| `ngs2t` | Infinite | 42 | 2000 GB |
| `ngs3t` | Infinite | 64 | 3000 GB |
| `ngs6t` | Infinite | 124 | 6000 GB |

### 2D. Course Partitions (time-limited, for teaching)

| Partition | Time Limit | Max `--cpus-per-task` | Max `--mem` |
| :--- | :--- | :--- | :--- |
| `ngscourse8g` | 2 hours | 1 | 8 GB |
| `ngscourse32g` | 4 hours | 4 | 32 GB |
| `ngscourse125g` | 1 day | 16 | 125 GB |

### 2E. ⚠️ Maximum-Spec Rule (IMPORTANT for agents)

> [!IMPORTANT]
> **When the user asks for "maximum spec", "full resources", "不要浪費", or "最大規格"**, you MUST fill `--cpus-per-task` and `--mem` to the QoS ceiling for that partition. Do **NOT** default to `--cpus-per-task=1`.

**Quick lookup — always set BOTH fields to the ceiling:**

| Partition | Use `--cpus-per-task=` | Use `--mem=` |
| :--- | :--- | :--- |
| `ngs8g` | 1 | 8G |
| `ngs16g` | 2 | 16G |
| `ngs32g` | 4 | 32G |
| `ngs62g` | 8 | 62G |
| `ngs125g` | 16 | 125G |
| `ngs250g` | **32** | **250G** |
| `ngs500g` | **64** | **500G** |
| `ngs1000g` | **124** | **1000G** |
| `ngs1500g` | **32** | **1500G** |
| `ngs2t` | **42** | **2000G** |
| `ngs3t` | **64** | **3000G** |
| `ngs6t` | **124** | **6000G** |

**To verify live QoS limits before scripting, always run:**
```bash
# Check QoS TRES limits for a partition's QoS
sacctmgr show qos p_<partition_name> format=Name,MaxTRESPerUser -n
# Example:
sacctmgr show qos p_ngs250g format=Name,MaxTRESPerUser -n
# Output: p_ngs250g  cpu=32,mem=256000M  → use --cpus-per-task=32 --mem=250G
```

---

## 3. GPU Partitions

All GPU partitions target `25a-hgpn[001-196]` (H200 × 8 per node) unless noted.  
**Account**: Use a GPU-enabled account (check Section 0 Step 1 to list your accounts, then verify GPU access).

```bash
# Check which accounts you have that can access GPU partitions:
scontrol show partition 8gpus | grep AllowAccounts
# Then verify your accounts against that list:
sacctmgr show user $USER withassoc format=User,Account -n | awk '{print $2}' | sort -u
```

> [!WARNING]
> CPU accounts (e.g., `mst109178`-type) are typically **denied** on GPU partitions. You must use a separate GPU-enabled account. Always verify before submitting.

| Partition | Max Jobs/User | Time Limit | Nodes | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `8gpus` | 8 | 2 days | `hgpn[001-196]` | Standard single-node |
| `16gpus` | 6 | 2 days | `hgpn[001-196]` | 2-node distributed |
| `32gpus` | 4 | 2 days | `hgpn[001-196]` | 4-node DDP |
| `64gpus` | 2 | 2 days | `hgpn[001-196]` | 8-node DDP |
| `256gpus` | 1 | 2 days | `hgpn[001-196]` | Restricted: `mst111479` / `gov115010` only |
| `dev` | — | 4 hours | `hgpn[001-196]` | Interactive/debug sessions |

> [!IMPORTANT]
> GPU QoS (`p_8gpus` through `p_64gpus`) enforces **job count** limits, not TRES limits. There is no per-job GPU cap — you may request all 8 GPUs on a node within your job quota.

### Special GPU Partitions (restricted accounts)

| Partition | Allowed Accounts | Nodes | Purpose |
| :--- | :--- | :--- | :--- |
| `taide` | `gov113008`, `gov115010` | `hgpn[216-220]` | 5 dedicated H200 nodes |
| `slinky` | `gov115010`, `gov113097` | `hgpn[201-215]` | 15 dedicated H200 nodes |

---

## 4. Job Templates

All templates use `logs/` for output. **Always run `mkdir -p logs` before `sbatch`**.

### A. CPU Job — Max Spec (ngs250g, **32 cores, 250 GB**, Infinite time)

> Use this pattern when the user requests "maximum resources" on `ngs250g`.

```bash
#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --partition=ngs250g            # Infinite time limit
#SBATCH --account=<YOUR_CPU_ACCOUNT>   # ← 從 Section 0 Step 1 查詢取得
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32             # QoS ceiling (cpu=32)
#SBATCH --mem=250G                     # QoS ceiling (mem=256000M ≈ 250G)
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<YOUR_EMAIL>       # ← 替換為用戶 email

mkdir -p /work/$(whoami)/tmp && export TMPDIR="/work/$(whoami)/tmp"
cd "$SLURM_SUBMIT_DIR"

echo "Job $SLURM_JOB_ID started on $(date)"
echo "Node: $SLURM_NODELIST  CPUs: $SLURM_CPUS_PER_TASK  Mem: 250G"

# YOUR TASK HERE
sleep infinity

echo "Job finished on $(date)"
```

### B. CPU Job — Conservative (ngs32g, 4 cores, 32 GB)

```bash
#!/bin/bash
#SBATCH --account=<YOUR_CPU_ACCOUNT>   # ← 從 Section 0 Step 1 查詢取得
#SBATCH --partition=ngs32g
#SBATCH --job-name=my_cpu_job
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=08:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

mkdir -p /work/$(whoami)/tmp && export TMPDIR="/work/$(whoami)/tmp"
cd "$SLURM_SUBMIT_DIR"

# YOUR TASK HERE
```

### C. Single-Node GPU Job (8gpus, 4× H200)

```bash
#!/bin/bash
#SBATCH --account=<YOUR_GPU_ACCOUNT>   # ← GPU 帳號，從 Section 0 Step 1 查詢取得
#SBATCH --partition=8gpus
#SBATCH --job-name=my_gpu_job
#SBATCH --nodes=1
#SBATCH --gres=gpu:H200:4
#SBATCH --cpus-per-task=48
#SBATCH --mem=800G
#SBATCH --time=1-00:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

cd "$SLURM_SUBMIT_DIR"
ml cuda/12.6

# YOUR TASK HERE
# singularity exec --nv -B /work /work/$(whoami)/docker/image.sif python train.py
```

### D. Multi-Node GPU Job (16gpus, 2 nodes, 16× H200)

```bash
#!/bin/bash
#SBATCH --account=<YOUR_GPU_ACCOUNT>   # ← GPU 帳號，從 Section 0 Step 1 查詢取得
#SBATCH --partition=16gpus
#SBATCH --job-name=ddp_job
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --gres=gpu:H200:8
#SBATCH --cpus-per-task=12
#SBATCH --mem=1800G
#SBATCH --time=1-00:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

cd "$SLURM_SUBMIT_DIR"
export MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
export MASTER_PORT=29500
export WORLD_SIZE=$((SLURM_NNODES * SLURM_NTASKS_PER_NODE))
ml cuda/12.6

srun python train.py --init_method tcp://$MASTER_ADDR:$MASTER_PORT --world_size $WORLD_SIZE
```

### E. Multi-CPU Job (ngs248c, 248 cores, no memory cap)

```bash
#!/bin/bash
#SBATCH --account=<YOUR_CPU_ACCOUNT>   # ← 從 Section 0 Step 1 查詢取得
#SBATCH --partition=ngs248c
#SBATCH --job-name=parallel_cpu
#SBATCH --nodes=2
#SBATCH --cpus-per-task=124
#SBATCH --time=12:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

cd "$SLURM_SUBMIT_DIR"
# YOUR MPI/OpenMP TASK HERE
```

---

## 5. Operations Quick Reference

```bash
# Check your running/pending jobs
squeue -u $USER

# Kill a job
scancel <JOB_ID>

# Get job details (node, state, resources)
scontrol show job <JOB_ID>

# Estimate when a pending job will start
squeue --start -j <JOB_ID>

# Review completed/failed job resource usage
sacct -j <JOB_ID> --format=JobID,JobName,State,ExitCode,Elapsed,MaxRSS

# Check idle resources across all partitions
bash .claude/skills/nano4-slurm/scripts/check_resources.sh

# ── QoS limit queries (run BEFORE writing a max-spec script) ──
# List all QoS with TRES limits
sacctmgr show qos format=Name,MaxTRESPerUser -n

# Check specific partition QoS (replace partition name)
sacctmgr show qos p_ngs250g format=Name,MaxTRESPerUser -n

# Check partition details (MaxCPUsPerNode, time limit, QoS name)
scontrol show partition ngs250g

# Launch interactive CPU session (replace <YOUR_CPU_ACCOUNT>)
srun -p ngstest --account=<YOUR_CPU_ACCOUNT> --cpus-per-task=4 --mem=32G --pty bash

# Launch interactive GPU session (replace <YOUR_GPU_ACCOUNT>)
srun -p dev --account=<YOUR_GPU_ACCOUNT> --gres=gpu:H200:1 --cpus-per-task=12 --mem=200G --pty bash
```

---

## 6. Key Gotchas

### A. `logs/` directory must exist before `sbatch`
Slurm cannot create the log directory. If it's missing, the job crashes at spawn with no output.
```bash
mkdir -p logs && sbatch my_job.slurm
```

### B. `/tmp` exhaustion (QIIME2, Python, large pipelines)
Node-local `/tmp` is small. Redirect to `/work`:
```bash
mkdir -p /work/$(whoami)/tmp
export TMPDIR="/work/$(whoami)/tmp"
```

### C. CPU account denied on GPU partitions
GPU partitions enforce `AllowAccounts` — CPU-type accounts are typically rejected. Before submitting a GPU job:
```bash
# 1. Check which accounts are allowed:
scontrol show partition 8gpus | grep AllowAccounts
# 2. List your accounts:
sacctmgr show user $USER withassoc format=User,Account -n | awk '{print $2}' | sort -u
# 3. Use the account that appears in both lists
```

### D. `taide` / `slinky` require special restricted accounts
`taide` and `slinky` partition access is restricted to specific project accounts only. Run `scontrol show partition taide | grep AllowAccounts` to see the current allowed list. Submitting with an unauthorized account will be rejected immediately.

### E. Singularity containers need `--nv` for GPU access
```bash
singularity exec --nv -B /work /work/$(whoami)/docker/image.sif python train.py
```

### F. Exit code 137 = OOM kill
Upgrade partition (e.g. `ngs32g` → `ngs62g`). Check actual usage first:
```bash
sacct -j <JOB_ID> --format=MaxRSS,ReqMem
```

### G. `ngs248c` / `ngs496c` span multiple CPN nodes — memory is not pooled
Each CPN node has ~1 TB independently. If your job needs more than 1 TB on a single process, use `ngs1000g` (single node, 1 TB) or MPN partitions.

### H. ❌ Anti-pattern: defaulting to `--cpus-per-task=1`
When generating a script for `ngs250g`, `ngs500g`, or any large-memory partition, **never** silently set `--cpus-per-task=1`. This wastes the allocated node slot. The rule:
- If the user specifies a CPU count → use it.
- If the user says "max", "full", or "最大規格" → fill to QoS ceiling (see Section 2E).
- If the user says nothing about CPU → **ask** or default to the QoS ceiling for infinite-time partitions.

```bash
# WRONG (wastes 31 of 32 available CPUs on ngs250g)
#SBATCH --cpus-per-task=1

# CORRECT for ngs250g max-spec
#SBATCH --cpus-per-task=32
#SBATCH --mem=250G
```

---

## 7. Troubleshooting

| Symptom | Cause | Fix |
| :--- | :--- | :--- |
| Job stuck `QOSMaxTRES` | Requested CPU or mem exceeds QoS limit | Reduce `--cpus-per-task` / `--mem` or switch to a higher partition |
| Job stuck `InvalidAccount` | Wrong account for partition | GPU job → `mst113173`; CPU/MPN → `mst109178` |
| Job fails instantly, no log | `logs/` directory missing | `mkdir -p logs` before `sbatch` |
| Exit code 137 | OOM killed | Use `sacct --format=MaxRSS` to size correctly; upgrade partition |
| `QOSMaxSubmitJobPerUserQOS` | Hit per-user job count limit | Wait for existing jobs to finish; GPU partitions cap at 1–8 concurrent jobs |
| GPU job, `CUDA_VISIBLE_DEVICES` wrong | Slurm assigns devices automatically via `gres` | Do **not** set `CUDA_VISIBLE_DEVICES` manually — let Slurm manage it |
| Container fails to see GPU | Missing `--nv` flag | `singularity exec --nv ...` |

---

## 8. Skill Package Files

```
.claude/skills/nano4-slurm/
  SKILL.md                    — this file
  scripts/
    check_resources.sh        — live partition idle summary
    interactive.sh            — menu-driven interactive srun launcher
  assets/
    template_cpu.slurm        — production CPU template
    template_gpu.slurm        — single-node GPU template
    template_multigpu.slurm   — multi-node DDP template
    template_multicpu.slurm   — ngs248c/ngs496c multi-CPU template
  references/
    nchc_lmod_guide.md        — Lmod module system reference
```
