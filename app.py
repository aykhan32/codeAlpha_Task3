from flask import Flask, request
import os
import pickle

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    username = request.form['username']
    file = request.files['file']
    file.save(f"./uploads/{username}.txt")

    os.system("echo 'User Uploaded File'")

    return "Upload Successful"

@app.route('/load', methods=['POST'])
def load():
    user = request.form['user']
    data = request.form['data']
    obj = pickle.loads(data.encode())  # Deserialization
    return f"Data loaded for {user}"

if __name__ == "__main__":
    app.run(debug=True)
