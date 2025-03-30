from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def calculate_grade():
    name = request.form["name"].upper() 
    grade1 = float(request.form["grade1"])
    grade2 = float(request.form["grade2"])
    grade3 = float(request.form["grade3"])

    final_grade = (grade1 + grade2 + grade3) / 3
    grade_prompt = "SIN NOTA"
    if (final_grade >= 5):
        grade_prompt = "APROBADO"
    elif (final_grade > 5 & final_grade <= 9 ):
        grade_prompt = "NOTABLE"
    else:
        grade_prompt = "SOBRESALIENTE"

    return render_template("result.html", name=name, final_grade=round(final_grade, 2), grade_prompt= grade_prompt)

if __name__ == "__main__":
    app.run(debug=True)


def notaFinal(nota):
    if (nota > 8):
        mensaje = "SOBRESALIENTE"
    elif (nota < 5):
        mensaje = "SUSPENSO"
    else:
        mensaje = "APROBADO"
    return mensaje