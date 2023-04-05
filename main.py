from school_schedule.student import Student
# from school_schedule.high_school_student import HighSchoolStudent
from school_schedule.middle_school_student import MiddleSchoolStudent

# first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")

# second instance
ellis = MiddleSchoolStudent(
                "Ellis", 
                "junior", 
                ["Painting"],
                gets_transportation=True,
                # clubs=["Algorithms Club"]
            )



students = [quinn, ellis]
for student in students:
    print(student.summary())