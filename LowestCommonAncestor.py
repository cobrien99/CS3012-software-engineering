def find_node_ancestors(graph, node, depth=None):
    if depth is None:
        depth = 1
    ancestors = []
    for successor in list(graph.successors(node)):
        ancestors.append((successor, depth))
    depth += 1
    for successor in list(graph.successors(node)):
        ancestors += find_node_ancestors(graph, successor, depth)
    return ancestors


def lowest_common_ancestor(graph, list_of_nodes):
    other_ancestors = []
    shortest_list = []
    for node in list_of_nodes:
        ancestors = find_node_ancestors(graph, node)
        ancestors.sort(key=lambda tup: tup[1], reverse=True)  # sort the list in order of decreasing depth

        if (len(shortest_list) is 0) or (len(ancestors) < len(shortest_list)):
            shortest_list = ancestors
        else:
            other_ancestors.append(ancestors)

    for node in shortest_list:
        for ancestors in other_ancestors:
            if does_list_contain_node(ancestors, node[0]) is False:
                break  # lca not found check next node
        return node[0]  # lca found
    return None  # lca does not exist


def does_list_contain_node(list_of_nodes, key):
    contains_node = False

    for node in list_of_nodes:
        if node[0] is key:
            contains_node = True
            break

    return contains_node
