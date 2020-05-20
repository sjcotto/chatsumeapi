from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from train import bot

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['POST'])
def get_bot_response():    
    data = request.get_json(force = True)  
    response = bot.get_response(data["mssg"])
    return jsonify(results = str(response))

if __name__ == "__main__":    
    app.run(host ='0.0.0.0', port = 5001, debug = True)
