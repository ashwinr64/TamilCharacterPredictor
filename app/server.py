from flask import Flask, request, jsonify
from multiprocessing import Value
import base64
from flask_cors import CORS, cross_origin
from io import BytesIO
from flask import g

from fastai import *
from fastai.vision import *

import json


app = Flask(__name__)
CORS(app)

counter = Value('i', 0)


@app.route('/', methods=['POST'])
def hello():
    if 'learn' not in g:
        g.learn = load_learner(Path(__file__).parent, 'export.pkl')

    if 'classChar' not in g:
        with open(Path(__file__).parent/'classChar.json', 'r') as f:
            g.classChar = json.load(f)

    with counter.get_lock():
        counter.value += 1
        id = counter.value
    content = request.json

    # We don't need the first 30 chars ("data:image/octet-stream;base64,")
    imgObj = open_image(BytesIO(base64.b64decode(content['img'][31:])))
    prediction = g.learn.predict(imgObj)[0]

    data = {
        'id': str(id),
        'prediction': g.classChar[str(prediction)]
    }

    return jsonify(data)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
