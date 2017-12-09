from flask import Flask, request
from Crypto import Random
from Crypto.Cipher import AES
import base64

KEY = '0123456789abcdef'

IV = Random.new().read(AES.block_size)

APP = Flask(__name__)

@APP.route('/')
def main():
    with open('index.html') as index:
        return index.read()

@APP.route('/encrypt', methods=['POST'])
def encrypt():
    aes = AES.new(KEY, AES.MODE_CFB, IV)
    return base64.urlsafe_b64encode(aes.encrypt(request.data))

@APP.route('/decrypt', methods=['POST'])
def decrypt():
    aes = AES.new(KEY, AES.MODE_CFB, IV)
    return aes.decrypt(base64.urlsafe_b64decode(request.data))

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
