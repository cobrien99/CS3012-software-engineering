from unittest import TestCase
import networkx as nx
import LowestCommonAncestor as Lca


class TestLca(TestCase):
    def createGraph(self):
        self.g = nx.DiGraph()

    def test_find_ancestors(self):
        self.g = nx.DiGraph()
        self.g.add_edges_from([(1, 2), (1, 3), (3, 4), (2, 5), (4, 6), (5, 6), (2, 7)])
        ancestors = Lca.find_node_ancestors(self.g, 1)
        self.assertEqual(ancestors, [(2, 1), (3, 1), (5, 2), (7, 2), (6, 3), (4, 2), (6, 3)])

    def test_lca(self):
        self.g = nx.DiGraph()
        self.g.add_edges_from([(1, 2), (1, 3), (3, 4), (2, 5), (4, 6), (5, 6), (2, 7)])
        lca = Lca.lowest_common_ancestor(self.g, [1, 2])
        print(lca)
        self.assertEqual(lca, 6)
