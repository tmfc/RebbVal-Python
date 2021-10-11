import unittest

from rebbval.RebbVal import RebbVal


class ArrayTest(unittest.TestCase):
    def testUnaryTests(self):
        v = RebbVal()
        self.assertTrue(v.val(10000, ">10 and <1000 or =10000"))
        self.assertTrue(v.val(1000, ">10 and <100000 and !=10000"))
        self.assertFalse(v.val(1000, ">10 and <100 or =10000"))
        self.assertTrue(v.val(1000, ">100 or <10 or =10000"))

    def testConjunction(self):
        v = RebbVal()
        self.assertTrue(v.val(100, ">10 and <1000"))
        self.assertFalse(v.val(100, ">10 and <100"))

    def testDisjunction(self):
        v = RebbVal()
        self.assertTrue(v.val(70, ">60 or <10"))
        self.assertTrue(v.val(5, ">60 or <10"))
        self.assertFalse(v.val(30, ">60 or <10"))

    def testNot(self):
        v = RebbVal()
        self.assertFalse(v.val(100, "<10"))
        self.assertTrue(v.val(100, "not (<10)"))
        self.assertTrue(v.val(100, "not <10"))
    

if __name__ == '__main__':
    unittest.main()
