def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    root = int(lines[0])
    tree = {}

    for line in lines[1:]:
        parts = line.split(',')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            parent = int(parts[0])
            child = int(parts[1])
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(child)

    return root, tree

def min_depth(root, tree):
    if root is None:
        return 0

    queue = [(root, 1)]

    while queue:
        node, depth = queue.pop(0)
        children = tree.get(node, [])

        if not children:
            return depth

        for child in children:
            queue.append((child, depth + 1))

    return 0

root, tree = read_file('input.txt')

result = min_depth(root, tree)

with open('output.txt', 'w') as f:
    f.write(str(result))

print('Minimal depth:', result)