from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def calculate_grade():
    students = []

    for i in range(1, 6):
        try:
            name = request.form[f"name{i}"].strip().upper()
            grade1 = float(request.form[f"grade{i}_1"])
            grade2 = float(request.form[f"grade{i}_2"])
            grade3 = float(request.form[f"grade{i}_3"])
        except KeyError:
            return "Missing form data. Please ensure all fields are filled.", 400
        except ValueError:
            return "Invalid input. Please enter numeric values for grades.", 400

        final_grade = round((grade1 + grade2 + grade3) / 3, 2)

        if final_grade < 5:
            result = "FAILED"
        elif 5 <= final_grade <= 7:
            result = "PASSED"
        elif 7 < final_grade <= 9:
            result = "GOOD"
        else:
            result = "EXCELLENT"

        students.append({"name": name, "grade": final_grade, "result": result})

    return render_template("result.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
