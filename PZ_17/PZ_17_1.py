class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    #високосный или не високосный год
    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return ("Високосный")
        else:
            return ("Не високосный")

    #сколько дней в месяце
    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month == 2:
            if self.is_leap_year():
                return 29
            else:
                return 28
        else:
            return 30

    #день недели
    def day_of_week(self):
        t = (self.year - (14 - self.month)//12) // 100
        y = self.year - t * 100
        m = self.month + 12 * ((14 - self.month) // 12) - 2
        d = (self.day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12) % 7
        return d

y = 10
m = 18
d = 20
c = Calendar(y, m, d)
days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
print(days[c.day_of_week()])
print(c.days_in_month())
print(c.is_leap_year())
