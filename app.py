from flask import Flask, render_template

app = Flask(__name__)

tareas = []

@app.route("/")
def home():
    # return render_template("index.html", tareas=tareas)
    return render_template("index.html")

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    # if request.method == "GET":
       return render_template("agregar.html")
    # else:
        # tarea =request.form.get("tarea")
        # tareas.append(tarea)
        # return redirect("home")
# 
if __name__ == "__main__":
    app.run(debug=True)