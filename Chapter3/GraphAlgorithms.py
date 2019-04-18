from ListNode import ListNode
''' This is the depth first search implementation ''' 
#TODO turn all 'visited' checks from arrays into hash tables (to reduce running time)

#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = []
#         self.pre = 0
#         self.post = 0 

def explore(node, num = 0, visited=None):
    if(visited is None):
        visited = []
    if(node.val in visited):
        return num, visited
    visited.append(node.val)
    num += 1
    node.pre = num
    for n in node.next:
            num, visited = explore(n, num, visited)
    num += 1
    node.post = num
    return num, visited

def create_copy_of_graph(node):
    ''' Helper function to not mutate graphs ''' 
    newNode = ListNode(node.val)
    for n in node.next:
        newNode.next.append(create_copy_of_graph(n))
    return newNode

def depth_first_search(nodes):
    ''' Pass in array of nodes to run DFS on ''' 
    visited = []
    n = 0
    g = []
    for node in nodes:
        if (node.val not in visited):
            node_copy = create_copy_of_graph(node)
            n, v = explore(node_copy, n, visited)
            g.append(node_copy)
            visited = [*visited, *v]

    return g

