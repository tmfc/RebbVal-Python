import unittest

from rebbval.RebbVal import RebbVal


class NumberTest(unittest.TestCase):
    def test_number_between(self):
        v = RebbVal()
        condition = "between 10 and 20"
        
        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(8.8, condition))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("8.8 between 10 and 20 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

    def test_number_interval(self):
        v = RebbVal()
        condition = "[5..20]"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(0.8, condition))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("0.8 [5..20] failed", v.errors[0])

        self.assertTrue(v.val(5.1, "(5..20]"))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(5, "(5..20]"))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("5 (5..20] failed", v.errors[0])

        self.assertFalse(v.val(20, "[5..20)"))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("20 [5..20) failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

    def test_number_equal(self):
        v = RebbVal()
        condition = "=10"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(8.8, condition))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("8.8 =10 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

    def test_number_not_equal(self):
        v = RebbVal()
        condition = "!=10"

        # double
        self.assertTrue(v.val(100.0, condition))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(10, condition))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("10 !=10 failed", v.errors[0])

        # float
        self.assertTrue(v.val(100.0, condition))
        self.assertEqual(0, len(v.errors))

        # integer
        self.assertTrue(v.val(100, condition))
        self.assertEqual(0, len(v.errors))

        # long
        self.assertTrue(v.val(100, condition))
        self.assertEqual(0, len(v.errors))

    def test_number_lt(self):
        v = RebbVal()
        condition = "<100"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(188.8, condition))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("188.8 <100 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

    def test_number_lte(self):
        v = RebbVal()
        condition = "<=100"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(188.8, condition))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("188.8 <=100 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

    def test_number_gt(self):
        v = RebbVal()
        condition = ">1"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(0.8, condition))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("0.8 >1 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

    def test_number_gte(self):
        v = RebbVal()
        condition = ">=10"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        self.assertFalse(v.val(8.8, condition))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("8.8 >=10 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEqual(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEqual(0, len(v.errors))
    

if __name__ == '__main__':
    unittest.main()
