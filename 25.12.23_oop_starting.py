from datetime import date


class Car:
    def __init__(self, type, model, year, color):
        self.type = type
        self.model = model
        self.year = year
        self.color = color

    def car_age(self):
        current_date = date.today()
        current_year = current_date.year
        return current_year - self.year



mah_car = Car("Hyundai", "Elantra", 2020, "white")
print(mah_car.car_age())