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

## 1. Hardware Summary

| Node Class | Hostnames | Count | CPU Cores | Memory | GPU |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CPU (CPN)** | `25a-cpn[01-10,16-18]` | 13 | 124 | ~1 TB (1,031 GB) | — |
| **Memory (MPN)** | `25a-mpn[01-02]` | 2 | 124 | ~6.1 TB (6,224 GB) | — |
| **GPU (HGPN)** | `25a-hgpn[001-220]` | 220 | 112 | ~1.9 TB (1,900 GB) | 8× NVIDIA H200 |

> [!NOTE]
> `25a-cpn[01-02]` and `25a-mpn01` are currently `drain` — do not target them explicitly. Slurm will skip drained nodes automatically.

---

## 2. CPU & Memory Partitions (Account: `mst109178`)

All partitions below target CPN or MPN nodes and require `--account=mst109178`.

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

---

## 3. GPU Partitions (Account: `mst113173`)

All GPU partitions target `25a-hgpn[001-196]` (H200 × 8 per node) unless noted.  
**Account**: `mst113173` (verified: `mst109178` is **denied** from GPU partitions).

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

### A. CPU Job (ngs32g, 4 cores, 32 GB)

```bash
#!/bin/bash
#SBATCH --account=mst109178
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

### B. Single-Node GPU Job (8gpus, 4× H200)

```bash
#!/bin/bash
#SBATCH --account=mst113173
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

### C. Multi-Node GPU Job (16gpus, 2 nodes, 16× H200)

```bash
#!/bin/bash
#SBATCH --account=mst113173
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

### D. Multi-CPU Job (ngs248c, 248 cores, no memory cap)

```bash
#!/bin/bash
#SBATCH --account=mst109178
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

# Launch interactive CPU session
srun -p dev --account=mst109178 --cpus-per-task=4 --mem=32G --pty bash

# Launch interactive GPU session (1× H200)
srun -p dev --account=mst113173 --gres=gpu:H200:1 --cpus-per-task=12 --mem=200G --pty bash
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

### C. GPU account: `mst109178` is **denied** on all GPU partitions
`32gpus` and `64gpus` explicitly deny `mst109178`. Use `mst113173` for all GPU work.

### D. `taide` / `slinky` require special accounts
`taide` allows only `gov113008`, `gov115010`. `slinky` allows only `gov115010`, `gov113097`. Submitting with `mst113173` to these partitions will be rejected immediately.

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
