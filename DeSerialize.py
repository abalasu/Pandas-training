import pickle
import os
import pandas as pd

class Student:
    def __init__(self, studid, studname, studsex, studdob):
        self.studid = studid
        self.studname = studname
        self.studsex = studsex
        self.studdob = studdob

os.chdir("c:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles")
MyFile = open("Pickle","rb")

Flag = True
while Flag:
    try:
        Student_Det = pickle.load(MyFile)
        print(Student_Det.studid, Student_Det.studname, Student_Det.studsex, Student_Det.studdob)
    except:
        print("Last Record")
        Flag = False
    finally:
        MyFile.close