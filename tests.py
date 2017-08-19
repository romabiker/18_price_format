import unittest
from format_price import format_price_for_site


class TestFormatPrice(unittest.TestCase):

    def test_format_price_for_site(self):
        self.assertEqual('1 235', format_price_for_site('1234.9787'))
        self.assertEqual('0', format_price_for_site('0'))
        self.assertEqual('132 746 872', format_price_for_site('132746872'))
        self.assertEqual('12 349 787', format_price_for_site('12349787.'))
        self.assertEqual('8', format_price_for_site('7.5'))
        self.assertEqual('7', format_price_for_site('7.4'))
        self.assertIsNone(format_price_for_site('123.4978.7'))
        self.assertIsNone(format_price_for_site('1234,9787'))
        self.assertIsNone(format_price_for_site('-12349787'))
        self.assertIsNone(format_price_for_site('asfsfsaf'))
        self.assertIsNone(format_price_for_site('-0.1'))


if __name__ == '__main__':
    unittest.main()
