# where I will write code to test my LCA code works

from treelib import Tree
import random

# function to generate a random tree with a given number of nodes
from LowestCommonAncestor import lca


def generate_tree(number_of_nodes):
    tree = Tree()

    for i in range(0, number_of_nodes):
        if i == 0:
            tree.create_node("0", "0")  # create the root first
        else:
            # pick a random previous node tobe the parent
            parent_node = random.randint(0, i - 1)
            tree.create_node(str(i), str(i), parent=str(parent_node))

    return tree


tree = generate_tree(1000)
tree.show()

descendants = ["200", "900", "234"]
lca = lca(tree, descendants)
print("the lca of " + str(descendants) + " is " + lca)
