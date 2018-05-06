from flask import Flask

from flask import render_template,request

app = Flask(__name__, template_folder='template') 

@app.route('/')

def mypysite(name=None):

	return render_template('index.html')

if __name__ == "__main__":
	app.debug = True
	app.run('192.168.0.101')


