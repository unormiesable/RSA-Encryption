from flask import Flask, redirect, url_for, render_template, request, jsonify
from helper.encryption import encrypt, decrypt
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
        
        return jsonify({
            'ciphertext': ciphertext,
            'pubkey': pubk,
            'privkey': privk
        })
    else:
        return render_template('index.html')
    
@app.route('/encrypt', methods=['POST'])
def encrypt_form():
    plaintext = request.form['plaintext']
    key1 = int(request.form['key1E'])
    key2 = int(request.form['key2E'])
    
    pubk, privk = generate_keypair(key1, key2)
    ciphertext = encrypt(pubk, plaintext)
    
    return jsonify({
            'ciphertext': ciphertext,
            'pubkey': pubk,
            'privkey': privk
    })

@app.route('/decrypt', methods=['POST'])
def decrypt_form():
    terenkripsi = request.form['terenkripsi']
    key1 = tuple(map(int, request.form['key1D'].split(',')))
    key2 = tuple(map(int, request.form['key2D'].split(',')))

    # Convert terenkripsi to a list of integers
    terenkripsi = list(map(int, terenkripsi.split(',')))

    print("Received terenkripsi:", terenkripsi)
    print("Received key1:", key1)
    print("Received key2:", key2)

    dekripsi = decrypt(key2, terenkripsi)
    
    print("Decrypted message:", dekripsi)

    return jsonify({
        'dekripsi': dekripsi
    })




@app.route('/github')
def github():
    return redirect("https://github.com/unormiesable/RSA-Encryption")

if __name__ == '__main__':
    app.run(debug=True)
