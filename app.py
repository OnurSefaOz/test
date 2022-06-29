from flask import Flask

app = Flask(__name__)


@app.route('/payment_type', methods=['POST'])
def payment_type():
    return {"response": "a"}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')