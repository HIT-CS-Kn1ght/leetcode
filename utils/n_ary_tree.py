# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children

    def add_children(self, children_list):
        self.children = children_list


# 完全二叉树的数组建树
def BuildTree(array):
    if not len(array):
        return None

    root = Node(array[0])
    current_layer = [root]
    i = 2
    while i < len(array):
        parents_list = current_layer
        current_layer = []
        for j in range(len(parents_list)):
            parent = parents_list[j]
            if i >= len(array):
                break
            children = []
            while array[i]:
                n = Node(array[i])
                children.append(n)
                current_layer.append(n)
                i += 1
                if i >= len(array):
                    break
            i += 1
            parent.add_children(children)

    return root


if __name__ == '__main__':
    r_array = [1, 0, 2, 3, 4, 5, 0, 0, 6, 7, 0, 8, 0, 9, 10, 0, 0, 11, 0, 12, 0, 13, 0, 0, 14]
    r = BuildTree(r_array)
    print(r.children[2].children[0].val)
