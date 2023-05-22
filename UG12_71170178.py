class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.child = []

class Tree:
    def __init__(self,root):
        self.root = root

    def addChild(self, node_parent,data):
        new_node = Node(data)
        new_node.parent = node_parent
        node_parent.child.append(new_node)
        return new_node

    def sums(self,node):
        if len(node.child) == 0:
            return node.data
        else:
            total = node.data
            for i in range(len(node.child)):
                total += self.sums(node.child[i])
            return total
                
    def sibling(self,node):
        total = 0
        if node.parent is not None:
            for children in (node.parent.child):
                total += children.data
            return total
        else:
            return node.data
    

if __name__ =='__main__':
    val200 = Node(200)
    t = Tree(val200) #Level 0

    val23 = t.addChild(val200, 23) 
    val11 = t.addChild(val200, 11)

    val13 = t.addChild(val23, 13) 
    val57 = t.addChild(val23, 57) 

    val32 = t.addChild(val11, 32) 

    val42 = t.addChild(val13, 42) 
    val51 = t.addChild(val13, 51) 
    val71 = t.addChild(val13, 71) 

    val12 = t.addChild(val57, 12) 
    val15 = t.addChild(val57, 15)

    val33 = t.addChild(val32, 33)
    val8 = t.addChild(val32, 8)

    # test-1
    print(f'Total value of node {val200.data} and all of its decendands = {t.sums(val200)}')
 
    # test-2
    print(f'Total value of all sibling on node {val33.data} = {t.sibling(val33)}')