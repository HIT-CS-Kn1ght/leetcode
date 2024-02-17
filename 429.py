import collections

from utils.n_ary_tree import BuildTree


def BFS(root):
    res = []
    if root:
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            parents_len = len(q)
            for _ in range(parents_len):
                parent = q.popleft()
                level.append(parent.val)
                if not parent.children:
                    continue
                for child in parent.children:
                    q.append(child)
            res.append(level)
    return res


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        return BFS(root)


if __name__ == '__main__':
    s = Solution()
    r_array = [1, 0, 2, 3, 4, 5, 0, 0, 6, 7, 0, 8, 0, 9, 10, 0, 0, 11, 0, 12, 0, 13, 0, 0, 14]
    r = BuildTree(r_array)
    print(s.levelOrder(r))
