from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def input():
    return render_template('main.html')

@app.route('/result',methods=['GET','POST'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True,port=8000)
