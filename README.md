# TinyNS
A small and simple network simulator

TinyTS is a very small and simple network simulator. The main purpose of TinyTS
is to enable you to implement, test and evaluate your own routing
algorithms in a variety of network topologies. Although this can be done in a
larger, professional simulator such as NS3, TinyNS has a number of features
that allow you to focus on the fundamentals, instead of spending your
time learning to use the tool:

* In its tiniest form, it is only 149 lines long. This means that you
  can understand the simulator inside and out, which makes it easier to
	modify it.
* It is written in Python, which is a very accessible language.
* It does not use discrete events. While this limits its
  power and flexibility, it results in a design that is very simple and
	easy to understand.

### The simulator

There are a few core ideas behind the simulator:

* There are two kinds of nodes: edge nodes and switches. An edge node
	generates and consumes packets; a switch forwards packets.
* Edge nodes have only one port; switches can have any number of ports.
* Nodes are connected by connecting their ports. Ports are
	bidirectional.
* The simulation consists of a repetition of these three steps:
	* Edge nodes are allowed to receive one packet.
	* Switches forward one packet stored in their memory.
	* Edge nodes are allowed to transmit a packet.

You can find a more complete tutorial [here](https://github.com/mbaz/TinyNS/raw/master/doc/TinyNS-Tutorial.pdf).
