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