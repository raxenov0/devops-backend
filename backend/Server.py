from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['POST'])
def post_data():
       data = request.data
       print(f"Received data: {data.decode('utf-8')}")
       with open("data.txt", "wb") as f:
           f.write(data)
       return '', 200

@app.route('/data', methods=['GET'])
def get_data():
       if os.path.exists("data.txt"):
           with open("data.txt", "rb") as f:
               data = f.read()
           print(f"Sending data: {data.decode('utf-8')}")
           return data, 200
       else:
           print("File not found")
           return 'File not found', 404

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=8080)  # Убедитесь, что хост установлен на '0.0.0.0'