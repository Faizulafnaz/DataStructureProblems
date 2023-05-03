class Trie:
    head = {}

    def insertion(self, word):
        cur = self.head
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur["*"] = {}

    def search(self, word):

        cur = self.head
        for i in word:
            if i not in cur:
                return print("word not in Trie")
            cur = cur[i]

        if "*" not in cur:
            print("word not in Trie")
        else:
            print("word found")




obj = Trie()
obj.insertion("faiz")
obj.insertion("febi")
obj.insertion("fiju")
obj.search('febi')
print(obj.head)
