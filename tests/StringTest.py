import unittest

from rebbval.RebbVal import RebbVal


class StringTest(unittest.TestCase):
    def testStringEqual(self):
        v = RebbVal()
        self.assertTrue(v.val("a string", "='a string'"))
        self.assertFalse(v.val("not a string", "='a string'"))

    def testStringCompare(self):
        v = RebbVal()
        self.assertFalse(v.val("a string", ">'a string'"))
        self.assertEqual("a string >'a string' failed(Unsupported Operation)", v.errors[0])
        self.assertFalse(v.val("not a string", "<'a string'"))
        self.assertEqual("not a string <'a string' failed(Unsupported Operation)", v.errors[0])

    def testStringPosition(self):
        v = RebbVal()
        self.assertTrue(v.val("This string", "starts with 'This'"))
        self.assertFalse(v.val("That string", "starts with 'This'"))
        self.assertTrue(v.val("This string", "ends with 'string'"))
        self.assertFalse(v.val("This string", "ends with 'foobar'"))
        self.assertFalse(v.val("This string", "starts with 'This very long string'"))
        self.assertFalse(v.val("This string", "ends with 'a very long string'"))

    def testStringIn(self):
        v = RebbVal()
        self.assertTrue(v.val("string", "in 'a longer string'"))

    def testStringContains(self):
        v = RebbVal()
        self.assertTrue(v.val("a longer string", "contains 'string'"))

    def testStringNotEmpty(self):
        v = RebbVal()
        self.assertTrue(v.val("a string", "not empty"))
        self.assertFalse(v.val("", "not empty"))

    def testStringMaxLength(self):
        v = RebbVal()
        self.assertTrue(v.val("a string", "max length 15"))
        self.assertFalse(v.val("a very looooooooooooooong string", "max length 15"))

    def testStringPercentage(self):
        v = RebbVal()
        self.assertTrue(v.val("100%", "is percentage"))
        self.assertTrue(v.val("99.9%", "is percentage"))
        self.assertFalse(v.val("1000%", "is percentage"))
        self.assertTrue(v.val("-10.01%", "is percentage"))

    def testStringBase64(self):
        v = RebbVal()
        self.assertTrue(v.val("YW55IGNhcm5hbCBwbGVhcw==", "is base64"))
        self.assertTrue(v.val("YW55IGNhcm5hbCBwbGVhc3U=", "is base64"))
        self.assertTrue(v.val("YW55IGNhcm5hbCBwbGVhc3Vy", "is base64"))
        self.assertFalse(v.val("YW5@IGNhcm5hbCBwbGVhcw==", "is base64"))
        self.assertFalse(v.val("YW55IGNhc=5hbCBwbGVhcw==", "is base64"))
        self.assertFalse(v.val("YW55IGNhcm5hbCBwbGVhc3V", "is base64"))
        self.assertFalse(v.val("YW55IGNhcm5hbCBwbGVh=", "is base64"))
        self.assertFalse(v.val("YW55IGNhcm5hbCBwbGVhc===", "is base64"))

    def testStringNumber(self):
        v = RebbVal()
        self.assertTrue(v.val("100", "is number"))
        self.assertTrue(v.val("100.12", "is number"))
        self.assertTrue(v.val("-100", "is number"))
        self.assertTrue(v.val("123.", "is number"))
        self.assertTrue(v.val("-110.123", "is number"))
        self.assertTrue(v.val("3.1415926", "is number"))
        self.assertTrue(v.val("3e30", "is number"))
        self.assertTrue(v.val("-1.2e12", "is number"))
        self.assertTrue(v.val("1.0E-12", "is number"))
        self.assertTrue(v.val(".01", "is number"))
        self.assertFalse(v.val(".0.1", "is number"))
        self.assertFalse(v.val("123abc", "is number"))

    def testStringInt(self):
        v = RebbVal()
        self.assertTrue(v.val("100", "is int"))
        self.assertFalse(v.val("100.12", "is int"))
        self.assertTrue(v.val("-100", "is int"))
        self.assertFalse(v.val("-110.123", "is int"))
        self.assertFalse(v.val("3.1415926", "is int"))
        self.assertFalse(v.val("3e30", "is int"))
        self.assertFalse(v.val(".0.1", "is int"))
        self.assertFalse(v.val("123abc", "is int"))

    def testStringFloat(self):
        v = RebbVal()
        self.assertFalse(v.val("100", "is float"))
        self.assertTrue(v.val("100.12", "is float"))
        self.assertTrue(v.val("111.", "is float"))
        self.assertFalse(v.val("-100", "is float"))
        self.assertTrue(v.val("-110.123", "is float"))
        self.assertTrue(v.val("3.1415926", "is float"))
        self.assertFalse(v.val("3e30", "is float"))
        self.assertFalse(v.val(".0.1", "is float"))
        self.assertFalse(v.val("123abc", "is float"))

    def testHexColor(self):
        v = RebbVal()
        self.assertTrue(v.val("#aaa", "is hex color"))
        self.assertTrue(v.val("#aaab", "is hex color"))
        self.assertTrue(v.val("#000000", "is hex color"))
        self.assertTrue(v.val("#ffffffff", "is hex color"))
        self.assertFalse(v.val("fff", "is hex color"))
        self.assertFalse(v.val("ffff", "is hex color"))
        self.assertFalse(v.val("bcdefg", "is hex color"))

    def testHexNumber(self):
        v = RebbVal()
        self.assertTrue(v.val("0xaaa", "is hex number"))
        self.assertTrue(v.val("0Xaaab", "is hex number"))
        self.assertTrue(v.val("0X000000", "is hex number"))
        self.assertTrue(v.val("0xffffffff", "is hex number"))
        self.assertTrue(v.val("fff", "is hex number"))
        self.assertTrue(v.val("ffff", "is hex number"))
        self.assertFalse(v.val("bcdefg", "is hex number"))

    def testPhone(self):
        v = RebbVal()
        self.assertTrue(v.val("021-59595959", "is phone"))
        self.assertTrue(v.val("0577-1234567", "is phone"))
        self.assertFalse(v.val("01234-123123123", "is phone"))
        self.assertFalse(v.val("58910293", "is phone"))

    def testMobile(self):
        v = RebbVal()
        self.assertTrue(v.val("13800138000", "is mobile"))
        self.assertTrue(v.val("13113113111", "is mobile"))
        self.assertFalse(v.val("12132132123", "is mobile"))
        self.assertFalse(v.val("021-59595959", "is mobile"))

    def testMatch(self):
        v = RebbVal()
        self.assertTrue(v.val("123", "match /^\\d+$/"))
        self.assertFalse(v.val("abc123", "match /^\\d+$/"))
    

if __name__ == '__main__':
    unittest.main()
