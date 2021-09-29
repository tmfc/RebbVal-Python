import unittest

from rebbval.RebbVal import RebbVal


class ErrorListenerTest(unittest.TestCase):
    def test_error(self):
        v = RebbVal()

        date1 = v.date('2019-05-01')

        self.assertFalse(v.val(date1, "older than a_string"))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("line 1:11 mismatched input 'a' expecting {'not', '(', 'between', 'in', 'contains', 'max', 'is', 'match', 'starts', 'ends', ']', '[', StringLiteral, NumbericLiteral, DateLiteral, TimeLiteral, '=', '!=', '<', '<=', '>', '>=', 'older', 'younger'}", v.errors[0])

        self.assertFalse(v.val(date1, "older than another_string"))
        self.assertEqual(1, len(v.errors))
        self.assertEqual("line 1:11 mismatched input 'another' expecting {'not', '(', 'between', 'in', 'contains', 'max', 'is', 'match', 'starts', 'ends', ']', '[', StringLiteral, NumbericLiteral, DateLiteral, TimeLiteral, '=', '!=', '<', '<=', '>', '>=', 'older', 'younger'}", v.errors[0])


if __name__ == '__main__':
    unittest.main()
