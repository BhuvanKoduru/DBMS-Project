from django.http import request
from django.shortcuts import render, redirect
from . forms import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .render import Render
from django.views.generic import View
import random


POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.05




timings ={
    "IS_SEM_3" : {
        "MON": ["11:00 - 11:50","11:50 - 12:40","12:40 - 1:30"],
        "TUE": ["8:30 - 9:30","9:30 - 10:30","11:00 - 11:50","11:50 - 12:40","12:40 - 1:30"],
        "WED": ["8:30 - 9:30","9:30 - 10:30"],
        "THR": ["7:30 - 8:30","8:30 - 9:30","9:30 - 10:30","11:00 - 11:50","11:50 - 12:40","12:40 - 1:30"],
        "FRI": ["9:30 - 10:30","11:00 - 11:50","11:50 - 12:40","12:40 - 1:30"],
        "SAT": ["9:30 - 10:30","11:00 - 11:50","11:50 - 12:40","12:40 - 1:30"]
    },
    "IS_SEM_5" : {
        "MON": ["11:00 - 11:50","11:50 - 12:40","12:40 - 1:30","2:30 - 3:30","3:30 - 4:30","4:30 - 5:30"],
        "TUE": ["7:30 - 8:30","8:30 - 9:30"],
        "WED": ["11:00 - 11:50","11:50 - 12:40","12:40 - 1:30","2:30 - 3:30","3:30 - 4:30","4:30-5:30"],
        "THR": ["11:00-11:50","11:50-12:40","12:40-1:30"],
        "FRI": ["9:30-10:30","11:00-11:50","11:50-12:40","12:40-1:30"],
        "SAT":[]
    },
    "IS_SEM_7" : {
        "MON": ["11:00-11:50","11:50-12:40","12:40-1:30","2:30-3:30","3:30-4:30","4:30-5:30"],
        "TUE": [],
        "WED": ["11:00-11:50","11:50-12:40","12:40-1:30","2:30-3:30","3:30-4:30","4:30-5:30"],
        "THR": ["8:30-9:30","9:30-10:30"],
        "FRI": ["11:00-11:50","11:50-12:40","12:40-1:30","2:30-3:30","3:30-4:30"],
        "SAT": ["11:00-11:50","11:50-12:40","12:40-1:30"]
    }
}

teachers_set=set()
teachers_list=list()
timing_map= {
"7:30 - 8:30": 1,
"8:30 - 9:30":2,
"9:30 - 10:30":3,
"11:00 - 11:50":4,
"11:50 - 12:40":5,
"12:40 - 1:30":6,
"2:30 - 3:30":7,
"3:30 - 4:30":8,
"4:30 - 5:30":9
}






