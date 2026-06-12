#!/usr/bin/env bash
# Interactive srun session launcher for NCHC HPC.
# Verified accounts/partitions on cluster 'hpc' 2026-06-12.

echo "=========================================================="
echo "          NCHC HPC Interactive Session Launcher           "
echo "=========================================================="
echo "Select session type:"
echo "  1) CPU  — dev partition, account mst109178 (4 cores, 32 GB)"
echo "  2) GPU  — dev partition, account mst113173 (1× H200, 12 cores, 200 GB)"
echo "  3) MEM  — ngs1500g partition, account mst109178 (32 cores, 1.5 TB)"
read -r -p "Choice [1/2/3, default 1]: " choice

case "$choice" in
  2)
    echo "[INFO] Launching GPU session (dev, mst113173, 1× H200)..."
    srun -p dev --account=mst113173 --gres=gpu:H200:1 --cpus-per-task=12 --mem=200G --pty bash
    ;;
  3)
    echo "[INFO] Launching high-memory session (ngs1500g, mst109178, 32 cores, 1.5 TB)..."
    srun -p ngs1500g --account=mst109178 --cpus-per-task=32 --mem=1500G --pty bash
    ;;
  *)
    echo "[INFO] Launching CPU session (dev, mst109178, 4 cores, 32 GB)..."
    srun -p dev --account=mst109178 --cpus-per-task=4 --mem=32G --pty bash
    ;;
esac
