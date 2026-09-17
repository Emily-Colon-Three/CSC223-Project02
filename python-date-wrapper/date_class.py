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