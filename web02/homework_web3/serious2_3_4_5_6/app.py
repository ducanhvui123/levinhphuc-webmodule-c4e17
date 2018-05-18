from flask import Flask, render_template, request, redirect, url_for
from models.collection import Service
import mlab

mlab.connect()
app = Flask(__name__)


@app.route('/service')
def service():
    service_list = Service.objects()  
    return render_template('service.html', service_list=service_list)


@app.route('/detail/<user_id>')
def detail(user_id):
    service_dict = Service.objects.with_id(user_id)
    return render_template('detail.html', item=service_dict)


@app.route('/add', methods=['POST', 'GET'])  
def add():
    if request.method == 'GET':  
        return render_template('add.html')
    elif request.method == 'POST':
        form = request.form  

        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == 'male':
            gender = 1
        else:
            gender = 0

        new_service = Service(name=name, yob=yob, phone=phone, gender=gender)
        new_service.save()

        return redirect(url_for('service'))


@app.route('/update/<user_id>', methods=['POST', 'GET'])
def update(user_id):
    
    service_dict = Service.objects.with_id(user_id)
    if request.method == 'GET':
        return render_template('update.html', item=service_dict)
    elif request.method == 'POST':
        service_list = Service.objects(id=user_id)
        form = request.form

        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == 'male':
            gender = 1
        else:
            gender = 0

        service_list.update(set__name=name,  
                            set__yob=yob,
                            set__phone=phone,
                            set__gender=gender)

    
        return 'update successful'


if __name__ == '__main__':
  app.run(debug=True)
