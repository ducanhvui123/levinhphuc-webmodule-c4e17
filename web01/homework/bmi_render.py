from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmiren/<int:weight>/<int:height>')
def index(weight, height):
    height = height/100
    b = weight/(height*height)
    return render_template("index1.html", result = b )

if __name__ == '__main__':
  app.run(debug=True)
 