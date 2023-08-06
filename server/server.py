from flask import Flask, redirect, url_for, request
from main import main


app = Flask(__name__)





@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        url = request.args['url']
        resp = Flask.response_class(main(url)) 
        print(main(url))
        print(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


if __name__ == '__main__':
    app.run(debug=True)
