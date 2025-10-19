#!/usr/bin/env python3
"""
run.py

Purpose:
- Check for required Python dependencies (requests, Crypto (pycryptodome), hashlib)
- Install missing packages using pip (using the same interpreter)
- Launch a separate target script (default: `main.py`)

Usage examples:
- python run.py                # check/install then run main.py
- python run.py --target app.py
- python run.py --no-install   # do not install packages, only check and run
- python run.py --background   # run the target in background (child process)

Notes:
- `hashlib` is part of the Python standard library (no pip required).
- The package that provides `Crypto` is usually `pycryptodome` on pip.
"""

import sys
import subprocess
import importlib
import importlib.util
import argparse
import os
from typing import Optional

REQUIREMENTS = [
    # (module_import_name, pip_package_name, human_readable_name)
    ("requests", "requests", "requests"),
    ("Crypto", "pycryptodome", "pycryptodome (provides Crypto)"),
    ("hashlib", None, "hashlib (stdlib)"),
]


def is_module_available(module_name: str) -> bool:
    """Check whether a module can be imported without executing its code.
    Uses importlib.util.find_spec for a safer check.
    """
    try:
        return importlib.util.find_spec(module_name) is not None
    except Exception:
        return False


def pip_install(pkg_name: str) -> bool:
    """Try to install a package via pip using the same Python interpreter (sys.executable).
    Returns True if installation succeeded.
    """
    print(f"Installing package: {pkg_name} ...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {pkg_name} (pip return code: {e.returncode})")
        return False
    except Exception as e:
        print(f"Error installing {pkg_name}: {e}")
        return False


def ensure_requirements(no_install: bool = False) -> dict:
    """Check all requirements. If a module is missing and no_install==False, attempt installation.
    Returns a dict with status entries: {module_name: {"available":bool, "attempted":bool, "installed":bool}}
    """
    status = {}
    for mod, pipname, human in REQUIREMENTS:
        available = is_module_available(mod)
        attempted = False
        installed = False
        if not available and pipname and not no_install:
            attempted = True
            installed = pip_install(pipname)
            # re-check availability after attempted install
            available = is_module_available(mod)
        status[mod] = {"available": available, "attempted": attempted, "installed": installed}
    return status


def launch_target(target_file: str, background: bool = False) -> int:
    """Run the target script using the same interpreter.
    If background=True, start it as a child process (Popen) and return immediately.
    Returns an exit code (foreground) or PID (background) or negative error codes.
    """
    if not os.path.exists(target_file):
        print(f"Target file not found: {target_file}")
        return -1

    cmd = [sys.executable, target_file]
    print(f"Launching: {cmd} (background={background})")
    try:
        if background:
            p = subprocess.Popen(cmd)
            print(f"Target is running in background (PID={p.pid})")
            return p.pid
        else:
            completed = subprocess.run(cmd)
            return completed.returncode
    except Exception as e:
        print(f"Failed to launch target: {e}")
        return -2


def parse_args():
    p = argparse.ArgumentParser(description="run.py — check/install requirements then run a target script")
    p.add_argument("--target", "-t", default="main.py", help="Target script to run (default: main.py)")
    p.add_argument("--no-install", action="store_true", help="Do not attempt to install missing packages (only check)")
    p.add_argument("--background", "-b", action="store_true", help="Run the target in background")
    return p.parse_args()


def main():
    args = parse_args()

    print("=== run.py: dependency check & auto-run ===")
    status = ensure_requirements(no_install=args.no_install)

    print("
Summary:")
    for mod, info in status.items():
        print(f" - {mod}: available={info['available']} attempted_install={info['attempted']} installed_success={info['installed']}")

    missing = [m for m, i in status.items() if not i["available"]]
    if missing:
        print("
Warning: some modules are still missing:", ", ".join(missing))
        print("If you want automatic installation, run without --no-install and ensure internet access.")

    print("
Launching target...
")
    result = launch_target(args.target, background=args.background)

    if args.background:
        print(f"Done — target running in background (returned: {result})")
        sys.exit(0)

    # foreground
    if isinstance(result, int):
        if result == 0:
            print("Target finished successfully (exit code 0)")
        elif result > 0:
            print(f"Target finished with exit code {result}")
        else:
            print(f"Target failed or not found (return {result})")
        sys.exit(result if result >= 0 else 1)


if __name__ == "__main__":
    main()
