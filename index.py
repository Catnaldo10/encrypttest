from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Danh sách tin nhắn lưu trong RAM
messages = []

@app.route('/', methods=['GET'])
def home():
    return 'REST API chat server is running.'

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    ip = data.get('ip')
    content = data.get('content')

    if not ip or not content:
        return jsonify({'error': 'Missing ip or content'}), 400

    msg = {
        'ip': ip,
        'content': content,
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }
    messages.append(msg)
    return jsonify({'status': 'sent', 'message': msg}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
