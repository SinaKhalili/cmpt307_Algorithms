from ListNode import ListNode
''' This is the depth first search implementation ''' 
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = []
#         self.pre = 0
#         self.post = 0 

def explore(node, num = 0):
    num += 1
    node.pre = num
    for n in node.next:
        num = explore(n, num)
    node.post = num
    return num

def create_copy_of_graph(node):
    ''' Helper function to not mutate graphs ''' 
    newNode = ListNode(node.val)
    for n in node.next:
        newNode.next.append(create_copy_of_graph(n))
    return newNode

def depth_first_search(node):
    g = create_copy_of_graph(node)
    # TODO: actually run explore on all nodes instead of just one
    explore(g)
    return g

