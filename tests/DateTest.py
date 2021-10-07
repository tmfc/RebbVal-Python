import unittest

from rebbval.RebbVal import RebbVal


class DateTest(unittest.TestCase):
    def testDateFunction(self):
        v = RebbVal()
        condition = "between 2020-01-01 and 2021-01-01"
        self.assertTrue(v.val(v.date("2020-05-01"), condition))

        self.assertIsNone(v.date("ABC"))
        self.assertEqual("time data 'ABC' does not match format '%Y-%m-%d'", v.errors[0])

        self.assertFalse(v.val(v.date("ABC"), condition))
        self.assertEqual("object is null(ObjectTypeNotSupported)", v.errors[0])

    def testDateBetween(self):
        v = RebbVal()
        condition = "between 2020-01-01 and 2021-01-01"

        date1 = v.date("2020-05-01")
        date2 = v.date("2021-05-01")
        self.assertTrue(v.val(date1, condition))
        self.assertFalse(v.val(date2, condition))

    def testDateInterval(self):
    
        v = RebbVal()
        condition = "[2020-01-01 .. 2021-01-01]"

        date1 = v.date("2020-05-01")
        date2 = v.date("2021-05-01")
        self.assertTrue(v.val(date1, condition))
        self.assertFalse(v.val(date2, condition))

        date1 = v.date("2020-01-01")
        date2 = v.date("2021-01-01")
        self.assertTrue(v.val(date1, "[2020-01-01 .. 2021-01-01)"))
        self.assertTrue(v.val(date2, "(2020-01-01 .. 2021-01-01]"))
        self.assertFalse(v.val(date1, "(2020-01-01 .. 2021-01-01)"))
        self.assertFalse(v.val(date2, "(2020-01-01 .. 2021-01-01)"))
        
    def testDateCompare(self):
        v = RebbVal()

        date1 = v.date("2020-05-01")

        self.assertTrue(v.val(date1, "=2020-05-01"))
        self.assertFalse(v.val(date1, "=2020-01-01"))

        self.assertTrue(v.val(date1, "!=2020-01-01"))
        self.assertFalse(v.val(date1, "!=2020-05-01"))

        self.assertTrue(v.val(date1, ">2020-01-01"))
        self.assertFalse(v.val(date1, ">2020-06-01"))

        self.assertTrue(v.val(date1, ">=2020-01-01"))
        self.assertTrue(v.val(date1, ">=2020-05-01"))
        self.assertFalse(v.val(date1, ">=2020-06-01"))

        self.assertTrue(v.val(date1, "<2020-06-01"))
        self.assertFalse(v.val(date1, "<2020-01-01"))

        self.assertTrue(v.val(date1, "<=2020-06-01"))
        self.assertTrue(v.val(date1, "<=2020-05-01"))
        self.assertFalse(v.val(date1, "<=2020-01-01"))

    def testLeapYear(self):
        v = RebbVal()
        date = v.date("2020-05-01")
        self.assertTrue(v.val(date, "is leapyear"))
        self.assertFalse(v.val(date, "is leapday"))

        date = v.date("2000-02-29")
        self.assertTrue(v.val(date, "is leapyear"))
        self.assertTrue(v.val(date, "is leapday"))

        date = v.date("1900-02-28")
        self.assertFalse(v.val(date, "is leapyear"))
        self.assertFalse(v.val(date, "is leapday"))

        date = v.date("1999-02-28")
        self.assertFalse(v.val(date, "is leapyear"))
        self.assertFalse(v.val(date, "is leapday"))
        self.assertTrue(v.val(v.year("2000"), "is leapyear"))
        self.assertFalse(v.val(v.year("2001"), "is leapyear"))
    

if __name__ == '__main__':
    unittest.main()
