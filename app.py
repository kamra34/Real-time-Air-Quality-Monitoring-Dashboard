from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect("air_quality_data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM measurements")
    data = cur.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    data = get_data()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
