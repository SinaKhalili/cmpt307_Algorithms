from ListNode import ListNode

listnode_array, edges = [a,b,c,d,e]
nodeset_ht = {}
for node in listnode_array:
    nodeset_ht[node.val] = set()
    nodeset_ht[node.val].add(node.val)

x = []

edges.sort()

for e in edges:
    if nodeset_ht[
