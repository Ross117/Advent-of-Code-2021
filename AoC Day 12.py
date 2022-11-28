# import sys

# sys.setrecursionlimit(20)

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

# start setup

all_paths = [i.split('-') for i in input]
    
caves = set()

cavemap = {}

# can do a set comprehension?
for path in all_paths:
    for cave in path:
        caves.add(cave)

for cave in caves:
    paths = []

    for path in all_paths:

        if path[0] == cave:
            paths.append(path[1])
        elif path[1] == cave:
            paths.append(path[0])
    
    cavemap[cave] = paths

# end setup

count_of_paths = 0

def lower_check(path):

    lower_caves = list(filter(lambda x: x.islower(), path))

    check = True

    for cave in lower_caves:
        if lower_caves.count(cave) > 1:
            check = False
            break

    return check

def find_all_paths(graph, start, end, path=[]):
    
    path = path + [start]

    if start == end:
        global count_of_paths
        count_of_paths += 1
        return [path]
        
    if not start in graph:
        return []

    paths = []
    
    for node in graph[start]:
        if node not in path or node.isupper() or (node != 'start' and node != 'end' and node.islower() and lower_check(path)):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    
    return paths

find_all_paths(cavemap, 'start', 'end')

print(count_of_paths)
