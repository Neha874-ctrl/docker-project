from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for student data
students = []


@app.route("/")
def home():
    return render_template("index.html", students=students)


@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form.get("name")
    roll_number = request.form.get("roll_number")
    course = request.form.get("course")
    email = request.form.get("email")

    student = {
        "name": name,
        "roll_number": roll_number,
        "course": course,
        "email": email
    }

    students.append(student)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
