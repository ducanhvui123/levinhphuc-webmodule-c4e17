from flask import Flask, render_template
from mongoengine import StringField, IntField, BooleanField, Document
from models.customer import Customer
import mlab

app = Flask(__name__)
mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<g>')
def search(g):
    all_customer = Customer.objects(gender=g, status=False)
    return render_template('search.html', all_customer=all_customer)


if __name__ == '__main__':
  app.run(debug=True)
