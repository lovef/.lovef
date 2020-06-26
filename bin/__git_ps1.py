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
added = 0
unstaged = 0
staged = 0
deleted = 0
deletedStaged = 0
renamed = 0
for r in status:
    if r.startswith('?'):
        new += 1
        continue
    if r.startswith('M'):
        staged += 1
    if r.startswith('A'):
        added += 1
    if r.startswith("R"):
        renamed += 1
    if r.startswith('D'):
        deletedStaged += 1
    if r.startswith('M', 1):
        unstaged += 1
    if r.startswith('D', 1):
        deleted += 1

print(f" {refName} " +
    '+' * min(staged + added, 3) +
    '~' * min(renamed, 3) +
    '-' * min(deletedStaged, 3) +
    '*' * min(unstaged + deleted, 3) +
    '?' * min(new, 3),
     end='')
