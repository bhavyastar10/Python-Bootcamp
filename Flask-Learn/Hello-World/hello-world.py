from flask import Flask, request
# pymessenger - Bot
# requests

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello, World'

if __name__ == '__main__':
    app.run()