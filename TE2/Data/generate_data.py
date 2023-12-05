import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.childValue = []

VERTEX_NUM = 1000000
vertex_list = []
vertex_sisa = VERTEX_NUM
root = TreeNode(0)
vertex_list.append(root.value)
vertex_sisa -= 1
i = 1

def generate_children(root):
    global vertex_sisa
    global i

    if vertex_sisa <= 0:
        return
    
    jumlah_child = random.randint(0, 4000)
    for j in range(jumlah_child):
        vertex_list.append(i)
        root.childValue.append(i)
        new_child = TreeNode(i)
        root.child.append(new_child)
        i = i+1

    vertex_sisa = vertex_sisa - jumlah_child
    for node in root.child:
        generate_children(node)

def print_edge_list(root):
    
    file.write(f"{root.value}: {' '.join(map(str, root.childValue))}\n")

    for node in root.child:
        print_edge_list(node)

generate_children(root)
filename = 'vertex_1m.txt'
with open(filename, 'w') as file:
    print_edge_list(root)
