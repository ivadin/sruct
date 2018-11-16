class Node:
    __slots__ = 'l', 'r', 'v'

    def __init__(self, value):
        self.l = None
        self.r = None
        self.v = value


class BinTree:
    __slots__ = '__root', '__tree_view'

    def __init__(self):
        self.__root = None
        self.__tree_view = ''

    def insert(self, value):
        if not self.__root:
            self.__root = Node(value)
        else:
            self.__insert(self.__root, value)

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

    def search(self, value):
        return self.__search(self.__root, value)

    def __search(self, cur_node, value):
        if cur_node.v == value:
            return True
        if value < cur_node.v:
            if cur_node.l:
                return self.__search(cur_node.l, value)
            else:
                return False
        if value > cur_node.v:
            if cur_node.r:
                return self.__search(cur_node.r, value)
            else:
                return False

    def __contains__(self, value):
        return self.__search(self.__root, value)

    def __str__(self):
        self.__tree_view = ""
        self.__rRl(self.__root, 0)
        return self.__tree_view

    def __rRl(self, node, l):
        if node:
            self.__rRl(node.r, l+1)
            self.__tree_view += " "*4*l
            if node:
                self.__tree_view += str(node.v) + ("\n")
            self.__rRl(node.l, l+1)

    # def remove(self, value):
    #     return self.__remove(self.__root, value)

    # def __remove(self, node, value):
    #     if node.l and node.l.v == value:
    #         tmp_value = node.l
    #         del node.l