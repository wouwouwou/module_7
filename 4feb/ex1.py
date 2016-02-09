from basicgraphs import *

g = graph(4)
print(g)
print(g[0])

u = g[0]
v = g[1]
print(g.adj(u, v))
g.addedge(v, u)
print(g.adj(u, v))
print(g)
w = g.addvertex()
e = g.addedge(u, w)
print(e.tail())
print(e.head())
print(e.otherend(u))
print(g.V())
print(g.E())
print(u.deg())
print(u.nbs())
x = g.addvertex("Node1")
print(g)
print(x)