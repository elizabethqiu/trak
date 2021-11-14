from flask import Flask, render_template

app = Flask(__name__)


# Entry point and function
@app.route('/')
def index():
    return render_template('index.html')


# Run web server and app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')