#!/usr/bin/env python3
import os
import sys
import subprocess
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_fuzzer.py <executable> [args...] <folder> [file_id]")
        print("  executable: path to the program to run")
        print("  args: optional arguments for the executable")
        print("  folder: directory containing input files")
        print("  file_id: optional - specific file ID to run (e.g., 1 for id:000001)")
        sys.exit(1)

    args = sys.argv[1:]

    # Find the folder (last argument that is a directory, or second-to-last if last is a number)
    folder = None
    target_id = None
    cmd_args = []

    # Check if last argument is a number (file_id)
    try:
        target_id = int(args[-1])
        # If it's a number, the folder should be second-to-last
        if len(args) < 2:
            print("Error: Need at least executable and folder arguments")
            sys.exit(1)
        folder = args[-2]
        cmd_args = args[:-2]
    except (ValueError, IndexError):
        # Last argument is not a number, so it should be the folder
        folder = args[-1]
        cmd_args = args[:-1]

    executable = cmd_args[0] if cmd_args else None
    exe_args = cmd_args[1:] if len(cmd_args) > 1 else []

    if not executable:
        print("Error: No executable specified")
        sys.exit(1)

    if not os.path.isfile(executable):
        print(f"Error: Executable '{executable}' not found")
        sys.exit(1)

    if not os.path.isdir(folder):
        print(f"Error: Folder '{folder}' not found")
        sys.exit(1)

    # Pattern to match files starting with id:0000XX
    pattern = re.compile(r'^id:(\d{6})')

    files_to_process = []
    for filename in os.listdir(folder):
        match = pattern.match(filename)
        if match:
            file_id = int(match.group(1))
            if target_id is None or file_id == target_id:
                files_to_process.append((filename, file_id))

    if not files_to_process:
        if target_id is not None:
            print(f"No file found with ID {target_id:06d}")
        else:
            print("No files found matching pattern id:0000XX")
        sys.exit(1)

    # Sort by file ID
    files_to_process.sort(key=lambda x: x[1])

    for filename, file_id in files_to_process:
        filepath = os.path.join(folder, filename)
        print(f"Running {executable} with {filename} (ID: {file_id:06d})")

        try:
            with open(filepath, 'rb') as input_file:
                cmd = [executable] + exe_args
                result = subprocess.run(
                    cmd,
                    stdin=input_file,
                    capture_output=True,
                    timeout=3
                )

                print(f"  Exit code: {result.returncode}")
                if result.stdout:
                    print(f"  Stdout: {result.stdout.decode('utf-8', errors='ignore').strip()}")
                if result.stderr:
                    print(f"  Stderr: {result.stderr.decode('utf-8', errors='ignore').strip()}")

        except subprocess.TimeoutExpired:
            print(f"  Timeout after 3 seconds - killed and continuing")
        except Exception as e:
            print(f"  Error: {e}")

        print("-" * 50)

if __name__ == "__main__":
    main()