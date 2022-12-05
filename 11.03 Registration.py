class Student():
    def __init__(self, firstname, lastname, tnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.courselist = []


class StudentList():
    def __init__(self):
        self.studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.studentlist.append(student)

    def find_student(self, studenttofind):
        for i in range(len(self.studentlist)):
            if (self.studentlist[i].tnumber == studenttofind):
                return i
        return -1

    def print_student_list(self):
        print("{:<15}{:<15}{:<15}{:<15}{:<51}{:<15}{:<15}".format("First Name", "Last Name", "T-Number", "Course", "Name", "Room", "Meeting Times"))
        for student in self.studentlist:
            print("{:<15}{:<15}{:<15}".format(
                student.firstname, student.lastname, student.tnumber))
            for course in student.courselist:
                print("{:<45}{:<15}{:<50}{:<15}{:<15}".format(
                    ' ', course.department + ' ' + course.number, course.name, course.room, course.meetingtimes))

    def add_student_from_file(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()

        for line in lines:
            line = line.strip().split(',')
            self.add_student(line[0], line[1], line[2])
        file.close()


class Course():
    def __init__(self, department, number, name, room, meetingtimes):
        self.department = department
        self.number = number
        self.name = name
        self.room = room
        self.meetingtimes = meetingtimes


class CourseList():
    def __init__(self):
        self.courselist = []

    def add_course(self, department, number, name, room, meetingtimes):
        course = Course(department, number, name, room, meetingtimes)
        self.courselist.append(course)

    def find_course(self, departmenttofind, numbertofind):
        for i in range(len(self.courselist)):
            if (self.courselist[i].department == departmenttofind and self.courselist[i].number == numbertofind):
                return i
        return -1

    def add_course_from_file(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()

        for line in lines:
            line = line.strip().split(',')
            self.add_course(line[0], line[1], line[2], line[3], line[4])
        file.close()


def main():
    courselist = CourseList()
    courselist.add_course_from_file("11.03 Courses.txt")

    studentlist = StudentList()
    studentlist.add_student_from_file("11.03 Students.txt")

    file = open("11.03 Registration.txt", 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip().split(',')
        
        tnumber = line[0]
        department = line[1]
        number = line[2]

        courseIndex = courselist.find_course(department, number)
        tCourse = courselist.courselist[courseIndex]
        course = Course(department, number, tCourse.name, tCourse.room, tCourse.meetingtimes)

        studentIndex = studentlist.find_student(tnumber)
        studentlist.studentlist[studentIndex].courselist.append(course)
    file.close()

    studentlist.print_student_list()
main()