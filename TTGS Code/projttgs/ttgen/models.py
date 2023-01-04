from django.db import models
import math
import random as rnd
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date

time_slots = (
    ('7:30 - 8:30', '7:30 - 8:30'),
    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)
DESIGNATIONS=(
    ('Asst Prof','Asst Prof'),
    ('Prof','Prof'),
    ('Asso Prof','Asso Prof')
)
Room_Type=(
    ('Theory','Theory'),
    ('Lab','Lab')
)

DEPTS = (
    ("IS_SEM_3","IS_SEM_3"),
    ("IS_SEM_5","IS_SEM_5"),
    ("IS_SEM_7","IS_SEM_7"),
    ("CSBS_SEM_1","CSBS_SEM_1"),
    ("CSBS_SEM_3","CSBS_SEM_3"),
    ("CSBS_SEM_5","CSBS_SEM_5"),
    ("CSBS_SEM_7","CSBS_SEM_7"),
)

POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1


class Room(models.Model): #done
    r_number = models.CharField(max_length=6)
    room_type=models.CharField(max_length=25,choices=Room_Type,default='Theory')

    def __str__(self):
        return self.r_number
    class Meta:
        db_table="Room"


class Instructor(models.Model): #done
    t_id = models.CharField(max_length=6)
    name = models.CharField(max_length=25)
    Desig = models.CharField(max_length=25,choices=DESIGNATIONS,default='Asst Prof')


    def __str__(self):
        return f'{self.t_id} {self.name}'

    class Meta:
        db_table="Faculty"

class Course(models.Model): #done
    course_number = models.CharField(max_length=15, primary_key=True)
    course_name = models.CharField(max_length=40)
    instructor = models.ManyToManyField(Instructor)


    def __str__(self):
        return f'{self.course_number} {self.course_name}'

    class Meta:
        db_table="Courses"

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    @property
    def get_courses(self):
        return self.courses

    def __str__(self):
        return f'{self.dept_name}'
    
    class Meta:
        db_table="Department"

class MeetingTime(models.Model):
    m_id = models.CharField(max_length=4, primary_key=True)
    time = models.CharField(max_length=50, choices=time_slots, default='11:30 - 12:30')
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)
    dept=models.CharField(max_length=15,choices=DEPTS,default="IS_SEM_3")

    

    def __str__(self):
        return f'{self.pid} {self.day} {self.time}'
    
    class Meta:
        db_table="Class Timing"


class Section(models.Model):
    section_id = models.CharField(max_length=25, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    num_class_in_week = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    meeting_time = models.ForeignKey(MeetingTime, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, null=True)

    def set_room(self, room):
        section = Section.objects.get(pk = self.section_id)
        section.room = room
        section.save()

    def set_meetingTime(self, meetingTime):
        section = Section.objects.get(pk = self.section_id)
        section.meeting_time = meetingTime
        section.save()

    def set_instructor(self, instructor):
        section = Section.objects.get(pk=self.section_id)
        section.instructor = instructor
        section.save()

    class Meta:
        db_table="Section"
