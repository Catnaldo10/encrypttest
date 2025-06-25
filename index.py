from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

clients = []


@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    encrypted_msg = data.get('msg')
    emit('message', encrypted_msg, broadcast=True, namespace='/')
    return jsonify({'status': 'sent'})

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    print("[!] Fernet Key:", fernet_key.decode())
    socketio.run(app, host='0.0.0.0', port=5000)
