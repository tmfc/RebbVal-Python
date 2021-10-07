import unittest

from rebbval.RebbVal import RebbVal


class IdentificationTest(unittest.TestCase):
    def test_imei(self):
        v = RebbVal()
        self.assertTrue(v.val("35-209900-176148-1", "is IMEI"))
        self.assertTrue(v.val("352099001761481", "is IMEI"))
        self.assertFalse(v.val("35-209900-176148-2", "is IMEI"))

    def test_imeisv(self):
        v = RebbVal()
        self.assertTrue(v.val("35-209900-176148-12", "is IMEISV"))
        self.assertTrue(v.val("3520990017614812", "is IMEISV"))
        self.assertFalse(v.val("35-209900-176148-2", "is IMEISV"))

    def test_isbn(self):
        v = RebbVal()
        self.assertTrue(v.val("978-0-596-52068-7", "is ISBN"))
        self.assertTrue(v.val("9787510892844", "is ISBN"))
        self.assertFalse(v.val("35-209900-176148-2", "is ISBN"))

    def test_uuid(self):
        v = RebbVal()
        self.assertTrue(v.val("eb3115e5-bd16-4939-ab12-2b95745a30f3", "is UUID"))
        self.assertFalse(v.val("13113113111", "is UUID"))

    def test_mac(self):
        v = RebbVal()
        self.assertTrue(v.val("00:11:22:33:44:55", "is MAC"))
        self.assertTrue(v.val("00-11-22-33-44-55", "is MAC"))
        self.assertFalse(v.val("00:11:22:33:44:GG", "is MAC"))

    def test_id(self):
        v = RebbVal()
        self.assertTrue(v.val("140303192005236131", "is ID"))
        self.assertFalse(v.val("110100199909093245", "is ID"))
        self.assertFalse(v.val("110100199902313244", "is ID"))
    

if __name__ == '__main__':
    unittest.main()
