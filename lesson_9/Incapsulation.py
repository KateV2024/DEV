class Student:
    __country = "Belarus"

    def __bank_account(self):
        print ("Мы не можем предоставить личную информацию")

    def country_of_birth(self):
        print("Наш студент родом из ", Student.__country)
pupil = Student()
pupil.country_of_birth()
pupil.__bank_account()
