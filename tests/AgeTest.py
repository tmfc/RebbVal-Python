import unittest

from rebbval.RebbVal import RebbVal


class AgeTest(unittest.TestCase):
    def test_age_compare(self):
        v = RebbVal()
        self.assertEqual(True, v.val(v.date('2020-05-01'), "younger than 18"))
        self.assertEqual(False, v.val(v.date('2020-05-01'), "younger than 1.8"))


if __name__ == '__main__':
    unittest.main()
