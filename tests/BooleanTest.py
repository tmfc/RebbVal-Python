import unittest

from rebbval.RebbVal import RebbVal
from rebbval.RebbValConfig import RebbValConfig


class BooleanTest(unittest.TestCase):

    def testBooleanTrue(self):
        v = RebbVal()
        self.assertTrue(v.val(True, "is true"))
        self.assertFalse(v.val(False, "is true"))

    def testNumberTrue(self):
        v = RebbVal()
        self.assertTrue(v.val(1, "is true"))
        self.assertFalse(v.val(0, "is true"))

    def testStringTrue(self):
        v = RebbVal()
        self.assertTrue(v.val("1", "is true"))
        self.assertTrue(v.val("on", "is true"))
        self.assertTrue(v.val("true", "is true"))
        self.assertTrue(v.val("yes", "is true"))
        self.assertFalse(v.val("0", "is true"))

    def testStringTrueConfigured(self):
        v = RebbVal()
        v.add_config(RebbValConfig.TRUE_STRING, ['true'])
        self.assertFalse(v.val("1", "is true"))
        self.assertFalse(v.val("on", "is true"))
        self.assertTrue(v.val("true", "is true"))
        self.assertFalse(v.val("yes", "is true"))
        self.assertFalse(v.val("0", "is true"))

    def testStringTrueGlobalConfigured(self):
        RebbVal.add_global_config(RebbValConfig.TRUE_STRING, ["true"])
        v = RebbVal()
        self.assertFalse(v.val("1", "is true"))
        self.assertFalse(v.val("on", "is true"))
        self.assertTrue(v.val("true", "is true"))
        self.assertFalse(v.val("yes", "is true"))
        self.assertFalse(v.val("0", "is true"))

    def testBooleanFalse(self):
        v = RebbVal()
        self.assertTrue(v.val(False, "is false"))
        self.assertFalse(v.val(True, "is false"))

    def testNumberFalse(self):
        v = RebbVal()
        self.assertTrue(v.val(0, "is false"))
        self.assertFalse(v.val(1, "is false"))

    def testStringFalse(self):
        v = RebbVal()
        self.assertFalse(v.val("1", "is false"))
        self.assertFalse(v.val("on", "is false"))
        self.assertFalse(v.val("true", "is false"))
        self.assertFalse(v.val("yes", "is false"))
        self.assertTrue(v.val("0", "is false"))


if __name__ == '__main__':
    unittest.main()
