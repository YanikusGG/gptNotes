from flask import Flask, make_response

PORT = 8080

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    response = make_response('gptNotes alive!', 200)
    return response


def main():
    app.run(port=PORT, debug=True)


if __name__ == '__main__':
    main()
