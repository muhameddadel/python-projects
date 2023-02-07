# -- instance (self)
# -- class attribute -> without (self)
# -- class method -> @classmethod -> (cls)
# -- static method -> @staticmethod
# -- 1) Inhertance -> multpile inhertance
# -- 2) Encapsulation -> praivate(__), protect(_)
# -- 3) Abstraction -> abc  , ABC , @abstractmethod
# -- 4) Polymorphism 
# -- Dunder function  -> __str__ , __int__

from datetime import date
from abc import ABC, abstractmethod
class Student:
    # class attribute
    num_of_students = 0
    # instance attribute
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age
        Student.num_of_students += 1
    
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def info(self):
        print(f"My name is {self.__name } and my age is {self.__age}")
    
    @classmethod
    def init_from_birth_year(cls, name ,birth_year):
        return cls(name, date.today().year - birth_year)

student_one = Student.init_from_birth_year('mohamed', 2000)

student_one.info()

print("###########################################")

class Person: 
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
    
    def display(self):
        return f"Name is {self.name} and age is {self.age}"


class Man(Person):
    gender = 'Male'
    num_of_men = 0

    def __init__(self, name, age, voice) -> None:
        super().__init__(name, age)
        self.voice = voice
        Man.num_of_men += 1

    def display(self):
        string = super().display()
        return string + f" and voice is {self.voice} and gender is {Man.gender}"

class Woman(Person):
    gender = 'Female'
    num_of_women = 0

    def __init__(self, name, age, voice) -> None:
        super().__init__(name, age)
        self.voice = voice
        Woman.num_of_women += 1

    def display(self):
        string = super().display()
        return string + f" and voice is {self.voice} and gender is {Woman.gender}"


man = Man('Muhamed', 23, 'hard')
print(man.display())
print(Man.num_of_men)

woman = Woman('Sara', 23, 'soft')
print(woman.display())
print(Woman.num_of_women)


print("###########################################")

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimter(self):
        pass

class Sqaure(Shape):
    def __init__(self, side) -> None:
        self.__side = side

    def area(self):
        return self.__side * self.__side
    
    def perimter(self):
        return self.__side * 4

class Rect(Shape):
    def __init__(self, hight, width) -> None:
        self.__hight = hight
        self.__width = width

    def area(self):
        return self.__hight * self.__width
    
    def perimter(self):
        return (self.__hight + self.__width) * 2

sqaure = Sqaure(10)
print(f"Squre area is {sqaure.area()} and perimter is {sqaure.perimter()}")
rect = Rect(6, 5)
print(f"Rectangle area is {rect.area()} and perimter is {rect.perimter()}")
