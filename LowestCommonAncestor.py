# where I will write the code that will attempt to solve the
# lowest common ancestor problem

# load in new tree from file
# the root n is stored in tree[1]
# if a node occupies tree[k] then its left child is in tree[k*2]
# and its right child is in tree[k*2+1]

# familyTree = open("FamilyTrees/small.txt", "r")
# print(familyTree)
# doesnt work for some reason


class FamilyTree:
    def __init__(self, family_tree_string):
        self.string = family_tree_string

    def find_parent(self, node):
        node_pos = self.string.find(node)
        parent_pos = (node_pos+1)//2
        return parent_pos

    def find_node_at_pos(self, pos):
        return self.string[pos-1]


def lca(family_tree, list_of_descendants):
    node = ""

    return node


familyTree = FamilyTree("abcd-ef-h")
print(familyTree.find_parent("b"))
print(familyTree.find_parent("h"))
print(familyTree.find_node_at_pos(4))

# pick nodes you want to find the LCA of
