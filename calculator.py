import os
from datetime import timedelta

SECONDS_IN_HOUR = 3600


class DollarPerHourCalculator:

    def __init__(self, hours, minutes, seconds, hourly_rate):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)
        self.hourly_rate = float(hourly_rate)

    @property
    def total_time(self) -> timedelta:
        return timedelta(hours=self.hours, minutes=self.minutes, seconds=self.seconds)

    @property
    def amount_earned(self) -> float:
        return self.calculate()

    def calculate(self) -> float:
        dollars_per_second = self.hourly_rate / SECONDS_IN_HOUR
        amount_earned = round(self.total_time.seconds * dollars_per_second, 2)
        return amount_earned

    @classmethod
    def from_input(cls, hourly_rate: float = None):
        hours = int_or_zero(input('Hours: '))
        minutes = int_or_zero(input('Minutes: '))
        seconds = int_or_zero(input('Seconds: '))
        hourly_rate = hourly_rate if hourly_rate else float_or_zero(input('Hourly Rate: $'))
        return cls(hours, minutes, seconds, hourly_rate)


    @classmethod
    def run(cls, hourly_rate: float = None):
        """ Convenience method for primary use of the calculator. 
        Displays the full cli (header, input, & results) to the console window. 
        """

        cls._print_header()
        instance = cls.from_input(hourly_rate=hourly_rate)
        print('\n' + instance._amount_earned_formatted)
        os.system('pause')

    @staticmethod
    def _print_header():
        print('Dollar per Hour Calculator'
              '\n'
              '\n'
              '_____________Time Worked______________')

    @property
    def _amount_earned_formatted(self) -> str:
        return f'Amount Earned: ${self.amount_earned:.2f}'


def int_or_zero(text: str):
    """
    Determines whether the item passed can be turned into an integer, and if not
    return zero. Used for handling int() error with empty strings.
    """

    return int(text) if text.isdecimal() else 0


def float_or_zero(text: str):
    """
    Determines whether the string passed can be turned into an float, and if not
    return zero. Used for handling int() error with empty strings.
    """

    try:
        return float(text)
    except:
        return 0.0


if __name__ == '__main__':
    DollarPerHourCalculator.run()
