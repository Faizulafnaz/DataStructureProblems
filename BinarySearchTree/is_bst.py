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


    def is_bst(self):

        if self.left_child:
            if self.left_child.key > self.key:
                return print(False)
            else:
                self.left_child.is_bst()

        elif self.right_child:
            if self.right_child.key < self.key:
                return print(False)
            else:
                self.right_child.is_bst()
        else:
            return print(True)

    def search(self, target):

        if self.key == target:
            return print("value present in bst")

        if target < self.key:
            if self.left_child:
                self.left_child.search(target)
            else:
                return print("value not present in bst")

        elif target > self.key:
            if self.right_child:
                self.right_child.search(target)
            else:
                return print("value not present in bst")

    def deletion(self, data):

        if self.key is None:
            print("it's an empty bst")
            return
        if self.left_child is None and self.right_child is None:
            self.key = None
            return
        if self.key > data:
            if self.left_child:
                self.left_child = self.left_child.deletion(data)
            else:
                print("value not present in bst")

        elif self.key < data:
            if self.right_child:
                self.right_child = self.right_child.deletion(data)
            else:
                print("value not present in bst")

        else:
            if self.right_child is None:
                temp = self.left_child
                self = None

                return temp

            elif self.left_child is None:
                temp = self.right_child
                self = None

                return temp

            else:
                node = self.right_child
                while node.left_child:
                    node = node.left_child
                self.key = node.key
                self.right_child = self.right_child.deletion(node.key)

        return self






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
bst.is_bst()
bst.search(34)
bst.deletion(43)
bst.deletion(6)
bst.deletion(1)
bst.deletion(34)
bst.deletion(54)
bst.deletion(8)
bst.deletion(5)
bst.deletion(2)
bst.deletion(23)
bst.deletion(7)


bst.inorder()