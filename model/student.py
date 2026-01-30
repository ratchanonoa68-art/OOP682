from model.person import Person

class Student(Person):
    def __init__(self,name,age,student_id,pid):
        super().__init__(name,age,pid)
        self.student_id = student_id
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, PID: {self.pid}, Student ID: {self.student_id}"
        
