class Node:
    __slots__ = 'l', 'r', 'v'

    def __init__(self, value):
        self.l = None
        self.r = None
        self.v = value


class BinTree:
    __slots__ = 'root', 'tree_view'

    def __init__(self):
        self.root = None
        self.tree_view = ''

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, cur_node, value):
        if value < cur_node.v:
            if not cur_node.l:
                cur_node.l = Node(value)
                return
            else:
                self.__insert(cur_node.l, value)
        else:
            if not cur_node.r:
                cur_node.r = Node(value)
                return
            else:
                self.__insert(cur_node.r, value)

    def search(self, cur_node, value):
        if cur_node.v == value:
            return True
        if value < cur_node.v:
            if cur_node.l:
                return self.search(cur_node.l, value)
            else:
                return False
        if value > cur_node.v:
            if cur_node.r:
                return self.search(cur_node.r, value)
            else:
                return False

    def __contains__(self, value):
        return self.search(self.root, value)

    def __str__(self):
        self.tree_view = ""
        self.__rRl(self.root, 0)
        return self.tree_view

    def __rRl(self, node, l):
        if node:
            self.__rRl(node.r, l+1)
            self.tree_view += " "*4*l
            if node:
                self.tree_view += str(node.v) + ("\n")
            self.__rRl(node.l, l+1)


bt = BinTree()
bt.insert(1)
bt.insert(2)
bt.insert(0.5)
bt.insert(3)
print(bt)
print(0 in bt)
