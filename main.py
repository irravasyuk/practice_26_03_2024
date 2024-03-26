# Завдання 1
# class Human:
#     def __init__(self, name, age, gender):
#         self._name = name
#         self._age = age
#         self._gender = gender
#
#     def info(self):
#         return f"Information:\nName:{self._name},\nAge:{self._age},\nGender:{self._gender}"
#
# class Builder(Human):
#     def __init__(self, name, age, gender, specialization):
#         super().__init__(name, age, gender)
#         self._specialization = specialization
#
#     def work(self):
#         return f"I am a builder specializing in {self._specialization}"
#
# class Sailor(Human):
#     def __init__(self, name, age, gender, rank):
#         super().__init__(name, age, gender)
#         self._rank = rank
#
#     def sail(self):
#         return f"I am a {self._rank} sailor"
#
# class Pilot(Human):
#     def __init__(self, name, age, gender, aircraft):
#         super().__init__(name, age, gender)
#         self._aircraft = aircraft
#
#     def fly(self):
#         return f"I am a pilot flying {self._aircraft}"
#
# builder = Builder("Ivan", 28, "male", "civil engineer")
# print(builder.info())
# print(builder.work())
#
# sailor = Sailor("Julia", 26, "female", "Junior Lieutenant")
# print(sailor.info())
# print(sailor.sail())
#
# pilot = Pilot("Nastya", 29, "female", "MIG 29")
# print(pilot.info())
# print(pilot.fly())

# Завдання 2
# class Passport:
#     def __init__(self, name, age, gender, nationality, passport_number):
#         self._name = name
#         self._age = age
#         self._gender = gender
#         self._nationality = nationality
#         self._passport_number = passport_number
#
#     def info(self):
#         return f"Name: {self._name}\nAge: {self._age}\nGender: {self._gender}\nNationality: {self._nationality}\nPassport number: {self._passport_number}"
#
# class ForeignPassport(Passport):
#     def __init__(self, name, age, gender, nationality, passport_number, visa_info, foreign_passport_number):
#         super().__init__(name, age, gender, nationality, passport_number)
#         self._visa_info = visa_info
#         self._foreign_passport_number = foreign_passport_number
#
#     def info(self):
#         passport_info = super().info()
#         return f"{passport_info}\nVisa information: {self._visa_info}\nForeign passport number: {self._foreign_passport_number}"
#
# passport = Passport("Ivan Belous", 35, "male", 'Ukraine', "123232")
# print("Passport Info:")
# print(passport.info())
#
# foreign_passport = ForeignPassport("Will Smith", 23, "male", "USA", "228545", "Valid until 2030", "8872564")
# print("\nPassport info:")
# print(foreign_passport.info())



# Завдання 3
class Animal:
    def __init__(self, name, species, habitat):
        self._name = name
        self._species = species
        self._habitat = habitat

    def eat(self, food):
        return f"{self._species} {self._name} is eating {food}."

    def sound(self):
        return "Animal sound."


class Tiger(Animal):
    def __init__(self, name, habitat, age):
        super().__init__(name, "Tiger", habitat)
        self._age = age

    def sound(self):
        return "Roar!"


class Crocodile(Animal):
    def __init__(self, name, habitat, speed):
        super().__init__(name, "Crocodile", habitat)
        self._speed = speed

    def sound(self):
        return "Grunt!"

    def move(self):
        return f"The crocodile {self._name} is swimming at a speed of {self._speed} km/h."


class Kangaroo(Animal):
    def __init__(self, name, habitat, jump_height):
        super().__init__(name, "Kangaroo", habitat)
        self._jump_height = jump_height

    def sound(self):
        return "Boing!"

    def jump(self):
        return f"The kangaroo {self._name} can jump up to {self._jump_height} meters."

tiger = Tiger("Will", "Jungle", 15)
print(tiger.eat("meat"))
print(tiger.sound())
print(f"Tiger: age - {tiger._age}")

crocodile = Crocodile("Pop", "River", 30)
print(crocodile.eat("fish"))
print(crocodile.sound())
print(crocodile.move())

kangaroo = Kangaroo("Juli", "Grassland", 3)
print(kangaroo.eat("grass"))
print(kangaroo.sound())
print(kangaroo.jump())


