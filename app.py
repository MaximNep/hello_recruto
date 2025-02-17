from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello_recruto():
    name = request.args.get('name', 'Recruto')
    message = request.args.get('message', 'Давай дружить')
    return f"Hello {name}! {message}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
