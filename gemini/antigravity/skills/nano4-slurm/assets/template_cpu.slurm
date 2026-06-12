#!/bin/bash
# =============================================================================
# template_cpu.slurm  —  Standard CPU job (ngs32g: 4 cores, 32 GB, 4 days)
# Account: mst109178   Nodes: 25a-cpn*
# =============================================================================
#SBATCH --account=mst109178
#SBATCH --partition=ngs32g
#SBATCH --job-name=cpu_job
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=08:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

set -euo pipefail

if [ ! -d "logs" ]; then
    echo "[ERROR] 'logs/' directory missing. Run: mkdir -p logs" >&2
    exit 1
fi

cd "$SLURM_SUBMIT_DIR"

# Redirect /tmp to /work to avoid node-local disk exhaustion
mkdir -p /work/$(whoami)/tmp
export TMPDIR="/work/$(whoami)/tmp"

echo "Job $SLURM_JOB_ID started on $(date)"
echo "Node: $SLURM_NODELIST  CPUs: $SLURM_CPUS_PER_TASK  Mem: $SLURM_MEM_PER_NODE MB"

# -------- YOUR TASK BELOW --------
# Example: QIIME2 via Singularity
# SINGULARITY_IMG="/work/c00cjz00/docker/qiime2-2026-4.sif"
# singularity exec -B /work "$SINGULARITY_IMG" qiime --help
# ---------------------------------

echo "Job finished on $(date)"
