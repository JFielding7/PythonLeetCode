def kth_smallest(node, k):
    if node is None:
        return None

    res = kth_smallest(node.left, k)
    if res is not None:
        return res

    k[0] -= 1

    return node.val if k[0] == 0 else kth_smallest(node.right, k)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return kth_smallest(root, [k])
