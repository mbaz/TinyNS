# TinyNS Simulator
#
# Copyright © 2018 Miguel Bazdresch <mxbiee@rit.edu>
# Rochester Institute of Technology
#
# This file is distributed under the 2-clause BSD License.

from random import random, choice

# Define Packet class
class Packet:
    # Class initializer
    def __init__(self, s_addr, d_addr, payload):
        self.s_addr = s_addr
        self.d_addr = d_addr
        self.payload = payload

# Define EdgeNode class. These nodes are origin and ultimate destination of
#  all packets. EdgeNodes have only one port.
class EdgeNode:
    # Class initializer
    def __init__(self, address, d_addr_set, tx_prob):
        self.address = address
        self.d_addr_set = d_addr_set
        self.tx_prob = tx_prob
        self.memory = []

    def isedge(self):
        return True

    def isswitch(self):
        return False

    # take an action after transmitting
    def txaction(self, pkt, time):
        return None

    # take an action after receiving
    def rxaction(self, pkt, time):
        return None

    # Transmit a packet
    def transmit(self, time):
        # Determine if a packet will be generated
        if random() < self.tx_prob:
            # Determine destination address
            d_addr = choice(self.d_addr_set)
            # instantiate packet
            pkt = Packet(self.address, d_addr, 'dummy payload')
            self.txaction(pkt, time)
            return pkt
        else:
            return None

    # Receive a message from the buffer
    def receive(self, time):
        if len(self.memory) > 0:
            pkt = self.memory.pop()
            self.rxaction(pkt, time)

# Define SwitchNode class. These nodes store and forward packets.
class SwitchNode:
    # Class initializer
    def __init__(self, ID, ports, rt):
        self.ID = ID
        self.ports = ports
        self.rt = rt
        self.memory = []

    def isedge(self):
        return False

    def isswitch(self):
        return True

    # take an action after forwarding
    def action(self, pkt, outport):
        return None

    # execute forwarding
    def forward(self, time):
        # if there is something in memory, process it
        if len(self.memory) > 0:
            pkt = self.memory.pop()
            # determine output port
            outport = None
            for i in self.rt:
                if i == pkt.d_addr:
                    outport = self.rt[i]
            # execute an action
            self.action(pkt, outport)
            # return packet and output port
            return pkt, outport
        else:
            return None, None

# Auxiliary functions

# List of connections
class ConnectionList:
    def __init__(self):
        self.connlist = []

    def connect(self, node1, port1, node2, port2):
        self.connlist.append((node1, port1, node2, port2))

# List of nodes
class NodeList:
    def __init__(self):
        self.nodelist = []

    def append_node(self, node):
        self.nodelist.append(node)

# Given a connection list, a node, and a port, find the node it is
# connected to.
def findnextnode(connlist, node, port):
    for c in connlist.connlist:
        if (c[0] == node) & (c[1] == port):
            return c[2]
        elif (c[2] == node) & (c[3] == port):
            return c[0]
    return None

# Round-robin scheduler:
#   All edge nodes receive
#   All switch nodes forward
#   All edge nodes transmit
def run(nodelist, connlist, iterations):
    for i in range(iterations):
        # Edge nodes receive
        for n in nodelist.nodelist:
            if n.isedge():
                n.receive(i)
        # Switch nodes forward
        for n in nodelist.nodelist:
            if n.isswitch():
                pkt, port = n.forward(i)
                if pkt != None:
                    nextnode = findnextnode(connlist, n, port)
                    nextnode.memory.insert(0,pkt)
        # Edge nodes transmit
        for n in nodelist.nodelist:
            if n.isedge():
                pkt = n.transmit(i)
                if pkt != None:
                    nextnode = findnextnode(connlist, n, '1')
                    nextnode.memory.insert(0,pkt)
    print("Done!")
