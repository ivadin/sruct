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


if __name__ == "__main__":
    unittest.main()
