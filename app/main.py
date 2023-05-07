from flask import Flask, render_template, request, redirect, url_for
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
        db.append(data)
        db.sort(key=lambda x: x['StudentNumber'])
        return render_template('result.html', db = db)
    elif request.method == 'GET':
        return render_template('result.html', db = db)

@app.route('/home')
def home():
    db.clear()
    return redirect('/')

@app.route('/', methods=['POST'])
def add_row():
    if request.method=='POST':
        data = dict()
        data['name'] = request.form.get('name')
        data['StudentNumber'] = request.form.get('StudentNumber')
        data['major'] = request.form.get('major')
        data['email'] = request.form.get('email_id')
        data['gender'] = request.form.get('gender')
        data['Languages'] = request.form.get('Languages')
        if data not in db:
            db.append(data)
        return render_template('result.html', db = db)
    
@app.route('/delete', methods=['GET','POST'])
def delete():
    action_btn = request.form.get('action_btn')
    if request.method == 'POST':
        if action_btn == 'delete_row':  
            selected_rows = request.form.getlist('delete')
            selected_rows = list(map(int, selected_rows))
            selected_rows.sort(reverse=True)
            for i in selected_rows:
               del db[i-1]
            return redirect('/result')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
