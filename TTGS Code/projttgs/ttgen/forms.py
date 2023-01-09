from django.forms import ModelForm
from. models import *
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        labels = {
            "r_number": "Room ID",
            #"seating_capacity": "Capacity",
            "r_type": "Room type"
        }
        fields = [
            'r_number',
            #'seating_capacity'
            'r_type'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        labels = {
            "uid": "Teacher ID",
            "name": "Full Name",
            "desig": "Designation"

        }
        widgets = {
             'uid': forms.TextInput(attrs={'class':"test-class"}),
            'name': forms.TextInput(attrs={'class':"test-class"}),
            'desig': forms.Select(attrs={'class':"test-class"}),
        }
        fields = [
            'uid',
            'name',
            'desig'
        ]


class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = [
            'pid',
            'time',
            'day'
        ]
        widgets = {
             'pid': forms.TextInput(attrs={'class':"test-class"}),
            'time': forms.Select(attrs={'class':"test-class"}),
            'day': forms.Select(attrs={'class':"test-class"}),
        }
        labels = {
            "pid": "Meeting ID",
            "time": "Time",
            "day": "Day of the Week"
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'credits', 'instructors']
        labels = {
            "course_number": "Course ID",
            "course_name": "Course Name",
            "credits": "Course Credits",
            "instructors": "Course Teachers"
        }
        # widgets = {
        #      'course_number': forms.TextInput(attrs={'class':"test-class"}),
        #     'course_name': forms.TextInput(attrs={'class':"test-class"}),
        #     'credits': forms.TextInput(attrs={'class':"test-class"}),
        #     "instructors":forms.MultipleChoiceField(attrs={'class':"test-class"})

        # }
        


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'courses']
        labels = {
            "dept_name": "Department Name",
            "courses": "Corresponding Courses"
        }


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'department', 'num_class_in_week']
        labels = {
            "section_id": "Section ID",
            "department": "Corresponding Department",
            "num_class_in_week": "Classes Per Week"
        }
