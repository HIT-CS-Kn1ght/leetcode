from utils.binary_tree import BuildTree, TreeNode


def DFS(node, tar):
    if node is None:
        return []
    if node.val == tar.val:
        return [node]

    path = DFS(node.left, tar)
    if len(path):
        path.append(node)
        return path

    path = DFS(node.right, tar)
    if len(path):
        path.append(node)
        return path

    return []


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path, q_path = DFS(root, p), DFS(root, q)
        if len(p_path) > len(q_path):
            tmp = p_path
            p_path = q_path
            q_path = tmp
        length = len(p_path)
        dif = len(q_path) - len(p_path)
        for i in range(length):
            if p_path[i].val == q_path[i + dif].val:
                return p_path[i]


if __name__ == '__main__':
    s = Solution()
    r_array = [3, 5, 1, 6, 2, 10, 8, 0, 0, 7, 4]
    p1, q1 = TreeNode(5), TreeNode(4)
    r = BuildTree(r_array)
    print(s.lowestCommonAncestor(r, p1, q1).val)
