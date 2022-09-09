from turtle import title
from flask import Flask,render_template,redirect,url_for
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("..\leut.csv")
df.to_csv("leut.csv",index=None)

df1 = pd.read_csv("..\walle.csv")
df1.to_csv("walle.csv", index=None)


@app.route('/')
def csvtohtml():
    data = pd.read_csv("leut.csv")

    return render_template("index.html",tables=[data.to_html()],titles=[''])

if __name__ == "__main__":
    app.run(host="localhost",port=int(5000))