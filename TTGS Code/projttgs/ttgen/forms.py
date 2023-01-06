from django.forms import ModelForm
from. models import *
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        labels = {
            "r_number": "Room ID",
            "seating_capacity": "Capacity"
        }
        fields = [
            'r_number',
            'seating_capacity'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        labels = {
            "uid": "Teacher UID",
            "name": "Full Name"
        }
        fields = [
            'uid',
            'name',
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
        fields = ['course_number', 'course_name', 'max_numb_students', 'instructors']
        labels = {
            "course_number": "Course ID",
            "course_name": "Course Name",
            "max_numb_students": "Course Capacity",
            "instructors": "Course Teachers"
        }
        widgets = {
             'course_number': forms.TextInput(attrs={'class':"test-class"}),
            'course_name': forms.TextInput(attrs={'class':"test-class"}),
            'max_numb_students': forms.TextInput(attrs={'class':"test-class"}),
            "instructors":forms.Select(attrs={'class':"test-class"})

        }
        


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'courses']
        labels = {
            "dept_name": "Department Name",
            "courses": "Corresponding Courses"
        }
        widgets = {
             'dept_name': forms.TextInput(attrs={'class':"test-class"}),
            'courses': forms.Select(attrs={'class':"test-class"}),
            #'day': forms.Select(attrs={'class':"test-class"}),
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
