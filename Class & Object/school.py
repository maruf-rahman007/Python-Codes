class Student :

    def __init__(self,name,id,cls):
        self.name = name
        self.cls = cls
        self.id = id
    def __repr__(self) -> str:
        return f'Name : {self.name} ID : {self.id} Class : {self.cls}'

class Teacher :
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'Name :  {self.name} ID : {self.id} Class : {self.subject}'

class School :

    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def add_students(self,name,cls):
        id = len(self.students) + 1
        student = Student(name,id,cls)
        self.students.append(student)



phitron = School('Phitron')
phitron.add_students("Maruf Rahman ",2)
phitron.add_students("Rafim Rabby ",1)
phitron.add_students("Sarbajit Paul Bappy ",2)
phitron.add_students("Rabiul Hasan Anim ",2)
 
phitron.add_teacher("Apurba Saha",'Data Stracture')
phitron.add_teacher("Fahad Hossain",'Basic Programming')
phitron.add_teacher("Dipto Saha",'Algorithm')

print(phitron)

