tree = {}
vc = [[set()]*3 for i in range(1005000)]

with open('vertex_1m.txt', 'r') as file:
    for line in file:
        line_new = line.split(': ')
        child = list(map(int, line_new[1].split()))
        tree[int(line_new[0])] = child

YES = 1
NO = 0
MAYBE = 2

def sum_child(children, status):
    return_set = set()
    for child in children:
        var = vertex_cover(child)
        return_set = return_set.union(vc[child][status])
    return return_set

def vertex_cover(node):
    global tree, vc

    if len(vc[node][MAYBE]) != 0:
        return vc[node][MAYBE]
    
    vc[node][YES] = {node}.union(sum_child(tree[node], MAYBE)) 
    vc[node][NO] = sum_child(tree[node], YES)

    if len(vc[node][YES]) < len(vc[node][NO]):
        vc[node][MAYBE] = vc[node][YES]
    else:
        vc[node][MAYBE] = vc[node][NO]

    return vc[node][MAYBE]

minimum = vertex_cover(0)
print('panjang nya', len(minimum))
print(minimum)
