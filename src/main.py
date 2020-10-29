import time
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash
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

@app.route("/insert", methods=['POST'])
def insert():
    if request.method == 'POST':
        newProject = {
            "id": request.form["id"], 
            "name": request.form["name"], 
            "category": request.form["category"],
            "main_category": request.form["main_category"],
            "currency": request.form["currency"],
            "deadline": request.form["deadline"],
            "goal": request.form["goal"],
            "launched": request.form["launched"],
            "pledged": request.form["pledged"],
            "state": request.form["state"],
            "backers": request.form["backers"],
            "country": request.form["country"],
            "usd_pledged": request.form["usd_pledged"],
            "usd_pledged_real": request.form["usd_pledged_real"],
            "usd_goal_real": request.form["usd_goal_real"]
        }
        projectList.append(newProject)
    return render_template('insert.html')

@app.route("/backup", methods=['GET'])
def backup():
    filename = "backup_" + time.strftime("%m-%d-%Y")
    exportCSV.exportList(filename, projectList)
    return render_template('backup.html')

@app.route("/delete/<string:id>")
def delete(id):
    for i in range(len(projectList)): 
        if projectList[i]['id'] == id: 
            del projectList[i] 
            break
    return redirect('/')

@app.route("/update/<string:id>", methods=['POST'])
def update(id):
    for i in range(len(projectList)): 
        if projectList[i]['id'] == id:
            projectList[i]["name"] = request.form["name"] 
            projectList[i]["category"] = request.form["category"]
            projectList[i]["main_category"] = request.form["main_category"]
            projectList[i]["currency"] = request.form["currency"]
            projectList[i]["deadline"] = request.form["deadline"]
            projectList[i]["goal"] = request.form["goal"]
            projectList[i]["launched"] = request.form["launched"]
            projectList[i]["pledged"] = request.form["pledged"]
            projectList[i]["state"] = request.form["state"]
            projectList[i]["backers"] = request.form["backers"]
            projectList[i]["country"] = request.form["country"]
            projectList[i]["usd_pledged"] = request.form["usd_pledged"]
            projectList[i]["usd_pledged_real"] = request.form["usd_pledged_real"]
            projectList[i]["usd_goal_real"] = request.form["usd_goal_real"]
    return redirect('/')

if __name__ == "__main__":
    projectList = importCSV.buildList('data/projects_clean.csv')
    app.run()
