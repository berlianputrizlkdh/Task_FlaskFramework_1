from flask import Flask, render_template

app = Flask(__name__)

app_global = "Long Time No See"

#1.Membuat aplikasi Flask sederhana
@app.route("/")
def hello_world():
    return "<p>Hello, Semuanya, apa kabar! </p>"


#2.Route: Ubah URL nya (Web)
@app.route("/Web/")
def Web():
    return "<p>Percobaan Ubah URLnya! </p>"

#3.Route: Memakai HTML
@app.route("/HTML/")
def HTML():
    return render_template('about.html')

#4.Route: Memakai HTML dengan Boostrapp
@app.route("/Boostrapp/")
def Boostrapp():
    return render_template('boostrapp.html')

#5.Route: Memakai HTML dengan Static
@app.route("/Static/")
def Static():
    return render_template('static.html')

#6.Route: Dinamis
@app.route("/nim/<Nim_Mahasiswa>/")
def getnama(Nim_Mahasiswa):
    return "NIM anda {}".format(Nim_Mahasiswa)

#7.Route: ID
@app.route('/user/<string:user_id>')
def user_id(user_id):
    return f"User ID: {user_id}"

#8.Route: Memakai Variabel Global
@app.route('/VariabelGlobal/')
def variabel_global():
    return f"Welcome!, {app_global}"

#9.Route: Variabel Dictionary
@app.route('/Dicti')
def Dicti():
    user = {"name": "Icsyy", "age": 18, "city": "Surabaya"}
    return render_template('dictionary.html', user=user)

#1. Coba-coba route id dgn v. global
# variabel global
nama_kampus = "Nice to Meet You" 

@app.route("/mahasiswa/<string:id>/")
def get_mahasiswa(id):
    return f"{nama_kampus} {id}"


if __name__ == "__main__":
    app.run(debug=True)

