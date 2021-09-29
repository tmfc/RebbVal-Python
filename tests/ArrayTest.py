import unittest

from rebbval.RebbVal import RebbVal


class ArrayTest(unittest.TestCase):
    def test_number_in_array(self):
        v = RebbVal()
        self.assertTrue(v.val(1, "in [1, 2, 3]"))
        self.assertFalse(v.val(8, "in [1, 2, 3]"))
        self.assertTrue(v.val(8, "not in [1, 2, 3]"))


if __name__ == '__main__':
    unittest.main()
