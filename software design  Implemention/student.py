from person import Perosn
from enroll import Enroll

class Student(Perosn):
    def __init__(self, first, last, dob, phone, address, international = False) -> None:
        super().__init__(first, last, dob, phone, address)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise ValueError("Invalid Enroll!")
        
        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False

    def is_part_time(self):
        return len(self.enrolled) <= 3