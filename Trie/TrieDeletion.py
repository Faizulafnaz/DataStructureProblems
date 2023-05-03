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

    def deletion(self, word):
        cur = self.head
        path = []

        for i in word:
            if i not in cur:
                return print("word not in Trie")
            path.append((cur, i))
            cur = cur[i]

        if "*" not in cur:
            return print("word not present in Trie")
        del cur["*"]
        for node, cur in reversed(path):
            if not node[cur]:
                del node[cur]
            else:
                break




obj = Trie()
obj.insertion("faiz")
obj.insertion("febi")
obj.insertion("fiju")
obj.search('febi')
obj.deletion('febi')
print(obj.head)
