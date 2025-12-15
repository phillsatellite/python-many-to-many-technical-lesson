class Student:
    all =[]
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Student.all.append(self)
    
    def courses(self):
        return [schedule.course for schedule in Schedule.all if 
                schedule.studemt == self]
    """
    We have added a course method in Student. 
    This method will loop through all of the schedules and find all 
    the schedules that matches this student, and add the course of 
    the schedule that matches the student that calls this method to 
    an array to return it.
    We then do the same with students and Course, this will fully 
    flesh out our many-to-many relationship allowing for any instance 
    of student or course to call each other
    """
    
    def calculate_gpa(self):
        grades = [schedule.grade for schedule in Schedule.all
                  if schedule.student == self]
        return sum(grades)/len(grades)
    
    """
    For this method, we built in student we take advantage of our 
    existing courses method to find all of the courses this instance 
    of student is taking.
    Once we have that, we can loop through these courses to add up 
    our grade and find our gpa by taking this summative variable and 
    dividing it by the total amount of courses this student is taking
    """

class Course:
    all =[]
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        Course.all.append(self)
    
    def students(self):
        return [schedule.student for schedule in Schedule.all if
                schedule.course == self]

#Connecting class Student/Course/Grade
class Schedule:
    all = []
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
        Schedule.all.append(self)

"""
By adding a property to our student and course we can use the method 
is-instance to check to is if what is being used is an instance of a 
Student and Course class respectively. Similarly to an int or a str, 
we can check to see if a variable is an instance of a class which will 
properly set up our intermediary class.1
"""
@property
def student(self):
    return self._student
@student.setter
def student(self, value):
    if not isinstance(value, Student):
        raise Exception
    self._student = value

@property
def course(self):
    return self._course
@course.setter
def course(self, value):
    if not isinstance(value, Course):
        raise Exception
    self._course = value