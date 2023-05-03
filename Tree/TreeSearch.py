class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self):
        print(self.data, end=" ")
        if self.left:
            self.left.printTree()

        if self.right:
            self.right.printTree()

    def TreeSearch(self, target):

        if self.data == target:
            return print("value present in tree")

        if self.left:
            self.left.TreeSearch(target)
        if self.right:
            self.right.TreeSearch(target)




root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.TreeSearch(6)