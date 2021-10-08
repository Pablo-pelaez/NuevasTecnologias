from flask import Flask, app, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan')
def plan():
    return render_template('choose.html')    


if __name__ == "__main__":
    app.run(debug=True, port=3500)