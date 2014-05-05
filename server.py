from flask import *
from subprocess import Popen
import os, signal
app = Flask(__name__)

def restart():
	if app.config.has_key('pid'):
		os.kill(app.config['pid'], signal.SIGTERM)
	p = Popen("./runserver.sh")
	app.config['pid'] = p.pid

@app.route("/", methods=['POST', 'GET'])
def receive():
	if request.method == 'POST':
		restart()
		return ""
	else:
		return "Hello"

if __name__ == "__main__":
	# app.debug = True
	restart()
	app.run()
