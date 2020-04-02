import datetime

class Person:
    def __init__(self, name, year, mounth, day):
        self.year = year
        self.name = name
        self.mounth = mounth
        self.day = day

    def __add__(self, other_obj):
        self.p = Person("Dragan", self.year + other_obj.year)
        print(self.p.name, self.p.year)
        return self.p

    def __sub__(self, other_obj):
        return self.year - other_obj.year
    
    def __mul__(self, other_obj):
        return self.year * other_obj.year
    
    def __radd__(self, year):
        print(year)
        return self.year + year

    def age(self):
        d = datetime.date.today()
        years = d.year - self.year

        if self.mounth < d.month:
            years -= 1

        elif self.mounth == d.month:
            if self.day > d.day:
                print()
                years -= 1

        return years



p1 = Person("Goshko", 2004, 4, 8)
#p2 = Person("Ivan", 14)
#print(p1 + p2)

print(p1.age())
