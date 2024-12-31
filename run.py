from flask import Flask, redirect, render_template, request, session, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_message(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    message_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(message_dict)


@app.route('/', methods = ["GET", "POST"])
def index():
    # Main page with instructions
    # return "To send a message use /USERNAME/MESSAGE"
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route('/chat/<username>', methods = ["GET", "POST"])
def user(username):
    # Add and display chat messages
    if request.method == "POST":
        username = session["username"] 
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))
    
    return render_template("chat.html", username = username, chat_messages = messages)


if __name__== '__main__':
    # app.run()
    app.run(host='127.0.0.1', port=8080, debug=False)  
    # app.run(host="0.0.0.0", port=8080)
    # app.run(host='127.0.0.1', port=5000, debug=True)  