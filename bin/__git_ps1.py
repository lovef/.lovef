#!/usr/bin/env python3

import subprocess

try:
    subprocess.check_call(['git', 'rev-parse', '--is-inside-work-tree'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
except:
    exit(0)

try:
    refName = subprocess.check_output(['git', 'symbolic-ref', '--quiet', '--short', 'HEAD']) \
        .decode().rstrip()
except:
    try:
        refName = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']) \
            .decode().rstrip()
    except:
        refName = "(unknown ref)"

status = subprocess.check_output(['git', 'status', '--porcelain'])
status = status.decode()
status = status.split('\n')
new = 0
unstaged = 0
staged = 0
for r in status:
    if r.startswith('?'):
        new += 1
        continue
    if r.startswith('M'):
        staged += 1
    if r.startswith('M', 1):
        unstaged += 1

print(f" {refName} {'+' * min(staged, 3)}{'*' * min(unstaged, 3)}{'?' * min(new, 3)}", end='')
