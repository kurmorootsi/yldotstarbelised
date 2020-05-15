from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "vhost79961s2"
app.config["MYSQL_USER"] = "vhost79961s2"
app.config["MYSQL_PASSWORD"] = "Sapakas123"

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        tunni_teema = request.form["tunni_teema"]
        aine = request.form["aine"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ainetund (aine, tunni_teema) VALUES (%s, %s)", (aine, tunni_teema))
        mysql.connection.commit()
        return redirect(url_for("Index"))


if __name__ == '__main__':
    app.run()
