from time import time


class Node:
    __slots__ = 'l', 'r', 'v', 'parent'

    def __init__(self, value):
        self.l = None
        self.r = None
        self.v = value
        self.parent = None

    def __str__(self):
        return "({}, {}, {})".format(self.l, self.v, self.r)

    def __eq__(self, other):
        if self.v == other.v:
            return True
        return False


def timer_count_and_runtime(func):
    func.__call_count__ = 0

    def wrapper(*args, **kwargs):
        func.__call_count__ += 1
        time_satrt = time()
        res = func(*args, **kwargs)
        print("{0} was called {1} times, runtime: {2}".format(
            func.__name__, func.__call_count__, time()-time_satrt))
        return res
    return wrapper


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
        if value == cur_node.v:
            print("Such element already in tree")
            return
        if value < cur_node.v:
            if not cur_node.l:
                cur_node.l = Node(value)
                cur_node.l.parent = cur_node
            else:
                self.__insert(cur_node.l, value)
        else:
            if not cur_node.r:
                cur_node.r = Node(value)
                cur_node.r.parent = cur_node
                return
            else:
                self.__insert(cur_node.r, value)

    def search(self, value):
        if self.__root:
            return self.__search(self.__root, value)
        return self.__root

    def __search(self, cur_node, value):
        if cur_node.v == value:
            return cur_node
        if value < cur_node.v:
            if cur_node.l:
                return self.__search(cur_node.l, value)
            else:
                return None
        if value > cur_node.v:
            if cur_node.r:
                return self.__search(cur_node.r, value)
            else:
                return None

    def __contains__(self, value):
        if self.__root:
            return self.__search(self.__root, value)
        return None

    def __str__(self):
        self.__tree_view = ""
        self.__rRl(self.__root, 0)
        return self.__tree_view if len(self.__tree_view) > 0 else "Empty Tree"

    def __rRl(self, node, l):
        if node:
            self.__rRl(node.r, l+1)
            self.__tree_view += " "*4*l
            if node:
                self.__tree_view += str(node.v) + ("\n")
            self.__rRl(node.l, l+1)

    def remove(self, value):
        if self.__root:
            target_elements = self.__search(self.__root, value)
            if target_elements:
                return self.__remove(target_elements)
            else:
                print("No such element")
                return False
        print("Empty Tree")
        return False

    def __remove(self, node):
        """CASE 1: 0 children"""
        if not node.l and not node.r:
            parent_node = node.parent
            if parent_node:
                if parent_node.l == node:
                    parent_node.l = None
                else:
                    parent_node.r = None
                return True
            else:
                self.__root = None
                return True
        """CASE 2: 1 children"""
        if node.l or node.r:
            target_node = node.l or node.r
            parent_node = node.parent
            if parent_node:
                if parent_node.l == node:
                    parent_node.l = None
                    parent_node.l = target_node
                    target_node.parent = parent_node
                else:
                    parent_node.r = None
                    parent_node.r = target_node
                    target_node.parent = parent_node
                return True
            else:
                self.__root = node
        """CASE 3: 2 children"""


if __name__ == "__main__":
    inst = BinTree()
    values = (2, 1, 4, 6, 5)
    for i in values:
        inst.insert(i)
    remove_values = (4, 6)
    for remove_value in remove_values:
        print("------------")
        # print(inst)
        inst.remove(remove_value)
        # print(inst)
