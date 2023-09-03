from flask import Flask, jsonify
import os
import uuid

app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
    #hostname = os.uname().nodename
    return jsonify({'hostname': os.uname().nodename}) # return jsonify(hostname=hostname / 'hostname' : hostname)

@app.route('/author', methods=['GET'])
def get_author():
    os.environ['AUTHOR'] = 'chursin_na'
    author = os.getenv('AUTHOR', 'default_author')
    return jsonify({'author': author})

@app.route('/id', methods=['GET'])
def get_id():
    my_uid = os.getenv('UID', str(uuid.uuid4()))
    return jsonify({'id': my_uid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
