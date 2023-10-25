import pickle
import os

class Student:
    def __init__(self, studid, studname, studsex, studdob):
        self.studid = studid
        self.studname = studname
        self.studsex = studsex
        self.studdob = studdob

Student1 = Student(1, "Arul", "M", "08/09/1971")
Student2 = Student(2, "Benhur", "M", "31/01/1971")
os.chdir("c:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles")
MyFile = open("Pickle","wb")
# Serialize and deserialize
pickled_data = pickle.dumps(Student1)
MyFile.write(pickled_data)
pickled_data = pickle.dumps(Student2)
MyFile.write(pickled_data)

MyFile.close()

# reconstructed = pickle.loads(pickled_data)
 
# Verify
# print("Data from reconstructed object:", reconstructed.studname)
# print(type(reconstructed))
