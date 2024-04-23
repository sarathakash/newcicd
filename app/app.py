from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Devops and CICD Jenkins Application & webhooks github automatic the pull and push in the jenkins hooks'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
