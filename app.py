from flask import Flask, request, render_template
from flask_cors import cross_origin, CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
    return "NLP app running!!"


if __name__=='__main__':
    app.run(debug=True)
