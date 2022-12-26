from flask import Flask, render_template, request , redirect
path="C:/Users/Nandan Holla K/Documents/GitHub/DBMS-PROJECT"
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route("/",methods=["GET"])
def geth():
    return render_template("homepage.html")
@app.route("/student")
def getstudent():
    return render_template("student.html")
@app.route("/teacher")
def getteacher():
    return render_template("teacher.html")
@app.route("/admin")
def getadmin():
    return render_template("admin.html")
@app.route("/csbs3",methods=["POST"])
def hello():
    return "Hello World"
@app.route("/addinstructors",methods=["GET"])
def addcourses():
    instructors='#'
    rooms='#'
    timings='#'
    courses='#'
    depts='#'
    sections='#'
    gene='#'
    password='#'
    log='#'
    return render_template("addinstructors.html",addInstructors=instructors,addRooms=rooms,addTimings=timings,addCourses=courses,addDepts=depts,addSections=sections,generate=gene,password_change=password,logout=log,n="Nandan")

# @app.route('/csbs3', methods = ['POST'])
# def home():
#     data = "hello world"
#     return jsonify({'data': data})
if __name__ == '__main__':
    app.run(debug = True)