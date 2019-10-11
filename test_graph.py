from unittest import TestCase
from Graph import Node, Graph
import networkx as nx


class TestGraph(TestCase):
    def test_make_node(self):
        self.node = Node("A")
        self.assertEqual(self.node.id, "A")

    def test_add_parent(self):
        self.node1 = Node("A")
        self.node2 = Node("B")
        self.node1.add_parent(self.node2)
        self.assertEqual(self.node1.parents[0].id, "B")

    def test_add_child(self):
        self.node1 = Node("A")
        self.node2 = Node("B")
        self.node1.add_child(self.node2)
        self.assertEqual(self.node1.children[0].id, "B")

    def test_is_child(self):
        self.node1 = Node("A")
        self.node2 = Node("B")
        self.node1.add_child(self.node2)
        self.assertTrue(self.node1.is_child("B"))

    def test_make_graph(self):
        self.node1 = Node("A")
        self.graph = Graph(self.node1)
        self.assertEqual(self.graph.head.id, "A")

    def test_add_node(self, new_node, parent_id):
        self.node1 = Node("A")
        self.graph = Graph(self.node1)
        self.graph.add_node(new_node, parent_id)
        self.assertEqual(self.graph.head.child[0].id, "B")
