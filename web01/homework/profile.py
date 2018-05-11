from flask import Flask, render_template
app = Flask(__name__)


@app.route('/users/<username>')
def profile(username):
    users = {
'tung':{ 
    'name': 'Tung',
    'age': '17',
    'status': 'single',
    'hobbies': 'masturbate',
},
'dung':{
    'nane': 'Van Dung',
    'age': '19',
    'status': 'single',
    'hobbies': 'masturbate',
},
'hoang':{
    'name': 'Nguyen Hoang',
    'age': '15',
    'status': 'single',
    'hobbies': 'masturbate',
},

    }
    if username in users.keys():
        return render_template('index2.html', users= users[username])
    else:
        return render_template('index3.html', users= username)
    
if __name__ == '__main__':
  app.run(debug=True)
 
