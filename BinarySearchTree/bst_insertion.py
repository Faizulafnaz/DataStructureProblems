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


bst = BinarySearchTree(None)
lst = [32, 1, 34, 54, 6, 7, 8, 5, 43, 2, 23]
for i in lst:
    bst.insertion(i)