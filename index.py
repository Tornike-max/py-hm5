class MixCl:
    def mix(self):
        res = f"name: {[self.name]}, surname: {[self.surname]},age: {[self.age]}, university: {[self.university]}"
        return res


class Person():
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def result(self):
        print(f"hi i'm {self.name} {self.surname}")

class Student(MixCl,Person):
    def __init__(self,name,surname,age,university):
        super().__init__(name,surname,age)
        self.university = university

    def result(self):
        print(f"Hello, I am a student and I study in {self.university}")

student = Student("Tornike", "Ozbetelashvili", 22, "Skillwill")
student.result()

result = student.mix()
print(result)