# flask needs app.py to run

from flask import *
from whitenoise import WhiteNoise  # treat like black box

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app,
                          root='static/',
                          prefix='static/',
                          index_file="index.htm",
                          autorefresh=True)  # plug into flask something to help us send files, needs root and prefix


@app.route('/', methods=['GET'])
# people can get data, can not send data to endpoint
def hello():
    return make_response("Hello, world!!!")


if __name__ == "__main__":
    app.run(threaded=True, port=500)
