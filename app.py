from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

@app.route("/books")
def books():
    df = pd.read_csv('books.csv')
    df['cover'] = df['cover'].fillna('')
    data = df.to_dict('records')

    return render_template('books.html', books=data)
