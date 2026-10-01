from flask import Flask, render_template, request

app = Flask(__name__)

suspicious_words = [
    "click here",
    "verify your account",
    "urgent",
    "win money",
    "lottery",
    "free prize",
    "send otp",
    "share otp",
    "password",
    "bank account",
    "claim now"
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    detected = []

    if request.method == "POST":
        message = request.form.get("message", "")
        for word in suspicious_words:
            if word.lower() in message.lower():
                detected.append(word)

        if len(detected) >= 2:
            result = "HIGH RISK 🔴"
        elif len(detected) == 1:
            result = "SUSPICIOUS 🟠"
        else:
            result = "LOW RISK 🟢"

    return render_template(
        "index.html",
        result=result,
        detected=detected
    )

if __name__ == "__main__":
    app.run(debug=True)