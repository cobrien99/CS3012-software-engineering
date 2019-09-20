from treelib import Tree, Node


def make_tree():
    tree = Tree()
    tree.create_node("A", "a")
    tree.create_node("b", "b", parent="a")
    tree.create_node("c", "c", parent="a")
    tree.create_node("d", "d", parent="a")
    tree.create_node("e", "e", parent="d")
    tree.create_node("f", "f", parent="b")
    tree.create_node("g", "g", parent="f")
    return tree



def lca(tree, list_of_descendants):
    list_of_family_trees = []
    shortest_family_tree = None
    for descendant in list_of_descendants:  # descendant is a string id for that node
        family_tree = find_heritage(tree, descendant)
        # find the shortest family_tree
        if (shortest_family_tree is None) or (len(family_tree) < len(shortest_family_tree)):
            shortest_family_tree = family_tree
        list_of_family_trees.append(family_tree)

    # begin the search for lca at the base of the shortest family_tree

    for lca in shortest_family_tree:
        contains_lca = False

        # check if the current possible lca is in all other family trees
        for family_tree in list_of_family_trees:
            for ancestor in family_tree:
                if ancestor is lca:
                    contains_lca = True
                    break

            if contains_lca is False:
                break

        if contains_lca is True:  # if all trees contain this same lca then we are done
            return lca


def find_heritage(tree, descendant):  # finds the chain from a given descendant to root
    chain = [descendant]  # adds this descendants id to the chain
    while tree.parent(descendant) is not None:
        descendant = tree.parent(descendant).identifier
        chain.append(descendant)
    return chain


# pick nodes you want to find the LCA of
