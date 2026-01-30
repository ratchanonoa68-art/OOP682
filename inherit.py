from model.student import Student
from model.staff import Staff
from model.person import Person
        
def main():
    student1 = Student("Alice",20,"S12345")
    print(f"Student Name: {student1.name}, Age: {student1.age}, Student ID: {student1.student_id}")
    
    staff1 = Staff("P67890","Bob",35,"ST54321")
    print(f"Staff Name: {staff1.name}, Age: {staff1.age}, PID: {staff1.pid}, Staff ID: {staff1.staff_id}")
    
main()

