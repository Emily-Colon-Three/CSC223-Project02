import builtins
import unittest
from date_class import Date
from unittest.mock import patch

### Part 1 Testing

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


### Part 2 Testing

# Uses the subtraction dunder method to find a positive difference between a later and earlier date
class DateSubtractionPositiveDays(unittest.TestCase):
    def setUp(self):
        self.date1 = Date(9, 21, 2026)
        self.date2 = Date(9, 17, 2026)

    def test_difference(self):
        difference = self.date1 - self.date2
        self.assertEqual(difference, 4)

# Uses subtraction dunder method to find a negative difference, subtracting a later date from an earlier one.
class DateSubtractionNegativeDays(unittest.TestCase):
    def setUp(self):
        self.date1 = Date(9, 17, 2026)
        self.date2 = Date(9, 21, 2026)

    def test_difference(self):
        difference = self.date1 - self.date2
        self.assertEqual(difference, -4)

# Subtracts two dates which are exactly the same, with an intended result of 0 days difference
class DateSubtractionEqual(unittest.TestCase):
    def setUp(self):
        self.date1 = Date()
        self.date2 = Date()

    def test_difference(self):
        difference = self.date1 - self.date2
        self.assertEqual(difference, 0)

# Subtracts a date from the previous year from the current date, different by one day and one year.
class DateSubtractionAcrossYears(unittest.TestCase):
    def setUp(self):
        self.date1 = Date(9, 21, 2026)
        self.date2 = Date(9, 20, 2025)

    def test_difference(self):
        difference = self.date1 - self.date2
        self.assertEqual(difference, 366)

# Tries to add two dates together, an unsupported feature and unimplemented operand with Date.
class UnsupportedOperand(unittest.TestCase):
    def setUp(self):
        self.date1 = Date(8, 1, 2000)
        self.date2 = Date(1, 20, 26)

    def test_addition(self):
        with self.assertRaises(TypeError):
            sum = self.date1 + self.date2

# Uses increment() method to bring a date forward by one day
class DateIncrement(unittest.TestCase):
    def test_increment(self):
        self.date = Date(3, 31, 2025)
        self.date.increment()
        self.assertEqual(self.date.to_numeric_string(), "04/01/2025")

# Increments a date from February 29, a date only possible on leap years, to the next month.
class LeapYearIncrement(unittest.TestCase):
    def test_increment(self):
        self.date = Date(2, 29, 2024)
        self.date.increment()
        self.assertEqual(self.date.to_numeric_string(), "03/01/2024")

# Increments a date over to the next year, from December 31 to January 1.
class NewYearIncrement(unittest.TestCase):
    def test_increment(self):
        self.date = Date(12, 31, 2026)
        self.date.increment()
        self.assertEqual(self.date.to_numeric_string(), "01/01/2027")

# Tests that increment() method returns itself; in this context, self.date
class IncrementReturnsSelf(unittest.TestCase):
    def test_increment(self):
        self.date = Date(9, 21, 2026)
        self.assertEqual(self.date.increment(), self.date)

# Tests the decrement() method, rolling a date over to the previous month.
class DateDecrement(unittest.TestCase):
    def test_decrement(self):
        self.date = Date(4, 1, 2000)
        self.date.decrement()
        self.assertEqual(self.date.to_numeric_string(), "03/31/2000")

# Decrements date to the last day of February on a leap year, which is meant to yield the 29th.
class LeapYearDecrement(unittest.TestCase):
    def test_decrement(self):
        self.date = Date(3, 1, 2024)
        self.date.decrement()
        self.assertEqual(self.date.to_numeric_string(), "02/29/2024")

# Rolls back date to the final day of the previous year with decrement()
class LastYearDecrement(unittest.TestCase):
    def test_decrement(self):
        self.date = Date(1, 1, 2000)
        self.date.decrement()
        self.assertEqual(self.date.to_numeric_string(), "12/31/1999")

# Checks that the return value of increment() is equal to itself, in this case self.date
class DecrementReturnsSelf(unittest.TestCase):
    def test_increment(self):
        self.date = Date(9, 21, 2026)
        self.assertEqual(self.date.increment(), self.date)

# Takes a particular date and tests str() to make sure it is equal to month-first format of the date.
class CustomStringOutput(unittest.TestCase):
    def test_string_output(self):
        self.date = Date(4, 18, 2018)
        self.assertEqual(str(self.date), "April 18, 2018")

# Creates mock input for a date, using it to test from_input() method and Date custom input. Test ensures a new and proper Date object is created according to input.
class CustomInput(unittest.TestCase):
    @patch("builtins.input", side_effect=["4", "18", "2018"])
    def test_from_input_creates_date(self, mock_input):
        result = Date.from_input()
        self.assertEqual(result.month, 4)
        self.assertEqual(result.day, 18)
        self.assertEqual(result.year, 2018)

# Puts string, non-numeric input into custom Date input to ensure that ValueError is thrown.
class NonNumberInput(unittest.TestCase):
    @patch("builtins.input", side_effect=["April", "Eighteenth", "Twenty-eighteen"])
    def test_from_input_non_number(self, mock_input):
        with self.assertRaises(ValueError):
            result = Date.from_input()

# Inputs non-existent date via mock input with from_input() to test if ValueError is thrown.
class InvalidDateInput(unittest.TestCase):
    @patch("builtins.input", side_effect=["2", "29", "2026"])
    def test_from_input_invalid_date(self, mock_input):
        with self.assertRaises(ValueError):
            result = Date.from_input()

if __name__ == '__main__':
    unittest.main()
