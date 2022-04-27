from flask import Flask

application = Flask(__name__)

@application.route('/', methods=['GET','POST'])
def hello_world():
    return 'Hello World Shreyas'


if __name__ == '__main__':
    application.run()