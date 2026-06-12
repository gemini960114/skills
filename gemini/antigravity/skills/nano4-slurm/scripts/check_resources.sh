#!/usr/bin/env bash
# Show idle resources across all NCHC HPC partitions.
# Verified on cluster 'hpc' (25a-lgn02) 2026-06-12.

echo "========================================================================="
echo "              NCHC HPC Partition Resources Idle Summary                  "
echo "========================================================================="
printf "%-22s %-20s %-24s\n" "Partition" "Nodes (A/I/O/T)" "CPUs (A/I/O/T)"
echo "-------------------------------------------------------------------------"

sinfo -o "%22P %20F %24C" | sort -u | grep -E "ngs|gpus|dev|taide|slinky" | while read -r part nodes cpus; do
    printf "%-22s %-20s %-24s\n" "$part" "$nodes" "$cpus"
done

echo "========================================================================="
echo ""
echo "Column legend: A=Allocated  I=Idle  O=Other(drain/down)  T=Total"
