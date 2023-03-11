from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self, name, code, maxi, mini, professor) -> None:
        self.name = name
        self.code = code 
        self.maxi = maxi
        self.mini = mini
        self.professors = []
        self.enorllments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise ValueError('Invalid Professor!')
            
            self.professors = professor
        else:
            raise ValueError('Invalid Professor!')
        

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise ValueError('Invalid professor!')
        
        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise ValueError('Invalid Enroll!')
        
        if len(self.enorllments) == self.maxi:
            raise ValueError('You can not enroll, course is full..')
        
        self.enorllments.append(enroll)


    def is_cancelled(self):
        return len(self.enorllments) < self.mini