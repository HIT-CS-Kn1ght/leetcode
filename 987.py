from utils.binary_tree import BuildTree


def DFS(node, col_num, r_dic, row_num):
    """
    :param node: TreeNode
    :param col_num: int
    :param row_num: int
    :param r_dic: dict
    :return: min_col
    """

    if node is None:
        return

    if col_num in r_dic.keys():
        if row_num in r_dic[col_num].keys():
            r_dic[col_num][row_num].append(node.val)
        else:
            r_dic[col_num][row_num] = [node.val]
    else:
        r_dic[col_num] = {row_num: [node.val]}

    DFS(node.left, col_num - 1, r_dic, row_num + 1)
    DFS(node.right, col_num + 1, r_dic, row_num + 1)


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        r_dic = dict()
        DFS(root, 0, r_dic, 0)
        res = []
        for i in range(min(r_dic.keys()), 1+max(r_dic.keys())):
            arr = []
            j = min(r_dic[i].keys())
            while j <= max(r_dic[i].keys()):
                if j in r_dic[i].keys():
                    arr += sorted(r_dic[i][j])
                j += 2
            res.append(arr)
        return res


if __name__ == '__main__':
    s = Solution()
    r_array = [3, 1, 4, 1000, 2, 2]
    r = BuildTree(r_array)
    print(s.verticalTraversal(r))
