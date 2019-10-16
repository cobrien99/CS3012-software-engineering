from unittest import TestCase
import networkx as nx
import LowestCommonAncestor as Lca


class TestLca(TestCase):
    def test_createGraph(self):
        self.g = nx.DiGraph()

    def test_find_ancestors(self):
        self.g = nx.DiGraph()
        self.g.add_edges_from([(1, 2), (1, 3), (3, 4), (2, 5), (4, 6), (5, 6), (2, 7)])
        ancestors = Lca.find_node_ancestors(self.g, 1)
        self.assertEqual(ancestors, [(1, 0), (2, 1), (3, 1), (5, 2), (7, 2), (6, 3), (4, 2), (6, 3)])

    def test_lca(self):
        self.g = nx.DiGraph()
        self.g.add_edges_from([(1, 2), (1, 3), (3, 4), (2, 5), (4, 6), (5, 6), (2, 7), (6, 8)])

        # basic test
        lca = Lca.lowest_common_ancestor(self.g, [1, 2])
        self.assertEqual(lca, 2)

        # there is a node behinf the lca that's also an ancestor
        lca = Lca.lowest_common_ancestor(self.g, [3, 2])
        self.assertEqual(lca, 6)

        # test with more then two nodes
        lca = Lca.lowest_common_ancestor(self.g, [1, 2, 7])
        self.assertEqual(lca, 7)

        # test where no lca possible
        lca = Lca.lowest_common_ancestor(self.g, [3, 7])
        self.assertEqual(lca, None)
