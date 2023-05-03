class Trie:
    head = {}

    def insertion(self, word):
        cur = self.head
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur["*"] = {}


obj = Trie()
obj.insertion("faiz")
obj.insertion("febi")
obj.insertion("fiju")
print(obj.head)
