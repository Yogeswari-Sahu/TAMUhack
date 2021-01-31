from chatbot import chatbot
from flask import Flask, render_template, request
from chat_bot_general_health import ask_question_tfidf

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return ask_question_tfidf(userText)

if __name__ == "__main__":
    app.run()
