from functools import singledispatchmethod
from datetime import date, timedelta, datetime


class BirthInfo:

    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register
    def from_data(self, dt: date):
        self.birth_date = dt

    @__init__.register
    def from_str_iso(self, dt: str):
        try:
            self.birth_date = date.fromisoformat(dt)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register
    def from_tp_ls(self, dt: list|tuple):
        if BirthInfo.valid_data(dt):
            y,m,d = dt
            self.birth_date = date(y, m, d)
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        today = date.today()
        years = today.year - self.birth_date.year
        # если день рождения ещё не наступил в этом году — вычитаем 1
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years

    @staticmethod
    def valid_data(data):
        try:

            y, m, d = data
            dt = date(y, m, d)
            return True
        except:
            return False



