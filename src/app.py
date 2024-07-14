#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST" id="inputForm">
         <input name="user_input" id="userInput">
         <input type="submit" value="Submit!">
     </form>
     <br>
     <label for="updatedField">Updated Field:</label>
     <input type="text" id="updatedField" readonly>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return '''
     <form action="/echo_user_input" method="POST" id="inputForm">
         <input name="user_input" id="userInput">
         <input type="submit" value="Submit!">
     </form>
     <br>
     <label for="updatedField">Updated Field:</label>
     <input type="text" id="updatedField" value="{}" readonly>
     '''.format(input_text)