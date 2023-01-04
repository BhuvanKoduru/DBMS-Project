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
            "uid": "Teacher UID",
            "name": "Full Name",
            "Desig":"Designation"
        }
        #widgets= {
         #   'uid':forms.TextInput(),
          #  'name':forms.TextInput(),
           # 'Desig':forms.Select()
        widgets = {
            'uid': forms.TextInput(attrs={'class':"test-class"}),
            'name': forms.TextInput(attrs={'class':"test-class"}),
            'Desig': forms.Select(attrs={'class':"test-class"}),
            #'dept': forms.Select(attrs={'class':"test-class"})    
        }
        fields = [
            'uid',
            'name',
            'Desig'
        ]





class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name', \
        'instructors']
        labels = {
            "course_number": "Course ID",
            "course_name": "Course Name",
            "instructors": "Course Teachers"
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
            'pid',
            'time',
            'day',
            'dept'
            
        ]
        widgets = {
            'pid': forms.TextInput(attrs={'class':"test-class"}),
            'time': forms.Select(attrs={'class':"test-class"}),
            'day': forms.Select(attrs={'class':"test-class"}),
            'dept': forms.Select(attrs={'class':"test-class"})
        
        }
        labels = {
            "pid": "Meeting ID",
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
