studentList = []


def addStudent(name, surname):
    studentName = name+" "+surname
    studentList.append(studentName)
    print(studentName + " student added to database")


def addMultipleStudent(students):
    for student in students:
        # dict
        for name in student:
            studentName = name+" "+student[name]
            studentList.append(studentName)
            print(studentName + " students added to database")


def removeStudent(name, surname):
    studentName = name+" "+surname
    studentList.remove(studentName)
    print(studentName + " student removed from database")


def removeMultipleStudent(students):
    for rmStudent in students:
        for name in rmStudent:
            studentName = name+" "+rmStudent[name]
            if studentName in studentList:
                studentList.remove(studentName)
                print(studentName + " students removed from database")


def getStudents():
    print("-"*8+" "+"All student of database"+" "+"-"*8)
    i = 0
    while(len(studentList) > i):
        print(studentList[i])
        i += 1


def getStudentNumber(name, surname):
    studentName = name+" "+surname
    if studentName in studentList:
        print("Student number of " + studentName+" : " +
              str(studentList.index(studentName)))
    else:
        print("Stundet not found")


# Print operations
addStudent("Murat", "Cinar")
addMultipleStudent([{"Murat": "110"}, {"Fatih": "220"}])
getStudents()
getStudentNumber("Murat", "110")
removeStudent("Murat", "Cinar")
removeMultipleStudent([{"Murat": "110"}, {"Fatih": "220"}])
getStudents()