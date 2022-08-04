import winsound


class student:
    def __init__(self, name, courses, grades):
        self.name = name
        self.courses = courses
        self.grades = grades

    def gpa(self):
        sum = 0
        for grade in self.grades:
            sum = sum + grade
        gpa = sum / len(self.grades)
        return gpa

 #shows if students share a class 
    def share_classes(self, other):
        self.courses
        
        other.courses

        for courses in self.courses:
            for other_cousrse in other.courses:
                if (course == other_cousrse):
                    print("you share a course: " + courses)
                    return
        print("You do not share a course")

Patrick = student("ibrahima", ["Physics", "Math", "English"], [50, 20, 70])
omari = student("omari", ["computer science", "Math", "English"], [70, 92, 90])
winston = student("winston", ["Math", "English", "Science"], [20, 28, 93])
