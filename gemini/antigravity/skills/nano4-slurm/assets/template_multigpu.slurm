#!/bin/bash
# =============================================================================
# template_multigpu.slurm  —  Multi-node DDP (16gpus: 2 nodes, 16× H200)
# Account: <YOUR_GPU_ACCOUNT>  (verify: scontrol show partition 16gpus | grep AllowAccounts)
# QoS p_16gpus: max 6 concurrent jobs per user
# =============================================================================
#SBATCH --account=<YOUR_GPU_ACCOUNT>
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

set -euo pipefail

if [ ! -d "logs" ]; then
    echo "[ERROR] 'logs/' directory missing. Run: mkdir -p logs" >&2
    exit 1
fi

cd "$SLURM_SUBMIT_DIR"

# Resolve distributed training variables
export MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
export MASTER_PORT=29500
export WORLD_SIZE=$((SLURM_NNODES * SLURM_NTASKS_PER_NODE))

echo "Job $SLURM_JOB_ID started on $(date)"
echo "Master: $MASTER_ADDR  World size: $WORLD_SIZE"

ml cuda/12.6

# -------- YOUR TASK BELOW --------
# srun python distributed_train.py \
#     --init_method tcp://$MASTER_ADDR:$MASTER_PORT \
#     --world_size $WORLD_SIZE
# ---------------------------------

echo "Job finished on $(date)"
