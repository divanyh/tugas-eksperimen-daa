from Data.generate_data import TreeNode

tree = {}

with open('vertex_20.txt', 'r') as file:
    for line in file:
        line_new = line.split(': ')
        child = list(map(int, line_new[1].split()))
        tree[int(line_new[0])] = child

vc = [[-1]*2 for i in range(20)]

def sum_vertex(root):
    global tree

    return_set = set()
    if tree[root] == []:
        vc[root][0] = 0
        vc[root][1] = 1
        return return_set
    
    total_cost = 0
    for vertex in root.child:
        return_set = return_set.union(sum_vertex(vertex))
        total_cost += min(vc[vertex.value][0], vc[vertex.value][1])
        if vc[vertex.value][0] > vc[vertex.value][1]:
            return_set = return_set.union(vertex.value)
    
    vc[root.value][0] = sum_no(root)
    vc[root.value][1] = 1 + total_cost

    if vc[root.value][1] < vc[root.value][0]:
        return_set = return_set.union(root.value)
    return return_set

def sum_no(root):
    total = 0
    for vertex in root.childValue:
        total += vc[vertex][1]

print(tree)