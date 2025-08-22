class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return root is not None and targetSum == root.val if root is None or root.left is None and root.right is None else self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)