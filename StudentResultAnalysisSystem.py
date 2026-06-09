"""
1. Student Result Analysis System (Beginner)

Concept:

Store marks of students in a NumPy array.
Calculate:
Total marks
Average marks
Highest and lowest score
Subject-wise average
Rank students
"""
import numpy as np

class Students:
    subjects = ["Hindi","English","Maths","Science","Computer"]
    def __init__(self):
        self.marks = []
        self.name = []
        nos = int(input("Enter no. of students: "))
        for i in range(nos):
            print()
            self.name.append(input(f"Enter Student{i+1} name: "))
            print("Enter marks-")
            new_marks = []
            for sub in self.subjects:
                new_marks.append(int(input(f"{sub}: ")))
            self.marks.append(new_marks)
        self.marks = np.array(self.marks)
        self.calculate()

    def calculate(self):
        self.total = np.sum(self.marks,axis=1)
        self.avg = np.mean(self.marks,axis=1)
        self.High = np.max(self.marks,axis=1)
        self.low = np.min(self.marks,axis=1)
        self.sub_avg = np.mean(self.marks,axis=0)
        self.rank_inx = np.argsort(-self.total)
        self.rank = np.empty_like(self.rank_inx)
        self.rank[self.rank_inx] = np.arange(1,len(self.rank)+1)
        self.display()

    def display(self):
        print()
        print("Student"," "*(9-len("Student")),end="")
        for sub in self.subjects:
            print(sub," "*(12-len(sub)),end="")
        print("Total"," "*(11-len("Total")),"Average"," "*(11-len("Average")),"Hscore"," "*(9-len("Hscore")),"Lscore"," "*(10-len("Lscore")),"Rank")
        i=0
        for name in self.name:
            print(name," "*(12-len(sub)),end="")
            for sub_marks in self.marks[i]:
                print(sub_marks," "*(12-len(str(sub_marks))),end="")
            print(self.total[i]," "*(12-len(str(self.total[i]))),end="")
            print(self.avg[i]," "*(12-len(str(self.avg[i]))),end="")
            print(self.High[i]," "*(12-len(str(self.avg[i]))),end="")
            print(self.low[i]," "*(12-len(str(self.low[i]))),end="")
            print(self.rank[i]," "*(12-len(str(self.rank[i]))))
            i+=1
            
if __name__=="__main__":
    student = Students()