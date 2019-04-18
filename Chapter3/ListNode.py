from graphviz import Digraph
#TODO turn all 'visited' checks from arrays into hash tables (to reduce running time)
#TODO change name from ListNode to something else (ListNode is too generic, and doesn't convery any info)

class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = []
         self.prev = []
         self.pre = 0
         self.post = 0

    def to_json(self):
        return { 
                "val":self.val,
                "next":list(map(lambda x: x.val, self.next)),
                "prev":list(map(lambda x: x.val, self.prev)),
                "pre":self.pre,
                "post":self.post
                }

    @classmethod
    def create_many(cls, init_value_array):
        return list(map(lambda x: cls(x), init_value_array))

    def append(self, node_array):
        try: 
            for a in node_array:
                if a not in self.next:
                    self.next.append(a)
                    if self not in a.prev:
                        a.prev.append(self)
        except:
            if node_array not in self.next:
                self.next.append(node_array)

    @staticmethod
    def show_graph(g, ordering=False):
        graph = Digraph()
        v = []
        for node in g:
            node.show(ordering, graph, v)
        return graph

    def show(self, ordering=False, g=None, visited=None):
        # Basically does a DFS to create the graphviz graph
        # Only works for one component 
        if visited is None:
            visited = []
        visited.append(self.val)
        if(g is None):
            g = Digraph()
        for node in self.next:
            if(node.val not in visited):
                node.show(ordering, g, visited)

            if(ordering):
                if(node.pre > 0 and node.post > 0):
                    #Taking care of the case of accidental null nodes
                    g.edge( str(self.pre) + ', ' + str(self.post) + ' \n ' + str(self.val),
                            str(node.pre) + ', ' + str(node.post) + ' \n ' + str(node.val))
            else:
                g.edge(str(self.val), str(node.val))

        return g
