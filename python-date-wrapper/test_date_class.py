import unittest
from date_class import Date

class DateConstructorTest(unittest.TestCase):
    def setUp(self):
        self.date = Date()

    def test_day(self):
        self.assertEqual(self.date.day, 1)

    def test_month(self):
        self.assertEqual(self.date.month, 1)

    def test_year(self):
        self.assertEqual(self.date.year, 1900)

if __name__ == '__main__':
    unittest.main()
