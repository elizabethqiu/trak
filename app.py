import json
from flask import Flask, render_template, request
from send_sms import *

app = Flask(__name__)


# Entry point and function
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def update_record():
    # print(request.data)
    # print(request.form)
    name = request.form['name']
    phone_number = request.form['phone_number']
    text_user(phone_number, name)
    text_user_prepare(phone_number, name)
    text_user_arrive(phone_number, name)
    return render_template('screen2.html')
    # record = json.loads(request.data)
    # new_records = []
    # with open('/tmp/data.txt', 'r') as f:
    #     data = f.read()
    #     records = json.loads(data)
    # for r in records:
    #     if r['name'] == record['name']:
    #         r['phone_number'] = record['phone_number']
    #     new_records.append(r)
    # with open('/tmp/data.txt', 'w') as f:
    #     f.write(json.dumps(new_records, indent=2))
    # return jsonify(record)
    # print(record)


# Run web server and app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')