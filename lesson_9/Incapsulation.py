class Student:
    def __init__(self, name, grade):
        self._name = name
        self.__grade = grade

    @property
    def grade(self):
        return (f"received {self.__grade}")


student = Student("Alice", "85")
print(student._name, student.grade)  # Output: 85
student._name = "Kate"
student.__grade = "78"
print(student._name, student.grade)