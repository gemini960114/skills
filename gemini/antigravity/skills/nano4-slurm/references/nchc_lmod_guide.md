# NCHC HPC Lmod Module Guide

This reference documents the environment modules available on the NCHC HPC system, which uses Lmod for environment management.

## 1. What is Lmod?
`Lmod` is a Lua-based environment module system that allows users to dynamically load, unload, and switch software compilations, compilers, and library paths (such as CUDA and MPI).

Instead of modifying your `~/.bashrc` manually, you should use `ml` or `module` commands in your Slurm scripts or shell.

---

## 2. Essential Commands

| Action | Command | Description |
| :--- | :--- | :--- |
| **List Available Modules** | `ml avail` or `module avail` | Lists all software libraries compiled on the cluster. |
| **Search Module** | `module spider <name>` | Searches for specific software names (case-insensitive). |
| **Load Module** | `ml <name>` or `module load <name>` | Loads the library into your current environment. |
| **Unload Module** | `ml -<name>` or `module unload <name>` | Unloads a module and reverts environment paths. |
| **Check Loaded Modules**| `ml` or `module list` | Shows currently loaded modules in this session. |
| **Clear Environment** | `module purge` | Unloads all currently active modules. |

---

## 3. Selecting CUDA Versions (Recommendation)

### A. CUDA 12.6
* **Why**: Highly recommended for Python framework users (PyTorch 2.x, TensorFlow 2.x, JAX). CUDA 12.x matches current pre-compiled wheels in pip/conda.
* **Loading command**:
  ```bash
  ml cuda/12.6
  ```

### B. CUDA 13.0
* **Why**: Pre-installed default version on the cluster. Good for pure CUDA C++ compilation or cutting-edge projects.
* **Loading command**:
  ```bash
  ml cuda/13.0
  ```

---

## 4. Troubleshooting Module Conflicts

If you load multiple conflicting compilers (e.g. GCC and Intel compiler at the same time), Lmod will auto-unload conflicts. To guarantee a clean state in your Slurm batch script, it is good practice to run `module purge` first:

```bash
# Clean active modules and load specific target stack
module purge
ml gcc/13.2
ml cuda/12.6
```
