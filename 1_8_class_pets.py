class Pet:
    """Базовый класс, который будут наследовать все остальные домашние животные."""
    colour = 'white'
    mass = 3  # kg
    life_expectancy = 0  # months
    food_needed = 0  # kg
    space_needed = 1  # square meter
    spead = 1  # 100m per hour

    def __init__(self, number):
        """Чтобы у каждого животного был номер."""
        self.number = number
        self.additional_colors = []


class Cattle(Pet):
    mass = 47
    food_needed = 2
    life_expectancy = 6
    space_needed = 3

    def running_spead(self, value=10):
        return self.spead * value


class Cow(Cattle):
    mass = 500
    food_needed = 4
    life_expectancy = 9
    space_needed = 6

    def running_spead(self, value=10):
        return self.spead * value * 4


class Goat(Cattle):
    def running_spead(self, value=10):
        return self.spead * value * 2


class Sheep(Cattle):
    life_expectancy = 60


class Pig(Cattle):
    mass = 100

    def running_spead(self, value=10):
        return self.spead * value * 2


class Poultry(Pet):
    food_needed = 0.1
    space_needed = 0.3
    life_expectancy = 4


class Duck(Poultry):
    mass = 6
    life_expectancy = 6


class Chicken(Poultry):
    pass


class Goose(Poultry):
    mass = 8
    life_expectancy = 8


print(Goose.__dict__)
chicken_1 = Chicken(1)
print(chicken_1)
print(chicken_1.food_needed)
goat_01 = Goat(3)
print(goat_01.running_spead)
cattle_01 = Cattle(1)
print(cattle_01.running_spead(20))
goat_01.additional_colors.append("green")
print(goat_01.__dict__)
