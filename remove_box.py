import os

def strip_boxed(s):
    result = []
    i = 0
    while i < len(s):
        if s.startswith(r'\boxed{', i):
            i += len(r'\boxed{')
            depth = 1
            start = i
            while i < len(s) and depth > 0:
                if s[i] == '{':
                    depth += 1
                elif s[i] == '}':
                    depth -= 1
                i += 1
            # append inner content (without outer braces)
            result.append(s[start:i-1])
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            new_content = strip_boxed(content)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
