import unittest

from rebbval.RebbVal import RebbVal


class AgeTest(unittest.TestCase):
    def test_age_compare(self):
        v = RebbVal()

        date1 = v.date('2019-05-01')

        self.assertFalse(v.val(date1, "older than a_string"))

        self.assertTrue(v.val(date1, "younger than 18"))
        self.assertFalse(v.val(date1, "older than 18"))
        self.assertTrue(v.val(date1, "older than 1.8"))

        date2 = v.date("1980-05-01")

        self.assertFalse(v.val(date2, "younger than 18"))
        self.assertTrue(v.val(date2, "older than 18"))

        self.assertFalse(v.val(v.date("2003-01-01"), "younger than 18"))
        self.assertTrue(v.val(v.date("2003-01-01"), "older than 18"))

        self.assertTrue(v.val(v.date("2004-01-01"), "younger than 18"))
        self.assertFalse(v.val(v.date("2004-01-01"), "older than 18"))


if __name__ == '__main__':
    unittest.main()
