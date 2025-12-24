from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/password-awareness")
def password_awareness():
    return render_template("password_awareness.html")

@app.route("/https-check", methods=["GET", "POST"])
def https_check():
    result = ""
    if request.method == "POST":
        url = request.form.get("url")
        if url.startswith("https://"):
            result = "SECURE: HTTPS is enabled"
        else:
            result = "NOT SECURE: HTTPS is missing"
    return render_template("https_check.html", result=result)

@app.route("/phishing-test", methods=["GET", "POST"])
def phishing_test():
    score = 0
    if request.method == "POST":
        answers = request.form
        correct_answers = ["phishing", "legit", "phishing"]
        for i, correct in enumerate(correct_answers):
            if answers.get(f"q{i}") == correct:
                score += 1
        return render_template("result.html", score=score)
    return render_template("phishing_test.html")

if __name__ == "__main__":
    app.run(debug=True)
