from datetime import date, datetime
import calendar

class Date:
    # The Date class is a wrapper around the datetime.date object.
    # It raises the "ValueError" exception when an invalid day, month, or year is used for the date.

    # Constructor for Date object with default values in case input not given
    def __init__(self, month: int = 1, day: int = 1, year: int = 1900) -> None:
        self.date = date(year, month, day)

    # Read-only access
    @property
    def month(self) -> int:
        return self.date.month

    @property
    def day(self) -> int:
        return self.date.day

    @property
    def year(self) -> int:
        return self.date.year

    # A valid and controlled way to change the date held in a Date object
    def set_date(self, month: int, day: int, year: int) -> None:
        self.date = date(year, month, day)

    # Method that will determine whether a given date falls on a leap year, returns boolean
    # To be leap year, the year must be divisible by 4, but not 100, unless divisible by 400.
    def is_leap_year(self) -> bool:
        return self.date.year % 4 == 0 and (self.date.year % 100 != 0 or self.date.year % 400 == 0)

    # Same as is_leap_year, but uses a year from input and is a static method.
    @staticmethod
    def year_is_leap(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # Returns the final day of whatever month is in the date of the Date object. Accounts for leap year on February.
    def last_day(self) -> int:
        return calendar.monthrange(self.date.year, self.date.month)[1]

    # Uses instance last_day() method to find the last day of a month on a given year
    @staticmethod
    def last_day_of_month(year: int, month: int) -> int:
        ex = Date(1, month, year) # Sets day to 1, not relevant
        return ex.last_day()

    # Returns string of the date in M/D/Y format
    def to_numeric_string(self) -> str:
        return self.date.strftime("%m/%d/%Y")

    # Returns string of the date in "M, D Y" format.
    def to_month_first_string(self) -> str:
        return self.date.strftime("%B %d, %Y")

    # Returns string of the date in "D M, Y" format.
    def to_day_first_string(self) -> str:
        return self.date.strftime("%d %B, %Y")