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

# Tests the is_leap_year() method, and whether it correctly identifies leap years.
class LeapYears(unittest.TestCase):
    def test_not_leap_year(self): # Tests date not on a leap year, should return false
        self.date1 = Date(2, 13, 2100)
        self.assertFalse(self.date1.is_leap_year())

    def test_leap_year(self): # Tests leap year date, should return true
        self.date2 = Date(3, 30, 2000)
        self.assertTrue(self.date2.is_leap_year())

# Tests the static method for leap years, year_is_leap().
class StaticLeapYears(unittest.TestCase):
    def test_not_leap_year(self):
        self.assertFalse(Date.year_is_leap(2001))

    def test_leap_year(self):
        self.assertTrue(Date.year_is_leap(2004))

# Tests how well the last_day() method identifies the final day of the month for a date, considering leap years.
class LastDayDate(unittest.TestCase):
    def test_normal(self):
        self.date = Date(3, 1, 2003)
        self.assertEqual(self.date.last_day(), 31)

    def test_special(self):
        self.date = Date(2, 1, 2000)
        self.assertEqual(self.date.last_day(), 29)

# Similar to the test for the instance method, but checks January and February (non-leap).
class LastDayMonth(unittest.TestCase):
    def test_normal(self):
        self.date = Date(1, 1, 2000)
        self.assertEqual(self.date.last_day(), 31)

    def test_special(self):
        self.date = Date(2, 1, 2001)
        self.assertEqual(self.date.last_day(), 28)

# Tests the date 25 December 2021 for if it's properly formatted by to_numeric_string method.
class NumericDateFormat(unittest.TestCase):
    def test_string(self):
        self.date = Date(12, 25, 2021)
        self.assertEqual(self.date.to_numeric_string(), "12/25/2021")

# Tests 25 December 2021 in month-first format, with the month in word form.
class MonthFirstFormat(unittest.TestCase):
    def test_string(self):
        self.date = Date(12, 25, 2021)
        self.assertEqual(self.date.to_month_first_string(), "December 25, 2021")

# Tests 25 December 2021 in day-first format, with the month in word form.
class DayFirstFormat(unittest.TestCase):
    def test_string(self):
        self.date = Date(12, 25, 2021)
        self.assertEqual(self.date.to_day_first_string(), "25 December, 2021")

if __name__ == '__main__':
    unittest.main()
