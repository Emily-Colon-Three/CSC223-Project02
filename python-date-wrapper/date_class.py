from datetime import date, timedelta
import calendar

class Date:
    """The Date class is a wrapper class for the datetime.date object.
    It contains a constructor which allows a valid date to be stored within a Date object, with
    ValueError raised for invalid dates and a default date of January 1st, 1900.
    There are three getter methods, which are classified as properties of a Date object. No
    setters for date, month, or year individually are available, and the date may only be set with
    method set_date().
    Additionally, there are both instance and static methods for determining whether a date is on
    a leap year and for retrieving the final day of the month of a date, named is_leap_year() and
    last_day() for the instance versions and year_is_leap() and last_day_of_month() for static.
    Date object has three methods for returning a string representation of the date in various
    formats, to_numeric_string(), to_month_first_string(), and to_day_first_string().
    Dates can be subtracted from one another with the __sub__() dunder method. If the first date is
    earlier than the second, a negative value will be returned. Output is in days, an integer.
    Date features increment() method which updates the date to be one day later. Returns itself.
    Similarly, decrement() method returns itself with a date one day earlier than before."""

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

    # Dunder method for Date Subtraction; returns number of days other date is earlier than self. Makes Date class compatible with - operand.
    def __sub__(self, other: Date) -> int:
        return (self.date - other.date).days

    # Method which changes date object within Date to be one day later using timedelta. Returns self.
    def increment(self) -> Date:
        self.date += timedelta(days = 1)
        return self

    # Method which changes date of Date object, decrementing it to one day earlier with timedelta. Returns itself as Date object.
    def decrement(self) -> Date:
        self.date -= timedelta(days = 1)
        return self