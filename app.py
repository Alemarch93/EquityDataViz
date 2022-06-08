import json
from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def graph():
    default_value = 'TSLA'
    ticker = request.form.get('ticker', default_value)

    if ticker:
        ticker = yf.Ticker(ticker)
        data = ticker.history(period='2y', interval='1d', auto_adjust=True,
                              prepost=False)
        df = pd.DataFrame(data)
        labels = [str(d)[:10] for d in df.index]
        values = df['Close'].apply(lambda x: round(x, 4)).tolist()
        vol = df['Volume'].to_list()
        print (labels)
        print(values)

    return render_template('chart.html',labels = labels, values=values, vol=vol )


if __name__ == '__main__':
    app.run(debug=True)
