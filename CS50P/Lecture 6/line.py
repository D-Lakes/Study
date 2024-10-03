import sys

count = 0

if len(sys.argv) != 2:
    sys.exit('Please enter a single file name or path')

if not sys.argv[1].endswith('.py'):
    sys.exit('I only read Python files')

try:
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            else:
                count += 1
except FileNotFoundError:
    sys.exit(f'File does not exist {sys.argv[1]}')

print(count)



