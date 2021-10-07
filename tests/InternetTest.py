import unittest

from rebbval.RebbVal import RebbVal


class InternetTest(unittest.TestCase):
    def testDomain(self):
        v = RebbVal()
        self.assertTrue(v.val("google.com", "is domain"))
        self.assertTrue(v.val("www.baidu.com", "is domain"))
        self.assertFalse(v.val("", "is domain"))

    def testEmail(self):
        v = RebbVal()
        self.assertTrue(v.val("abc@gmail.com", "is email"))
        self.assertTrue(v.val("13800138000@139.com", "is email"))
        self.assertFalse(v.val("fdsads", "is email"))

    def testIpv4(self):
        v = RebbVal()
        self.assertTrue(v.val("8.8.8.8", "is ipv4"))
        self.assertTrue(v.val("192.168.1.1", "is ipv4"))
        self.assertFalse(v.val("266.1.3.4", "is ipv4"))

    def testIpv6(self):
        v = RebbVal()
        self.assertTrue(v.val("::", "is ipv6"))
        self.assertTrue(v.val("::123", "is ipv6"))
        self.assertTrue(v.val("::123:456", "is ipv6"))
        self.assertTrue(v.val("::123:456:789", "is ipv6"))
        self.assertTrue(v.val("::123:456:789:abc:def:6666", "is ipv6"))
        self.assertFalse(v.val("::123:456:789:abc:def:6666:7", "is ipv6"))

        self.assertTrue(v.val("123::456", "is ipv6"))
        self.assertTrue(v.val("123::456:789:abc", "is ipv6"))
        self.assertTrue(v.val("123::456:789:abc:def:6", "is ipv6"))
        self.assertFalse(v.val("123::456:789:abc:def:6:7", "is ipv6"))

        self.assertTrue(v.val("123:456::789", "is ipv6"))
        self.assertTrue(v.val("123:456::789:abc:def", "is ipv6"))
        self.assertTrue(v.val("123:456::789:abc:def:6666", "is ipv6"))
        self.assertFalse(v.val("123:456::789:abc:def:6666:7", "is ipv6"))

        self.assertTrue(v.val("123:456:789::abc", "is ipv6"))
        self.assertTrue(v.val("123:456:789::abc:def", "is ipv6"))
        self.assertTrue(v.val("123:456:789::abc:def:6666", "is ipv6"))
        self.assertFalse(v.val("123:456:789::abc:def:6666:7", "is ipv6"))

        self.assertTrue(v.val("123:456:789:abc::def", "is ipv6"))
        self.assertTrue(v.val("123:456:789:abc::def:6666", "is ipv6"))
        self.assertFalse(v.val("123:456:789:abc::def:6666:7", "is ipv6"))

        self.assertTrue(v.val("123:456:789:abc:def::6666", "is ipv6"))
        self.assertFalse(v.val("123:456:789:abc:def::6666:7", "is ipv6"))

        self.assertTrue(v.val("123:456:789:abc:def:6666::", "is ipv6"))
        self.assertTrue(v.val("123:456:789:abc:def::", "is ipv6"))
        self.assertTrue(v.val("123:456:789:abc::", "is ipv6"))
        self.assertTrue(v.val("123:456:789::", "is ipv6"))
        self.assertTrue(v.val("123:456::", "is ipv6"))
        self.assertTrue(v.val("123::", "is ipv6"))

        self.assertTrue(v.val("123::456:789:abc:def:6666", "is ipv6"))
        self.assertFalse(v.val("123:456:789:abc:def:6666:7", "is ipv6"))
        self.assertFalse(v.val("123::456::abc", "is ipv6"))

        self.assertTrue(v.val("2001:0db8:85a3:08d3:1319:8a2e:0370:7334", "is ipv6"))

    def testPrivateIp(self):
        v = RebbVal()
        self.assertTrue(v.val("127.0.0.1", "is private_ip"))
        self.assertTrue(v.val("10.1.1.1", "is private_ip"))
        self.assertTrue(v.val("172.18.100.1", "is private_ip"))
        self.assertTrue(v.val("192.168.2.100", "is private_ip"))
        self.assertFalse(v.val("8.8.8.8", "is private_ip"))
        self.assertTrue(v.val("FEC0:0001::", "is private_ip"))
        self.assertFalse(v.val("123:456:789:abc:def:6666::", "is private_ip"))

    def testUrl(self):
        v = RebbVal()
        self.assertTrue(v.val("https://www.google.com", "is url"))
        self.assertTrue(v.val("http://www.example.com/to/path?param1=foo&param2=bar", "is url"))
        self.assertFalse(v.val("somebody@somedomain.com", "is url"))


if __name__ == '__main__':
    unittest.main()
