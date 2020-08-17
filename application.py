from flask import Flask, render_template, request, session 
from flask_session import Session 

app=Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def note():
    if session.get("notes") is None:
        session["notes"] = [["head1","body1"],["head2","body2"]]
    if request.method == "POST":
        note=[]
        header=request.form.get("header")
        note.append(header)
        body=request.form.get("body")
        note.append(body)
        session["notes"].append(note)
    
    return render_template("note.html", notes=session["notes"])