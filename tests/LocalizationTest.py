import unittest

from rebbval.RebbVal import RebbVal


class LocalizationTest(unittest.TestCase):
    def test_gb_code(self):
        v = RebbVal()
        self.assertTrue(v.val("110101", "is gbcode"))
        self.assertFalse(v.val("100100", "is gbcode"))
        self.assertFalse(v.val("13113113111", "is gbcode"))


if __name__ == '__main__':
    unittest.main()
