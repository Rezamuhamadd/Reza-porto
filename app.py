from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__, static_url_path='/static')
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)