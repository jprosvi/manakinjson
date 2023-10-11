from flask import Flask, render_template, jsonify
import socket

app = Flask(__name__)

manakins = [
    {
        "commonName": "Long-tailed Manakin",
        "scientificName": "Chiroxiphia linearis",
    },
    {
        "commonName": "Red-capped Manakin",
        "scientificName": "Ceratopipra mentalis",
    },
    {
        "commonName": "White-collared Manakin",
        "scientificName": "Manacus candei",
    },
    {
        "commonName": "Orange-collared Manakin",
        "scientificName": "Manacus aurantiacus",
    },
    {
        "commonName": "Blue-crowned Manakin",
        "scientificName": "Lepidothrix coronata",
    }
]

@app.route('/')
def index():
    myhost = socket.gethostname()
    ip_address = socket.gethostbyname(myhost)
    return render_template('index.html', myhost=myhost, ip_address=ip_address)

@app.route("/api/v1/manakins")
def birds():
    return jsonify(manakins)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
