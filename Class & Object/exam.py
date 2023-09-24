class Exam:

    def __init__(self,Name):
        self.Name = Name
        self.Attended_Exam = []
        self.obtained_marks = {}
    
    def attend_exam(self,exam):
        self.Attended_Exam.append(exam)
    def add_marks(self,subject,marks):
        self.obtained_marks[subject] = marks


maruf = Exam("Maruf")
maruf.attend_exam("Engineering Mathematics")
maruf.attend_exam("Data Stracture")
maruf.add_marks("Engineering Mathematics",80)
maruf.add_marks('Data Stracture',90)
print("Student Name :" ,maruf.Name)
print("Attended Exam : ",maruf.Attended_Exam)
print("Obtained Marks : ",maruf.obtained_marks)
