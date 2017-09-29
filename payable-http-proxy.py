from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello world\n"

@app.route("/AmIBehindProxy")
def areyouaproxy():
	if "X-Forwarded-For" in request.headers:
		return "Behind a proxy\n"
	else:
		return "Not behind proxy\n"

if __name__ == '__main__':
	app.run(host="::", port=5000)