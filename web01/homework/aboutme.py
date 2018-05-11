from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def index():
    blog = {
        "title": "This is some information about me",
        "content": '''Name: Lê Vĩnh Phúc,
         work: newbie developer
         hobbies: coding, playing computer games, have fun with friends and collecting stamps
         my Crush: Hoàng Diệu Anh''',
         "author": "made by Lê Vĩnh Phúc",


    }
    return render_template('index.html', blog=blog)


@app.route('/school')
def hello():
    return redirect("http://techkids.vn/", code=302)

if __name__ == '__main__':
  app.run(debug=True)
 
