from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image46')
def image46():
    return render_template('image46.html')

@app.route('/image136')
def image136():
    return render_template('image136.html')

@app.route('/image262')
def image262():
    return render_template('image262.html')

@app.route('/image2')
def image2():
    return render_template('image2.html')

@app.route('/video932')
def video932():
    return render_template('video932.html')

@app.route('/video40')
def video40():
    return render_template('video40.html')

@app.route('/backend')
def backend():
    return render_template('backend.html')

@app.route('/long_request')
def long_request():
    import time
    time.sleep(60)
    return "this is the result of a long request"

@app.route('/short_request')
def short_request():
    import time
    time.sleep(10)
    return "this is the result of a short request"

if __name__ == '__main__':
    app.run(debug=True)