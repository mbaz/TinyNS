# Simple test case: three edge nodes and one switch

from tinyns import *

e1 = EdgeNode('E1',['E2'],1)
e2 = EdgeNode('E2',['E1','E3'],1)
e3 = EdgeNode('E3',['E1','E2'],1)
s = SwitchNode('S',['1','2','3'],dict([('E1','1'),('E2','2'),('E3','3')]))
nl = NodeList()
nl.append_node(e1)
nl.append_node(e2)
nl.append_node(e3)
nl.append_node(s)
cl = ConnectionList()
cl.connect(e1,'1',s,'1')
cl.connect(e2,'1',s,'2')
cl.connect(e3,'1',s,'3')
run(nl,cl,10)
