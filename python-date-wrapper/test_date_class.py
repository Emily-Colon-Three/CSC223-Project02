import unittest
from date_class import Date

# Tests if default Date constructor functions properly
class DateConstructorTest(unittest.TestCase):
    def setUp(self): # Creates the Default Date to be tested
        self.date = Date()

    def test_day(self):
        self.assertEqual(self.date.day, 1)

    def test_month(self):
        self.assertEqual(self.date.month, 1)

    def test_year(self):
        self.assertEqual(self.date.year, 1900)

# Creates a valid Date object, then tests that the right values have been used
class ValidDateConstructorTest(unittest.TestCase):
    def setUp(self):
        self.date = Date(9, 15, 2026) # Date is 9/15/2026

    def test_day(self):
        self.assertEqual(self.date.day, 15)

    def test_month(self):
        self.assertEqual(self.date.month, 9)

    def test_year(self):
        self.assertEqual(self.date.year, 2026)

class InvalidMonth(unittest.TestCase):
    def test_ValueError(self):
        with self.assertRaises(ValueError):
            self.date = Date(0, 2, 2009)

class InvalidDay(unittest.TestCase):
    def test_ValueError(self):
        with self.assertRaises(ValueError):
            self.date = Date(3, 32, 2000)

class InvalidLeapDay(unittest.TestCase):
    def test_ValueError(self):
        with self.assertRaises(ValueError):
            self.date = Date(2, 29, 2100)

class ReadOnlyProperty(unittest.TestCase):
    def test_AttributeError(self):
        with self.assertRaises(AttributeError):
            self.date = Date()
            self.date.day = 15

# Creates a Date object, before using set_date() method to change it, and verifying it worked properly.
class ValidSetDate(unittest.TestCase):
    def setUp(self):
        self.date = Date()
        self.date.set_date(9, 17, 2026)

    def test_day(self):
        self.assertEqual(self.date.day, 17)

    def test_month(self):
        self.assertEqual(self.date.month, 9)

    def test_year(self):
        self.assertEqual(self.date.year, 2026)

# Creates default Date object, then sets it to a non-existent date to test if ValueError is raised.
class InvalidSetDate(unittest.TestCase):
    def test_ValueError(self):
        with self.assertRaises(ValueError):
            self.date = Date()
            self.date.set_date(3, 0, 2001)

# Tries to change default date to invalid one, then tests to see if date remains unchanged.
class DateAfterInvalidSetDate(unittest.TestCase):
    def setUp(self):
        self.date = Date()
        with self.assertRaises(ValueError):
            self.date.set_date(0, 0, 0)

    def test_day(self):
        self.assertEqual(self.date.day, 1)

    def test_month(self):
        self.assertEqual(self.date.month, 1)

    def test_year(self):
        self.assertEqual(self.date.year, 1900)

if __name__ == '__main__':
    unittest.main()
