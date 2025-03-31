from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def calculate_grade():
    student_count = 0
    names = []
    grade1 = []
    grade2 = []
    grade3 = []
    final_grade = []
    grade_prompt = []
    
    names.append(request.form["name"].upper())
    grade1.append(float(request.form["grade1"]))
    grade2.append(float(request.form["grade2"]))
    grade3.append(float(request.form["grade3"]))

    final_grade.append(
        round(
            (
                grade1[student_count] + 
                grade2[student_count] + 
                grade3[student_count]) / 3), 
            2)

    if (final_grade >= 5):
        grade_prompt.append("APROBADO")
    elif (final_grade > 5 & final_grade <= 9 ):
        grade_prompt.append("NOTABLE")
    else:
        grade_prompt.append("SOBRESALIENTE")

    student_count +=1

    return render_template("result.html", names=names, final_grade=round(final_grade, 2), grade_prompt= grade_prompt)
    


if __name__ == "__main__":
    app.run(debug=True)

