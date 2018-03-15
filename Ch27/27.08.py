class Assessment:
    def __init__(self,t,m):
        self.__AssessmentTittle = t
        self.__MaxMarks = m

    def OutputAssessmentDetails(self):
        print(self.__AssessmentTittle,'Marks: ',self.__MaxMarks)

class Course:
    def __init__(self,t,m,):
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__CourseLesson = []
        self.__CourseAssement = Assessment

    def AddLesson(self,t,d,r):
        self.__NumberOfLessons = self.__NumberOfLessons + 1
        self.__CourseLesson.append(Lesson(t,d,r))

    def AddAssessment(self,t,m):
        self.__CourseAssessment = Assessment(t,m)

    def OutputCourseDetails(self):
        print(self.__CourseTitle,end='')
        print('Maximum number of students: ',self.__MaxStudents)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())

class Lesson:
    def __init__(self,t,d,r):
        self.__LessonTittle = t
        self.__DurationMinutes = d
        self.__requiresLab = r

    def OutputLessonDetails(self):
        print(self.__LessonTittle, self.__DurationMinutes)

def Main():
    MyCourse = Course('Computing',10)
    MyCourse.AddAssessment('Programming',100)
    MyCourse.OutputCourseDetails()

Main()
