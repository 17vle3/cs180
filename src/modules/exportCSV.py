#Takes the specified list of dictionaries and exports them to a CSV file
def exportList(fileName, projectList):
    fileLocation = "data/" + fileName + ".csv"

    #"w" here creates a new file with the filename. We overwrite the previous backup if one already exists with the same name
    csvFile = open(fileLocation, "w")

    #Write the header line before exporting the list 
    csvFile.write("ID,name,category,main_category,currency,deadline,goal,launched,pledged,state,backers,country,usd pledged,usd_pledged_real,usd_goal_real\n")

    for project in projectList:

        csvFile.write(project["id"] + "," + project["name"] + "," + project["category"] + "," + project["main_category"] + "," + project["currency"] + "," + project["deadline"] + "," + project["goal"] + "," + project["launched"] + "," + project["pledged"] + "," + project["state"] + "," + project["backers"] + "," + project["country"] + "," + project["usd_pledged"] + "," + project["usd_pledged_real"] + "," + project["usd_goal_real"] + "\n")

    csvFile.close()
    
    return