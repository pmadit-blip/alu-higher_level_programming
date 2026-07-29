#!/usr/bin/python3
""" Doc
"""
from flask import Flask, Response, request, redirect, url_for
app = Flask(__name__)

@app.route("/catch_me", methods=['PUT'], strict_slashes=False)
def catch_me_1():
	if request.method == 'PUT':
		return redirect(url_for('catch_me_2'), code=307)
	else:
		res = Response("No")
		res.headers["Allow"] = "PUT"
		return res

@app.route("/catch_me_2", methods=['PUT'], strict_slashes=False)
def catch_me_2():
	if request.form.get("user_id") == "98":
		return redirect(url_for('catch_me_3'), code=307)
	else:
		return "You are not user_id = 98", 401

@app.route("/catch_me_3", methods=['PUT'], strict_slashes=False)
def catch_me_3():
	if request.headers.get('Origin') == "HolbertonSchool":
		return "You find me!"
	else:
		return "You are not coming from HolbertonSchool", 403


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
    
