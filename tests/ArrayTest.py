import unittest

from rebbval.RebbVal import RebbVal


class ArrayTest(unittest.TestCase):
    def test_number_in_array(self):
        v = RebbVal()
        self.assertTrue(v.val(1, "in [1, 2, 3]"))
        self.assertFalse(v.val(8, "in [1, 2, 3]"))
        self.assertTrue(v.val(8, "not in [1, 2, 3]"))

    def test_array_is_unique(self):
        v = RebbVal()
        self.assertTrue(v.val([1, 2, 3], "is unique"))
        self.assertFalse(v.val([1, 2, 2], "is unique"))

    def test_array_is_unique_type_not_support(self):
        v = RebbVal()
        self.assertFalse(v.val(8, "is unique"))
        self.assertTrue(1, v.has_error)
        self.assertEqual(1, len(v.errors))
        self.assertEqual("8 is unique failed(ObjectTypeNotSupported)", v.errors[0])

if __name__ == '__main__':
    unittest.main()
