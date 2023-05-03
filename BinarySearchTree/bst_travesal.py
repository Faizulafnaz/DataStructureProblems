class BinarySearchTree:
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

    def insertion(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key > data:
            if self.left_child:
                self.left_child.insertion(data)
            else:
                self.left_child = BinarySearchTree(data)

        elif self.key < data:
            if self.right_child:
                self.right_child.insertion(data)
            else:
                self.right_child = BinarySearchTree(data)

    def preorder(self):

        print(self.key, end=" ")

        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()


    def inorder(self):

        if self.left_child:
            self.left_child.inorder()

        print(self.key, end=" ")

        if self.right_child:
            self.right_child.inorder()

    def postorder(self):

        if self.left_child:
            self.left_child.postorder()

        if self.right_child:
            self.right_child.postorder()

        print(self.key, end=" ")



bst = BinarySearchTree(None)
lst = [32, 1, 34, 54, 6, 7, 8, 5, 43, 2, 23]
for i in lst:
    bst.insertion(i)

bst.preorder()
print()
bst.inorder()
print()
bst.postorder()
print()