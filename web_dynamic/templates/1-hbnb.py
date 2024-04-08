# 1-hbnb.py
from flask import Flask, render_template
import uuid

app = Flask(__name__)


@app.route('/1-hbnb/')
def hbnb():
    return render_template('1-hbnb.html', cache_id=uuid.uuid4())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
