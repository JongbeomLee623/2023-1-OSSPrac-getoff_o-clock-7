from flask import Flask, render_template, request
app = Flask(__name__)
db=[]


@app.route('/')
def input():
    return render_template('main.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=="POST":
        data = dict()
        data['name'] = request.form.get('name')
        data['StudentNumber'] = request.form.get('StudentNumber')
        data['major'] = request.form.get('major')
        data['email'] = request.form.get('email_id') + '@' + request.form.get('email_addr')
        data['gender'] = request.form.get('gender')
        data['Languages'] = request.form.getlist('Languages')
        if data not in db:
            db.append(data)
        db.sort(key=lambda x: x['StudentNumber'])
        return render_template('result.html', db = db)
    
    elif request.method=="GET":
        return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True,port=8000)
