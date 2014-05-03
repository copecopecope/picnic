from flask import *
from subprocess import call
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def receive():
	if request.method == 'POST':
		call(["./script.sh"], shell=True)
		return True
	else:
		return "Hellos"

if __name__ == "__main__":
	app.debug = True
	app.run()