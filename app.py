from flask import Flask, render_template, request
import fungsipertama as fsatu
import fungsikedua as fdua
import fungsiketiga as ftiga

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index() :
    if request.method == 'POST':
        msg = request.form['text']
        fitur = request.form['fitur']
        if fitur == "1":
            satu = fsatu.fungsipertama(msg)
            return render_template("index.html", satu = satu, msg = msg)
        elif fitur == "2":
            dua = fdua.fungsikedua(msg)
            return render_template("index.html", dua = dua, msg = msg)
        elif fitur == "3":
            tiga = ftiga.fungsiketiga(msg)
            return render_template("index.html", tiga = tiga, msg = msg)
        # return fitur
    else:
        return render_template("index.html")

@app.route("/team")
def team() :
    return render_template("team.html")

if __name__ == "__main__" :
    app.run(debug=True)