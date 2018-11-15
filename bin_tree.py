class Node:
    __slots__ = 'l', 'r', 'v'

    def __init__(self, value):
        self.l = None
        self.r = None
        self.v = value


class BinTree:
    __slots__ = 'root'

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, cur_node, value):
        if value < cur_node.v:
            if not cur_node.l:
                cur_node.l = Node(value)
                return
            else:
                self._insert(cur_node.l, value)
        else:
            if not cur_node.r:
                cur_node.r = Node(value)
                return
            else:
                self._insert(cur_node.r, value)

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


bt = BinTree()
bt.insert(1)
bt.insert(2)