class Data:
    def __init__(self):
        self._rooms = Room.objects.all()
        self._meetingTimes = MeetingTime.objects.all()
        self._instructors = Instructor.objects.all()
        self._courses = Course.objects.all()
        self._depts = Department.objects.all()

    def get_rooms(self): return self._rooms

    def get_instructors(self): return self._instructors

    def get_courses(self): return self._courses

    def get_depts(self): return self._depts\

    def get_meetingTimes(self): return self._meetingTimes


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numberOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self): return self._numberOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness



    def initialize(self):
        sections = Section.objects.all()
        #print(sections[0].num_class_in_week)
        for section in sections:
            # print(section.meeting_time)
            dept = section.department
            n = section.num_class_in_week
            #n=0
            courses = dept.courses.all()
            # print("Here are the credits")
            # print(courses[0].credits)
            #for course in courses:
            #    n+=int(course.credits)
            if n <= len(MeetingTime.objects.all()):
                courses = dept.courses.all()
                for course in courses:
                    #print(course)
                    for i in range (int(course.credits)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept, section.section_id, course)
                        self._classNumb += 1
                        flag=1
                        x=data.get_meetingTimes()[rnd.randrange(0, len(MeetingTime.objects.all()))]
                        #print(x)
                        newClass.set_meetingTime(x)
                        newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                        newClass.set_instructor(crs_inst[rnd.randrange(0, len(crs_inst))])
                        #print(newClass.meeting_time.day)
                        self._classes.append(newClass)
            else:
                n = len(MeetingTime.objects.all())
                courses = dept.courses.all()
                for course in courses:
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept, section.section_id, course)
                        self._classNumb += 1
                        flag=1
                        while (flag):
                            temp_timing_obj = data.get_meetingTimes()[rnd.randrange(0, len(MeetingTime.objects.all()))]
                            dict_of_sem = timings[dept.dept_name]
                            day_list= dict_of_sem[temp_timing_obj.day]
                            if temp_timing_obj.time in day_list:
                                newClass.set_meetingTime(temp_timing_obj)
                                flag=0

                        print("yay while loop!")

                         
                        
                        #newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(MeetingTime.objects.all()))])
                        newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                        # print(crs_inst)
                        newClass.set_instructor(crs_inst[rnd.randrange(0, len(crs_inst))])
                        self._classes.append(newClass)


        return self

    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.get_classes()
        for i in range(len(classes)):
            # d=classes[i].meeting_time.day
            # t=classes[i].meeting_time.time
            # de=classes[i].department.dept_name
            # deptdic=timings[de]
            # daylist=deptdic[d]
            # if(t not in daylist):
            #     self._numberOfConflicts += 1
            #print(classes[i])
            for j in range(len(classes)):
                if j > i:
                    #print(classes[j].section_id)
                    if (classes[i].meeting_time == classes[j].meeting_time) and \
                            (classes[i].section_id != classes[j].section_id) and (classes[i].section == classes[j].section):
                        if classes[i].room == classes[j].room:
                            self._numberOfConflicts += 1
                        if classes[i].instructor == classes[j].instructor:
                            self._numberOfConflicts += 1
                        if classes[i].course!=classes[j].course:
                            self._numberOfConflicts += 1
                    elif((classes[i].meeting_time.day==classes[j].meeting_time.day) and (classes[i].meeting_time.time!=classes[j].meeting_time.time) and(classes[i].instructor == classes[j].instructor) and(classes[i].section_id != classes[j].section_id)and(classes[i].section== classes[j].section)):
                        self._numberOfConflicts += 1
                      
                    elif((classes[i].meeting_time.day==classes[j].meeting_time.day)and(classes[i].instructor == classes[j].instructor)and(abs(timing_map[classes[i].meeting_time.time]-timing_map[classes[j].meeting_time.time])==1)):
                        if((abs(timing_map[classes[i].meeting_time.time]+timing_map[classes[j].meeting_time.time])!=7) or (abs(timing_map[classes[i].meeting_time.time]+timing_map[classes[j].meeting_time.time])!=13)):
                            self._numberOfConflicts += 1
                      
                    elif( (classes[i].meeting_time.day==classes[j].meeting_time.day) and (classes[i].instructor == classes[j].instructor )and (abs(timing_map[classes[i].meeting_time.time]-timing_map[classes[j].meeting_time.time])>5)):
                       self._numberOfConflicts += 1
                  



                       
        return 1 / (1.0 * self._numberOfConflicts + 1)


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = [Schedule().initialize() for i in range(size)]

    def get_schedules(self):
        return self._schedules


