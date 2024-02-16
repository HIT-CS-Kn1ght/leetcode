import collections
from binary_tree import BuildTree


def BFS(root):
    res = []
    q = collections.deque()
    if root:
        q.append(root)
        while q:
            level_res = []
            level_len = len(q)
            for _ in range(level_len):
                node = q.popleft()
                level_res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(res) & 1:
                level_res.reverse()
            res.append(level_res)
    return res


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return BFS(root)


if __name__ == '__main__':
    s = Solution()
    r_array = [3, 9, 20, 0, 0, 15, 7]
    r = BuildTree(r_array)
    print(s.zigzagLevelOrder(r))
