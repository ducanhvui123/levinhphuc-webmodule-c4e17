from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            "title": "Anh Tuan Anh nhat",
            "content": "hihihihih",
            "author": "Tuan Anh",
            "gender": 1
        },
        {
        "title": "Anh Tuan Anh nhat",
         "content": "hihihihih",
         "author": "Tuan Anh",
         "gender": 0
        },
        {
        "title": "muoi",
        "content": "muoi trong tim anh thay xe long",
        "author": "haha",
        "gender": 1
        }
    ]
    
    return render_template("index.html",posts=posts)

@app.route('/c4e')
def sayhi():
    return "Hi C4E17"

@app.route('/sayhi/<name>/<age>')
def sayhello(name, age):
    return "Hi {0}, you are {1} years old".format(name, age)

if __name__ == '__main__':
  app.run(debug=True)
 
