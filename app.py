from flask import Flask, render_template, jsonify, request
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

number_manakins = len(manakins)

@app.route('/')
def index():
    myhost = socket.gethostname()
    ip_address = socket.gethostbyname(myhost)
    return render_template('index.html', myhost=myhost, ip_address=ip_address, number_manakins=number_manakins)

@app.route("/api/v1/manakins")
def birds():
    return render_template("manakins.html", manakins=manakins, number_manakins=number_manakins)

@app.route("/api/v1/manakins/<int:id>")
def one_bird(id):
    
    if id >= number_manakins or id < 0:
        return '<h1>No such id</h1>'
    else:
        return render_template("manakin.html", manakins=manakins, id=id)
 
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
