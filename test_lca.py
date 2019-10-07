from unittest import TestCase
from treelib import Tree
from LowestCommonAncestor import lca


class TestLca(TestCase):
    def setUp(self):
        self.tree = Tree()

    def testLca(self):
        self.tree.create_node("Harry", "harry")  # root node
        self.tree.create_node("Jane", "jane", parent="harry")
        self.tree.create_node("Bill", "bill", parent="harry")
        self.tree.create_node("Diane", "diane", parent="jane")
        self.tree.create_node("Mary", "mary", parent="diane")
        self.tree.create_node("Mark", "mark", parent="jane")
        result = lca(self.tree, ["mark", "mary"])
        self.assertEquals(result, "jane")
