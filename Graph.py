class Node:
    def __init__(self, id):
        self.parents = []
        self.children = []
        self.id = id

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.children.append(child)

    def is_child(self, node_id):
        for child in self.children:
            if child.id == node_id: return True
        return False


class Graph:
    def __init__(self, node):
        self.head = node

    def add_node(self, parent_id, new_node):
        # search graph for node with matching id
        parent_found = False
        current_node = self.head

        while not parent_found:
            if current_node.id == parent_id:
                parent_found = True
            else:
                for child in current_node.children:

    # parent.children.append(new_node)
    # new_node.parents.append(parent)
