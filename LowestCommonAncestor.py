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
            contains_lca = False
            for ancestor in family_tree:
                if ancestor is lca:
                    contains_lca = True
                    break
            # if it gets here and the lca hasnt been founf then this lca isnt in this tree

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
