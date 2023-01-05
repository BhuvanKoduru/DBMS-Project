from django.forms import ModelForm
from. models import *
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        labels = {
            "r_number": "Room ID",
            "room_type":"Room Type"
        }
        widgets={
            "r_number":forms.TextInput(),
            "room_type":forms.Select()
        }
        fields = [
            'r_number',
            'room_type'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        labels = {
            "t_id": "Teacher ID",
            "name": "Full Name",
            "Desig":"Designation"
        }
        widgets= {
            't_id':forms.TextInput(),
            'name':forms.TextInput(),
            'Desig':forms.Select()
            
        }
        fields = [
            't_id',
            'name',
            'Desig'
        ]





class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name', \
        'instructor']
        labels = {
            "course_number": "Course ID",
            "course_name": "Course Name",
            "instructor": "Course Teacher"
        }

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'courses']
        labels = {
            "dept_name": "Department Name",
            "courses": "Corresponding Courses"
        }

class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = [
            'm_id',
            'time',
            'day',
            'dept'
            
        ]
        widgets = {
            'm_id': forms.TextInput(attrs={'class':"test-class"}),
            'time': forms.Select(attrs={'class':"test-class"}),
            'day': forms.Select(attrs={'class':"test-class"}),
            'dept': forms.Select(attrs={'class':"test-class"})
        
        }
        labels = {
            "m_id": "Meeting ID",
            "time": "Time",
            "day": "Day of the Week",
            "dept": "Department"
           
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
