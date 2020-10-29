import time
from flask import Flask, jsonify, redirect, render_template, request, url_for
from modules import importCSV
from modules import exportCSV
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

@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        return "Thanks for adding a project!"
    return render_template('insert.html')

@app.route("/backup", methods=['GET'])
def backup():
    filename = "backup_" + time.strftime("%m-%d-%Y")
    exportCSV.exportList(filename, projectList)
    return render_template('backup.html')

if __name__ == "__main__":
    projectList = importCSV.buildList('data/projects_clean.csv')
    app.run()
