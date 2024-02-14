# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_LeftSon(self, Node):
        self.left = Node

    def add_RightSon(self, Node):
        self.right = Node


# 完全二叉树的数组建树
def BuildTree(array):
    l = []
    root = TreeNode(array[0])
    l.append(root)
    i = 1
    while i < len(array):
        parent = l[(i+1)//2-1]
        if parent:
            if array[i]:
                left = TreeNode(array[i])
                parent.add_LeftSon(left)
            else:
                left = None
            l.append(left)

            if i == len(array) - 1:
                break

            if array[i+1]:
                right = TreeNode(array[i+1])
                parent.add_RightSon(right)
            else:
                right = None
            l.append(right)
        i += 2

    return root


if __name__ == '__main__':
    r_array = [3, 9, 20, 0, 0, 15, 7]
    r = BuildTree(r_array)
    print(r.right.right.val)
