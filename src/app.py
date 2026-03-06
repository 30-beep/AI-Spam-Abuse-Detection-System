from flask import Flask, render_template, request, redirect
from ai_detector import analyze_comment

app = Flask(__name__)

comments = []
flagged_comments = []

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", comments=comments)

@app.route('/post_comment', methods=['POST'])
def post_comment():

    text = request.form['comment']
    result = analyze_comment(text)

    comment_data = {
        "text": text,
        "status": result
    }

    comments.append(comment_data)

    if result != "Safe":
        flagged_comments.append(comment_data)

    return redirect("/dashboard")

@app.route('/moderator')
def moderator():
    return render_template("moderator.html", comments=flagged_comments)

app.run(debug=True)
