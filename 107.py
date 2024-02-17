import collections
from utils.binary_tree import BuildTree


def BFS(root):
    res = []
    q = collections.deque()
    if root:
        q.append((root, 0))
        while q:
            node = q.popleft()
            if len(res) == node[1]:
                res.append([node[0].val])
            else:
                res[node[1]].append(node[0].val)
            if node[0].left:
                q.append((node[0].left, node[1] + 1))
            if node[0].right:
                q.append((node[0].right, node[1] + 1))
    return res


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = BFS(root)
        res.reverse()
        return res


if __name__ == '__main__':
    s = Solution()
    r_array = [3, 9, 20, 0, 0, 15, 7]
    r = BuildTree(r_array)
    print(s.levelOrderBottom(r))
