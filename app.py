from flask import Flask, render_template, request
import smtplib
from data.projects import projects

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def project_page():
    return render_template("projects.html", projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("officially.ekongg@gmail.com", "yniepeqlognndisg")
            server.sendmail(
                email,
                "officially.ekongg@gmail.com",
                f"From: {name}\nEmail: {email}\n\n{message}"
            )

        return render_template("contact.html", success=True)

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
