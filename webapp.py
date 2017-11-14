from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html', option = get_state_options())
    
@app.route("/fact", methods=['GET','POST'])
def get_fact():  
    menu = request.args['pickstate']
    return render_template('index.html', fact = funfact(menu), option = get_state_options())
    
with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)


def get_state_options(counties):
    options = ""
    for c in counties:
        options += Markup("<option value=\"" + counties["State"] + "\">" + counties["State"] + "</option>")
        
def funfact(state):
  fact = 0
    for c in counties:
        if state == c["State"]:
            fact += c["Miscellaneous"]["Percent Female"]
    return fact
        
        
if __name__=="__main__":
    app.run(debug=False, port=54321)

    