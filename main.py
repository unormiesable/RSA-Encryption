from flask import Flask, redirect, url_for, render_template, request, jsonify
from helper.encryption import encrypt
from helper.calculation import generate_keypair

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key1 = int(request.form['key1E'])
        key2 = int(request.form['key2E'])
        
        pubk, privk = generate_keypair(key1, key2)
        ciphertext = encrypt(pubk, plaintext)
        
        return jsonify({'ciphertext': ciphertext})
    else:
        return render_template('index.html')
    
@app.route('/encrypt', methods=['POST'])
def encrypt_form():
    plaintext = request.form['plaintext']
    key1 = int(request.form['key1E'])
    key2 = int(request.form['key2E'])
    
    pubk, privk = generate_keypair(key1, key2)
    ciphertext = encrypt(pubk, plaintext)
    
    return jsonify({'ciphertext': ciphertext})

@app.route('/github')
def github():
    return redirect("https://github.com/unormiesable/RSA-Encryption")

if __name__ == '__main__':
    app.run(debug=True)
