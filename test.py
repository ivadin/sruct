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

    # def test_remove(self);
    #     inst = BinTree()
    #     inst.insert(2)
    #     inst.insert(1)
    #     inst.insert(3)
    #     inst.insert(4)
    #     self.assertIn(3, inst)
    #     inst.remove(3)
    #     self.assertNotIn(3, inst)


if __name__ == "__main__":
    unittest.main()
