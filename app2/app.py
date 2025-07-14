from flask import Flask,request
import requests
app2=Flask(__name__)

@app2.route('/')
def index():
    return "Welcome to index page in app2."

@app2.route('/forward')
def get_from_app1():
    url_path = request.args
    print(url_path)
    response=requests.get("http://app1:5000/")
    return f"Response form app1: {response.text}"

if __name__=='__main__':
    app2.run(host='0.0.0.0',port=5001)

