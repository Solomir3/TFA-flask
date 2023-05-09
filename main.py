from flask import Flask, jsonify
import os
import time


app = Flask(__name__)


@app.route('/')
def index():
    for i in range(2)
        print(i)
        time.sleep(3)
        
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
