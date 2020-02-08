from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return  render_template('body.html')# 'Hello World'

@app.route('/CS127')
def cs127():
	return jsonify({"message":"flask is cool!"})





if __name__ == '__main__':
   app.run(debug=True)

