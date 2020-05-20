from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from train import bot

app = Flask(__name__)




@app.route("/", methods = ['POST'])
@cross_origin()
def get_bot_response():    
    data = request.get_json(force = True)  
    response = bot.get_response(data["mssg"])
    # print(response)
    return jsonify(results = str(response))

if __name__ == "__main__":    
    app.run()
