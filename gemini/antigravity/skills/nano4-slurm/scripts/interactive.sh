#!/usr/bin/env bash
# Interactive srun session launcher for NCHC HPC.
# Generic: dynamically discovers the current user's accounts at runtime.

echo "=========================================================="
echo "          NCHC HPC Interactive Session Launcher           "
echo "=========================================================="

# Discover available accounts for the current user
echo ""
echo "Fetching your available accounts..."
mapfile -t ACCOUNTS < <(sacctmgr show user "$USER" withassoc format=Account -n | awk '{print $1}' | sort -u)

if [ ${#ACCOUNTS[@]} -eq 0 ]; then
    echo "[ERROR] No accounts found for user $USER. Contact your HPC administrator."
    exit 1
fi

echo ""
echo "Your accounts:"
for i in "${!ACCOUNTS[@]}"; do
    printf "  %d) %s\n" $((i+1)) "${ACCOUNTS[$i]}"
done
read -r -p "Select account number [1]: " acc_choice
acc_idx=$(( ${acc_choice:-1} - 1 ))
SELECTED_ACCOUNT="${ACCOUNTS[$acc_idx]:-${ACCOUNTS[0]}}"
echo "Using account: $SELECTED_ACCOUNT"

echo ""
echo "Select session type:"
echo "  1) CPU  — ngstest partition (4 cores, 32 GB)"
echo "  2) GPU  — dev partition (1x H200, 12 cores, 200 GB)"
echo "  3) MEM  — ngs1500g partition (32 cores, 1.5 TB)"
read -r -p "Choice [1/2/3, default 1]: " choice

case "$choice" in
  2)
    echo "[INFO] Launching GPU session (dev, $SELECTED_ACCOUNT, 1x H200)..."
    srun -p dev --account="$SELECTED_ACCOUNT" --gres=gpu:H200:1 --cpus-per-task=12 --mem=200G --pty bash
    ;;
  3)
    echo "[INFO] Launching high-memory session (ngs1500g, $SELECTED_ACCOUNT, 32 cores, 1.5 TB)..."
    srun -p ngs1500g --account="$SELECTED_ACCOUNT" --cpus-per-task=32 --mem=1500G --pty bash
    ;;
  *)
    echo "[INFO] Launching CPU session (ngstest, $SELECTED_ACCOUNT, 4 cores, 32 GB)..."
    srun -p ngstest --account="$SELECTED_ACCOUNT" --cpus-per-task=4 --mem=32G --pty bash
    ;;
esac
