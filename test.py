import unittest
from bin_tree import BinTree


class Testing(unittest.TestCase):
    def test_insert_digits(self):
        inst = BinTree()
        inst.insert(2)
        inst.insert(1)
        inst.insert(3)
        self.assertIn(1, inst)

    def test_insert_str(self):
        inst = BinTree()
        inst.insert("asd")
        inst.insert("asb")
        inst.insert("as")
        self.assertIn("as", inst)

    def test_add_mix_data(self):
        inst = BinTree()
        inst.insert("asd")
        inst.insert("asb")
        self.assertRaises(TypeError, inst.insert, 1)

    def test_remove_from_Empty(self):
        inst = BinTree()
        self.assertFalse(inst.remove(1))

    def test_remove_Node_root(self):
        inst = BinTree()
        inst.insert(1)
        remove_value = 1
        self.assertIn(remove_value, inst)
        inst.remove(remove_value)
        self.assertNotIn(remove_value, inst)

    def test_remove_node_0_children(self):
        inst = BinTree()
        values = (2, 1, 4, 3, 5)
        for i in values:
            inst.insert(i)
        remove_value = 1
        self.assertIn(remove_value, inst)
        inst.remove(remove_value)
        self.assertNotIn(remove_value, inst)


if __name__ == "__main__":
    unittest.main()
