import pdb

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, render_template, jsonify


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Constructor to initialize the Task object
    def __init__(self, title, description):
        self.title = title
        self.description = description


@app.route("/tasks", methods=["GET"])
def list_tasks(self=None):
    try:
        tasks = Task.query.all()
    except Exception as e:
        print(f"Error retrieving tasks: {e}")
        tasks = []
    return render_template("tasks/list.html", tasks=tasks)


@app.route("/tasks/create", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        try:
            title = request.form.get("title")
            description = request.form.get("description")
            new_task = Task(title=title, description=description)
            db.session.add(new_task)
            db.session.commit()
            return redirect("/tasks")
        except Exception as e:
            print(f"Error creating task: {e}")
            return redirect("/tasks/create")
    return render_template("tasks/create.html")


@app.route("/tasks/update/<int:id>", methods=["GET", "POST"])
def update_task(id: int):
    try:
        task = Task.query.get(id)
        if request.method == "POST":
            task.title = (
                request.form.get("title") if request.form.get("title") else None
            )
            task.description = (
                request.form.get("description")
                if request.form.get("description")
                else None
            )
            db.session.commit()
            return redirect("/tasks")
    except Exception as e:
        print(f"Error updating task: {e}")
        return redirect("/tasks")
    return render_template("tasks/edit.html", task=task)


@app.route("/tasks/delete/<int:id>", methods=["POST"])
def delete_task(id: int):
    try:
        task = Task.query.get(id)
        if task is not None:
            db.session.delete(task)
            db.session.commit()
    except Exception as e:
        print(f"Error deleting task: {e}")
    return redirect("/tasks")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
