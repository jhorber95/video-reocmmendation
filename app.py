from flask import Flask, jsonify
import turicreate as tc

model = tc.load_model("recommendation.model")

app = Flask(__name__)


@app.route('/recommend')
def recommends():
    r = model.recommend()
    return jsonify(list(r))


@app.route('/custom-recommend/<:user>')
def make_custom_recommend(user):
    r = model.recommend(users=[user])
    return jsonify(list(r))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
