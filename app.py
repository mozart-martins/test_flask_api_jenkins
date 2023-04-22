"""
  API para retornar a data de hoje.
"""
import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/today')
def time():
    """
        Metodo que retorna a data de hoje.
    """
    return str(datetime.datetime.today())


if __name__ == '__main__':
    app.run(port=8888)