class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if rnd.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(len(mutateSchedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop


class Class:
    def __init__(self, id, dept, section, course):
        self.section_id = id
        self.department = dept
        self.course = course
        self.instructor = None
        self.meeting_time = None
        self.room = None
        self.section = section

    def get_id(self): return self.section_id

    def get_dept(self): return self.department

    def get_course(self): return self.course

    def get_instructor(self): return self.instructor

    def get_meetingTime(self): return self.meeting_time

    def get_room(self): return self.room

    def set_instructor(self, instructor): self.instructor = instructor

    def set_meetingTime(self, meetingTime): self.meeting_time = meetingTime

    def set_room(self, room): self.room = room


data = Data()


def context_manager(schedule):
    classes = schedule.get_classes()
    context = []
    cls = {}
    for i in range(len(classes)):
        cls["section"] = classes[i].section_id
        cls['dept'] = classes[i].department.dept_name
        cls['course'] = f'{classes[i].course.course_name} ({classes[i].course.course_number}, ' \
                        f'{classes[i].course.max_numb_students}'
        cls['room'] = f'{classes[i].room.r_number} ({classes[i].room.seating_capacity})'
        cls['instructor'] = f'{classes[i].instructor.name} ({classes[i].instructor.uid})'
        cls['meeting_time'] = [classes[i].meeting_time.pid, classes[i].meeting_time.day, classes[i].meeting_time.time]
        context.append(cls)
        #teachers.add(classes[i].instructor.name)
    #print(teachers)
    return context


def timetable(request):
    schedule = []
    population = Population(POPULATION_SIZE)
    generation_num = 0
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    geneticAlgorithm = GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_num += 1
        print('\n> Generation #' + str(generation_num))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        schedule = population.get_schedules()[0].get_classes()


    timings_list = [[''],['7:30 - 8:30'],['8:30 - 9:30'], ['9:30 - 10:30'], ['11:00 - 11:50'], ['11:50 - 12:40'], ['12:40 - 1:30'], ['2:30 - 3:30'], ['3:30 - 4:30'], ['4:30 - 5:30']]
    days_list = [['MON'], ['TUE'], ['WED'], ['THR'], ['FRI'],['SAT']]

    tt = {}

    for section in (Section.objects.all()):
        t = [ ["-"] * (len(timings_list)  - 1) for i in range(len(days_list))]
        t.insert(0, timings_list)
        for i in range(1, len(t)):
            t[i].insert(0, days_list[i - 1])

        timings_list_map = {'': 0, '7:30 - 8:30': 1, '8:30 - 9:30': 2, '9:30 - 10:30': 3, '11:00 - 11:50': 4, '11:50 - 12:40': 5, '12:40 - 1:30':6,'2:30 - 3:30': 7, '3:30 - 4:30': 8, '4:30 - 5:30': 9}
        days_list_map = {'MON': 1, 'TUE': 2, 'WED': 3, 'THR': 4, 'FRI': 5,'SAT':6}

        for i in schedule:
            t[days_list_map[i.meeting_time.day]][timings_list_map[i.meeting_time.time]] = [i.course.course_name, i.room.r_number, i.instructor.name]
            teachers_set.add(i.instructor.name)

        tt[str(section.section_id) + " " + str(section.department)] = t
    #teachers_list=list(teachers_set)

    print(tt)
  
    return render(request, 'gentimetable.html', {'schedule': schedule, 'sections': Section.objects.all(),
                                              'times': MeetingTime.objects.all(), 'timetable': tt})

    #return render(request, 'gentimetable.html', {'schedule': schedule, 'sections': Section.objects.all(),
    #                                          'times': MeetingTime.objects.all()})

############################################################################


def index(request):
    return render(request, 'homepage.html', {})


def about(request):
    return render(request, 'aboutus.html', {})


def help(request):
    return render(request, 'help.html', {})


def terms(request):
    return render(request, 'terms.html', {})


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('TTGS Contact',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['bckoduru@gmail.com'],
                  fail_silently=False)
    return render(request, 'contact.html', {})

def teacher_home(request):
    return render(request,'help.html')

#################################################################################

@login_required
def admindash(request):
    return render(request, 'admindashboard.html', {})

#################################################################################

@login_required
def addCourses(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addCourses')
        else:
            print('Invalid')
    context = {
        'form': form
    }
    return render(request, 'addCourses.html', context)

@login_required
def course_list_view(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courseslist.html', context)

@login_required
def delete_course(request, pk):
    crs = Course.objects.filter(pk=pk)
    if request.method == 'POST':
        crs.delete()
        return redirect('editcourse')

#################################################################################

@login_required
def addInstructor(request):
    form = InstructorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addInstructors')
    context = {
        'form': form
    }
    return render(request, 'addInstructors.html', context)

@login_required
def inst_list_view(request):
    context = {
        'instructors': Instructor.objects.all()
    }
    return render(request, 'inslist.html', context)

@login_required
def delete_instructor(request, pk):
    inst = Instructor.objects.filter(pk=pk)
    if request.method == 'POST':
        inst.delete()
        return redirect('editinstructor')

#################################################################################

@login_required
def addRooms(request):
    form = RoomForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addRooms')
    context = {
        'form': form
    }
    return render(request, 'addRooms.html', context)

@login_required
def room_list(request):
    context = {
        'rooms': Room.objects.all()
    }
    return render(request, 'roomslist.html', context)

@login_required
def delete_room(request, pk):
    rm = Room.objects.filter(pk=pk)
    if request.method == 'POST':
        rm.delete()
        return redirect('editrooms')

#################################################################################

@login_required
def addTimings(request):
    form = MeetingTimeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addTimings')
        else:
            print('Invalid')
    context = {
        'form': form
    }
    return render(request, 'addTimings.html', context)

@login_required
def meeting_list_view(request):
    context = {
        'meeting_times': MeetingTime.objects.all()
    }
    return render(request, 'mtlist.html', context)

@login_required
def delete_meeting_time(request, pk):
    mt = MeetingTime.objects.filter(pk=pk)
    if request.method == 'POST':
        mt.delete()
        return redirect('editmeetingtime')

#################################################################################

@login_required
def addDepts(request):
    form = DepartmentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addDepts')
    context = {
        'form': form
    }
    return render(request, 'addDepts.html', context)

@login_required
def department_list(request):
    context = {
        'departments': Department.objects.all()
    }
    return render(request, 'deptlist.html', context)

@login_required
def delete_department(request, pk):
    dept = Department.objects.filter(pk=pk)
    if request.method == 'POST':
        dept.delete()
        return redirect('editdepartment')

#################################################################################

@login_required
def addSections(request):
    form = SectionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addSections')
    context = {
        'form': form
    }
    return render(request, 'addSections.html', context)

@login_required
def section_list(request):
    context = {
        'sections': Section.objects.all()
    }
    return render(request, 'seclist.html', context)

@login_required
def delete_section(request, pk):
    sec = Section.objects.filter(pk=pk)
    if request.method == 'POST':
        sec.delete()
        return redirect('editsection')

#################################################################################

@login_required
def generate(request):
    return render(request, 'generate.html', {})

#################################################################################

class Pdf(View):
    def get(self, request):
        params = {
            'request': request
        }
        return Render.render('gentimetable.html', params)


