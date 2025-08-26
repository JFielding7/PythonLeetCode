def connect_same_level_nodes(node, level, level_tail_nodes):
    if node is None:
        return

    node.next = None
    if level == len(level_tail_nodes):
        level_tail_nodes.append(node)
    else:
        level_tail_nodes[level].next = node
        level_tail_nodes[level] = node

    connect_same_level_nodes(node.left, level + 1, level_tail_nodes)
    connect_same_level_nodes(node.right, level + 1, level_tail_nodes)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        connect_same_level_nodes(root, 0, [])
        return root