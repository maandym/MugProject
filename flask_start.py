from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/hello/')
def hello():
    msg="Satvik"
    return render_template('hello.html', msg=msg)

if __name__=='__main__':
    app.run(debug=True,port=8000)