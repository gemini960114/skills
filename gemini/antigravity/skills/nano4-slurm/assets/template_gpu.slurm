#!/bin/bash
# =============================================================================
# template_gpu.slurm  —  Single-node GPU job (8gpus: 1 node, up to 8× H200)
# Account: <YOUR_GPU_ACCOUNT>  (verify: scontrol show partition 8gpus | grep AllowAccounts)
# QoS p_8gpus: max 8 concurrent jobs per user, no TRES cap
# =============================================================================
#SBATCH --account=<YOUR_GPU_ACCOUNT>
#SBATCH --partition=8gpus
#SBATCH --job-name=gpu_job
#SBATCH --nodes=1
#SBATCH --gres=gpu:H200:4
#SBATCH --cpus-per-task=48
#SBATCH --mem=800G
#SBATCH --time=1-00:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

set -euo pipefail

if [ ! -d "logs" ]; then
    echo "[ERROR] 'logs/' directory missing. Run: mkdir -p logs" >&2
    exit 1
fi

cd "$SLURM_SUBMIT_DIR"

echo "Job $SLURM_JOB_ID started on $(date)"
echo "Node: $SLURM_NODELIST"
nvidia-smi --query-gpu=index,name,memory.total --format=csv,noheader

# Load CUDA 12.6 (recommended for PyTorch 2.x / TF 2.x)
ml cuda/12.6

# -------- YOUR TASK BELOW --------
# Direct Python:
#   python train.py
#
# Via Singularity (MUST include --nv to bind host GPU drivers):
#   singularity exec --nv -B /work /work/$(whoami)/docker/image.sif python train.py
# ---------------------------------

echo "Job finished on $(date)"
