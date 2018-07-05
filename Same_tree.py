class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSameTree(self, p , q):
        if p is None and q is None:
            return True
        if p is not None or q is not None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

if __name__ == '__main__':
    tree1 = [1,2,3]
    tree2 = [1,2,3]
    p = []
    q = []
    for i in range(len(tree1)):
        node = TreeNode(tree1[i])
        p.append(node)
    for i in range(len(p)//2):
        tree_node = p[i]
        tree_node.left = p[i*2+1]
        tree_node.right = p[i*2+2]

    for j in range(len(tree2)):
        node = TreeNode(tree2[i])
        q.append(node)

    for j in range(len(tree2)//2):
        tree_node = p[i]
        tree_node.left = q[i * 2 + 1]
        tree_node.right = q[i * 2 + 2]

    print(Solution().isSameTree(p[0], q[0]))

