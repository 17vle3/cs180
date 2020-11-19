import time
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash
from modules import importCSV
from modules import exportCSV
from modules import search
from modules import analytics

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/projects", methods=['GET'])
def results():
    
    matches = search.search(request.args.get('keyword'), request.args.get('filter'), projectList)
    if not matches:
        return render_template('matchError.html')
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

        if cachedStats["countryStats"] !=  "Empty":
            countryToUpdate = newProject["country"]
            cachedStats["countryStats"][countryToUpdate] += 1

        if cachedStats["categoryStats"] !=  "Empty":
            categoryToUpdate = newProject["category"]
            cachedStats["categoryStats"][categoryToUpdate] += 1

    return render_template('insert.html')

@app.route("/backup", methods=['GET'])
def backup():
    fileName = "backup_" + time.strftime("%m-%d-%Y")
    exportCSV.exportList(fileName, projectList)
    return render_template('backup.html')

@app.route("/delete/<string:id>")
def delete(id):
    for i in range(len(projectList)): 
        if projectList[i]['id'] == id:
            if cachedStats["countryStats"] !=  "Empty":
                countryToUpdate = projectList[i]["country"]
                cachedStats["countryStats"][countryToUpdate] -= 1 
            if cachedStats["categoryStats"] !=  "Empty":
                categoryToUpdate = projectList[i]["category"]
                cachedStats["categoryStats"][categoryToUpdate] -= 1

            del projectList[i] 
            break
    return redirect('/')

@app.route("/update/<string:id>", methods=['POST'])
def update(id):
    for i in range(len(projectList)): 
        if projectList[i]['id'] == id:
            projectList[i]["name"] = request.form["name"]
            if cachedStats["categoryStats"] !=  "Empty":
                categoryToUpdate = projectList[i]["category"]
                cachedStats["categoryStats"][categoryToUpdate] -= 1 
            projectList[i]["category"] = request.form["category"]
            if cachedStats["categoryStats"] !=  "Empty":
                categoryToUpdate = projectList[i]["category"]
                cachedStats["categoryStats"][categoryToUpdate] += 1
            projectList[i]["main_category"] = request.form["main_category"]
            projectList[i]["currency"] = request.form["currency"]
            projectList[i]["deadline"] = request.form["deadline"]
            projectList[i]["goal"] = request.form["goal"]
            projectList[i]["launched"] = request.form["launched"]
            projectList[i]["pledged"] = request.form["pledged"]
            projectList[i]["state"] = request.form["state"]
            projectList[i]["backers"] = request.form["backers"]
            if cachedStats["countryStats"] !=  "Empty":
                countryToUpdate = projectList[i]["country"]
                cachedStats["countryStats"][countryToUpdate] -= 1 
            projectList[i]["country"] = request.form["country"]
            if cachedStats["countryStats"] !=  "Empty":
                countryToUpdate = projectList[i]["country"]
                cachedStats["countryStats"][countryToUpdate] += 1
            projectList[i]["usd_pledged"] = request.form["usd_pledged"]
            projectList[i]["usd_pledged_real"] = request.form["usd_pledged_real"]
            projectList[i]["usd_goal_real"] = request.form["usd_goal_real"]
    return redirect('/')

@app.route("/countryStats")
def countryStats():
    start = time.time()
    #If we don't have the stats cached, then this is our first time loading this page. That means we will calculate the results and save them.
    #If we already have the stats cached, we just use those instead of recalculating everything. 
    if cachedStats["countryStats"] ==  "Empty":
        cachedStats["countryStats"] = analytics.getCountryStats(projectList)
    print("--- %s seconds ---" % (time.time() - start))
    return render_template('countryStats.html', countryValues=cachedStats["countryStats"].values(), countryNames=cachedStats["countryStats"].keys(), chartName="Country Statistics")

@app.route("/categoryStats")
def categoryStats():
    #If we don't have the stats cached, then this is our first time loading this page. That means we will calculate the results and save them.
    #If we already have the stats cached, we just use those instead of recalculating everything. 
    if cachedStats["categoryStats"] ==  "Empty":
        cachedStats["categoryStats"] = analytics.getCategoryStats(projectList)
    return render_template('categoryStats.html', categoryValues=cachedStats["categoryStats"].values(), categoryNames=cachedStats["categoryStats"].keys(), chartName="Category Statistics")

@app.route("/deadlineStats")
def deadlineStats():
    deadlineStats = analytics.getDeadlineStats(projectList)
    return render_template('deadlineStats.html', deadlineValues=deadlineStats.values(), deadlineNames=deadlineStats.keys(), chartName="Deadline Statistics")

@app.route("/mostSuccessfulCategoryStats")
def mostSuccessfulCategoryStats():
    mostSuccessfulCategoryStats = analytics.getMostSuccessfulCategoryStats(projectList)
    return render_template('mostSuccessfulCategoryStats.html', mostSuccessfulCategoryValues=mostSuccessfulCategoryStats.values(), mostSuccessfulCategoryNames=mostSuccessfulCategoryStats.keys(), chartName="Most Successful Statistics")

@app.route("/failedTakeoffStats")
def failedTakeoffStats():
    failedTakeoffStats = analytics.getFailedTakeoffStats(projectList)
    return render_template('failedTakeoffStats.html', categoryValues=failedTakeoffStats.values(), categoryNames=failedTakeoffStats.keys(), chartName="Failed Takeoff Statistics")

@app.route("/fundingVersusSuccessStats")
def fundingVersusSuccessStats():
    fundingVersusSuccessStats = analytics.getFundingVersusSuccessStats(projectList)
    return render_template('fundingVersusSuccessStats.html', fundingVersusSuccessValues=fundingVersusSuccessStats.values(), fundingVersusSuccessNames=fundingVersusSuccessStats.keys(), chartName="Funding Versus Success Statistics")

if __name__ == "__main__":
    projectList = importCSV.buildList('data/projects_clean.csv')
    cachedStats = {
        "countryStats": "Empty",
        "categoryStats": "Empty"
    }
    app.run()
