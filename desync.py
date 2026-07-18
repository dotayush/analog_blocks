#!/usr/bin/env python3
import sys, re

log = open(sys.argv[1], encoding='utf-8', errors='replace').read()

stack = []  # entries: ('file', name) or ('ord',)
i = 0
n = len(log)
warning_re = re.compile(r'(Under|Over)full \\[hv]box')
fname_re = re.compile(r'^[./\w-]+\.(tex|sty|cls|def|cfg|clo)\b')

def current_file():
    for kind, *rest in reversed(stack):
        if kind == 'file':
            return rest[0]
    return "???"

while i < n:
    c = log[i]
    if c == '(':
        chunk = log[i+1:i+300]
        m = fname_re.match(chunk.lstrip())
        if m:
            stack.append(('file', m.group(0)))
        else:
            stack.append(('ord',))
    elif c == ')':
        if stack:
            stack.pop()
    elif warning_re.match(log[i:i+20]):
        line_no = log[:i].count('\n') + 1
        print(f"log line {line_no}: current open file = {current_file()}")
    i += 1
