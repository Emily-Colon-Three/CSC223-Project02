from datetime import date
import calendar

class Date:
    def __init__(self, month: int = 1, day: int = 1, year: int = 1900) -> None:
        self.month = month
        self.day = day
        self.year = year