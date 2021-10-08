import unittest

from rebbval.RebbVal import RebbVal


class NumberTest(unittest.TestCase):
    def test_number_between(self):
        v = RebbVal()
        condition = "between 10 and 20"
        
        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(8.8, condition))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("8.8 between 10 and 20 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

    def testNumberInterval(self):
        v = RebbVal()
        condition = "[5..20]"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(0.8, condition))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("0.8 [5..20] failed", v.errors[0])

        self.assertTrue(v.val(5.1, "(5..20]"))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(5, "(5..20]"))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("5 (5..20] failed", v.errors[0])

        self.assertFalse(v.val(20, "[5..20)"))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("20 [5..20) failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

    def testNumberEqual(self):
        v = RebbVal()
        condition = "=10"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(8.8, condition))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("8.8 =10 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))
    


    def testNumberNotEqual(self):
        v = RebbVal()
        condition = "!=10"

        # double
        self.assertTrue(v.val(100.0, condition))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(10, condition))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("10 !=10 failed", v.errors[0])

        # float
        self.assertTrue(v.val(100.0, condition))
        self.assertEquals(0, len(v.errors))

        # integer
        self.assertTrue(v.val(100, condition))
        self.assertEquals(0, len(v.errors))

        # long
        self.assertTrue(v.val(100, condition))
        self.assertEquals(0, len(v.errors))
    


    def testNumberLT(self):
        v = RebbVal()
        condition = "<100"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(188.8, condition))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("188.8 <100 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

    def testNumberLTE(self):
        v = RebbVal()
        condition = "<=100"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(188.8, condition))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("188.8 <=100 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

    def testNumberGT(self):
        v = RebbVal()
        condition = ">1"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(0.8, condition))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("0.8 >1 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

    def testNumberGTE(self):
        v = RebbVal()
        condition = ">=10"

        # double
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        self.assertFalse(v.val(8.8, condition))
        self.assertEquals(1, len(v.errors))
        self.assertEquals("8.8 >=10 failed", v.errors[0])

        # float
        self.assertTrue(v.val(10.0, condition))
        self.assertEquals(0, len(v.errors))

        # integer
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))

        # long
        self.assertTrue(v.val(10, condition))
        self.assertEquals(0, len(v.errors))
    

if __name__ == '__main__':
    unittest.main()
