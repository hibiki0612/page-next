
from flask import Flask,request
from flask.templating import render_template
from servo import servo_back, servo_next,servo_go,auto_servo

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/index')
def index():
    servo_next()
    return render_template('index.html')

@app.route('/select',methods=["GET"])
def select():
    return render_template('select.html')

@app.route('/one_page',methods=["GET"])
def one_page():
    return render_template('one_page.html')

@app.route('/one_page_go',methods=["GET"])
def one_page_go():
    servo_go()
    return render_template('one_page.html')

@app.route('/one_page_back',methods=["GET"])
def one_page_back():
    servo_back()
    return render_template('one_page.html')

@app.route('/auto',methods=["GET"])
def auto():
    return render_template('auto.html')

@app.route('/auto',methods=['POST'])
def form():

    list_datas = request.form.getlist('list_data')
    auto_servo(int(list_datas[0]))

    return render_template('auto.html',title='flask入門',message='flask入門へようこそ',data = [list_datas])
    
    
@app.route('/stop',methods=["GET"])
def stop():
    return render_template('stop.html')

@app.route('/end',methods=["GET"])
def end():
    return render_template('end.html')

app.run(port=8000, debug=True)