#!/usr/bin/env python3
import subprocess
import os
import sys

os.chdir(r'C:\Users\ASUS\Hongnan')

# First check the remote
print("=== Checking remote ===")
result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True, shell=True)
print(result.stdout)

# Now try push with more debugging
print("\n=== Running git push ===")
env = os.environ.copy()
env['GIT_TRACE'] = '1'
env['GIT_CURL_VERBOSE'] = '1'

result = subprocess.run(
    'git push -u origin main --force',
    capture_output=True,
    text=True,
    shell=True,
    env=env
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("RETURN CODE:", result.returncode)

# Also try with full path to git
print("\n=== Trying with full git path ===")
git_path = r'C:\Program Files\Git\cmd\git.exe'
result = subprocess.run(
    [git_path, 'push', '-u', 'origin', 'main', '--force'],
    capture_output=True,
    text=True,
    shell=True
)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("RETURN CODE:", result.returncode)
