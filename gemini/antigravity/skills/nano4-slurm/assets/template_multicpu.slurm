#!/bin/bash
# =============================================================================
# template_multicpu.slurm  —  Multi-CPU parallel (ngs248c, 2 nodes, no mem cap)
# Account: <YOUR_CPU_ACCOUNT>  (run: sacctmgr show user $USER withassoc format=Account -n)
# Nodes: 25a-cpn* (2 nodes, no memory QoS cap)
# =============================================================================
#SBATCH --account=<YOUR_CPU_ACCOUNT>
#SBATCH --partition=ngs248c
#SBATCH --job-name=multicpu_job
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=124
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

set -euo pipefail

if [ ! -d "logs" ]; then
    echo "[ERROR] 'logs/' directory missing. Run: mkdir -p logs" >&2
    exit 1
fi

cd "$SLURM_SUBMIT_DIR"

# Redirect /tmp to /work — each CPN node has limited local disk
mkdir -p /work/$(whoami)/tmp
export TMPDIR="/work/$(whoami)/tmp"

echo "Job $SLURM_JOB_ID started on $(date)"
echo "Nodes: $SLURM_NODELIST  Total tasks: $SLURM_NTASKS"

# -------- YOUR TASK BELOW --------
# MPI example:
#   srun --mpi=pmix python mpi_script.py
#
# NOTE: ngs248c has no memory cap per QoS, but each CPN node caps at ~1 TB.
#       Do not rely on >1 TB per node — use ngs1000g or MPN partitions instead.
# ---------------------------------

echo "Job finished on $(date)"
