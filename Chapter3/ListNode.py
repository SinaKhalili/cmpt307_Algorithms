from graphviz import Digraph

class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = []
         self.pre = 0
         self.post = 0

    def to_json(self):
        return { 
                "val":self.val,
                "next":list(map(lambda x: x.val, self.next)),
                "pre":self.pre,
                "post":self.post
                }

    @classmethod
    def create_many(cls, init_value_array):
        return list(map(lambda x: cls(x), init_value_array))

    def test_func(self):
        print('hi')

    def append(self, node_array):
        try: 

            for a in node_array:
                self.next.append(a)
        except:
            self.next.append(node_array)

   #  def create_random_graph:
        # Create a random graph

    def show(self, g=None, ordering=False):
        if(not ordering):
            if(g is None):
                g = Digraph()
            if(self.next == []):
                print("Leaf node")
                #g.edge(str(self.val), str(self.val))
            for node in self.next:
                g.edge(str(self.val), str(node.val))
            return g


#d.edge('1','2')
#d.edge('1','3')

