class Node:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

    def getName(self):
        return self.name


class Edge:
    """Assumes src & dest are nodes"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src
    def get_destination(self):
        return self.dest
    def __str__(self):
        return f"{self.src.getName()} -> {self.dest.getName()}"


class Digraph:
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node] = []
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not src in self.edeges and dest in self.edges:
            raise ValueError ("Node not in graph")
        self.edges[src].append(dest)
    
    def childOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self,name):
        for n in self.edges.keys():
            if n.getName() == name:
                return n
            raise ValueError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += f"{src.getName()} -> {dest.getName()}\n"
        return result


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self,rev)


nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

g.addEdge(Edge(g.getNode("ABC"), g.getNode("BAC")))
g.addEdge(Edge(g.getNode("ABC"), g.getNode("ACB")))
g.addEdge(Edge(g.getNode("BAC"), g.getNode("BCA")))
g.addEdge(Edge(g.getNode("ACB"), g.getNode("CAB")))
g.addEdge(Edge(g.getNode("CAB"), g.getNode("CBA")))
g.addEdge(Edge(g.getNode("BCA"), g.getNode("CBA")))

print(g.__str__())