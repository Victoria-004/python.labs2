def find_connected_components(n, edges):
    graph = {}
    all_people = set()
    for p1_str, p2_str in edges:
        p1 = int(p1_str)
        p2 = int(p2_str)
        all_people.add(p1)
        all_people.add(p2)
        if p1 not in graph:
            graph[p1] = []
        if p2 not in graph:
            graph[p2] = []
        graph[p1].append(p2)
        graph[p2].append(p1)

    visited = set()
    components = []

    def dfs(node, current_component):
        visited.add(node)
        current_component.add(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, current_component)

    for person in all_people:
        if person not in visited:
            component = set()
            dfs(person, component)
            components.append(component)

    return components

def calc_tribe_pairs(n, tribe_pairs):
    components = find_connected_components(n, tribe_pairs)
    inter_tribe_pairs = []

    tribe_info = []
    for i, component in enumerate(components):
        males = [person for person in component if person % 2 != 0]
        females = [person for person in component if person % 2 == 0]
        tribe_info.append({'males': males, 'females': females, 'id': i})

    num_tribes = len(tribe_info)
    for i in range(num_tribes):
        for male in tribe_info[i]['males']:
            for j in range(num_tribes):
                if i != j:
                    for female in tribe_info[j]['females']:
                        pair = tuple(sorted((male, female)))
                        inter_tribe_pairs.append(pair)

    unique_pairs = sorted(list(set(inter_tribe_pairs)))
    return len(unique_pairs), unique_pairs

n = 4
tribe_pairs = [
    ("1", "2"),
    ("2", "3"),
    ("4", "5"),
    ("5", "6")
]

count, pairs = calc_tribe_pairs(n, tribe_pairs)
print(count)

n = 3
tribe_pairs = [
    ("1", "2"),
    ("2", "4"),
    ("3", "5")
]
count, pairs = calc_tribe_pairs(n, tribe_pairs)
print(count)

n = 5
tribe_pairs = [
    ("1", "2"),
    ("2", "4"),
    ("1", "3"),
    ("3", "5"),
    ("8", "10")
]
count, pairs = calc_tribe_pairs(n, tribe_pairs)
print(count)

