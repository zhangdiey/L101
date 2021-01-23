import sys

path_to_file = sys.argv[1]
keyword = sys.argv[2]

with open(path_to_file, 'r') as f:
    tokens = []
    for line in f.readlines():
        tokens += line.split()
    print(tokens.count(keyword))