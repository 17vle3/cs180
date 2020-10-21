from flask import Flask, jsonify, redirect, render_template, request, url_for
from modules import importCSV
from modules import search

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/projects", methods=['GET'])
def results():
    matches = search.search(request.args.get('keyword'), request.args.get('filter'), projectList)
    if not matches:
        return "No matches found :("
    return render_template('projects.html', matches=matches)
    #return jsonify(matches)

if __name__ == "__main__":
    projectList = importCSV.buildList('data/projects.csv')
    app.run()
