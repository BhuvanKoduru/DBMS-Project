# Timetable Generation System

<h3>Project Description</h3>
<p>The project, IS Timetable Generator, is a web application developed using the Django Framework and an SQLite database.</p>
<p>The project makes use of a genetic algorithm to satisfy the soft and hard constraints and generate the most optimal timetable. The web application includes a simple authentication-authorization module, and on successfull authentication the user is redirected to the admin dashboard.</p>
<p>On the admin dashboard the user can input the data of the college/university which is required to generate the timetable. The user must add the following details:</p>
<ol>
  <li>Teachers</li>
  <li>Classrooms</li>
  <li>Timings</li>
  <li>Courses</li>
  <li>Departments</li>
  <li>Sections</li>
</ol>
<p>Constraints:</p>
<ol>
  <li>No two classes occur in the same room</li>
  <li>No teacher teaches any two classes at the same time</li>
  <li>A teacher doesn't take more than one class per day per section</li>
  <li>No teacher takes consecutive classes apart from before and after breaks. </li>
  <li>No teacher teaches for more than 6 hours per day</li>
  <li>No two classes happen at the same time for any section</li>
</ol>
<p>Upon successfull entry of the data into sqlite database, the user can navigate to the "Generate Timetable" page to start the process of generating the timetable. Upon successfull generation of the timetable the user can download the timetable as a PDF.</p>   

<p>Technologies Used:</p>
<ul>
  <li>HTML5</li>
  <li>CSS3</li>
  <li>Python 3.8</li>
  <li>Django 3.0.*</li>
  <li>JavaScript</li>
  <li>sqlite3</li>
</ul>

<h3>Contact</h3>
<p>Email: bckoduru@gmail.com</p>
