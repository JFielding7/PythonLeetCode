def path_sums(node, target, curr_path, paths):
    if node is None:
        return

    target -= node.val
    curr_path.append(node.val)

    if target == 0 and node.left is None and node.right is None:
        paths.append(curr_path[:])

    path_sums(node.left, target, curr_path, paths)
    path_sums(node.right, target, curr_path, paths)

    curr_path.pop()


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        path_sums(root, targetSum, [], paths)
        return paths