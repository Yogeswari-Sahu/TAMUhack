from flask import Flask, render_template, request
from chat_bot_general_health import ask_question_tfidf
from medicines_chatbot_query import ask_question_tfidf_medicine

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/disease")
def disease_home():
    return render_template("disease.html")

@app.route("/getdisease")
def get_bot_response_disease():
    userText = request.args.get('msg')
    return ask_question_tfidf(userText)

@app.route("/medicine")
def medicine_home():
    return render_template("medicine.html")

@app.route("/getmedicine")
def get_bot_response_medicine():
    userText = request.args.get('msg')
    return ask_question_tfidf_medicine(userText)

if __name__ == "__main__":
    app.run()
