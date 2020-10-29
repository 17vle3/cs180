#Takes the specified list of dictionaries and exports them to a CSV file
def exportList(filename, projectList):
    file_location = "data/" + filename + ".csv"

    #"x" here creates a new file with the filename. We get an error if the file already exists that way we don't overwrite a previous backup
    csv_file = open(file_location, "w")

    #Write the header line before exporting the list 
    csv_file.write("ID,name,category,main_category,currency,deadline,goal,launched,pledged,state,backers,country,usd pledged,usd_pledged_real,usd_goal_real\n")

    for project in projectList:

        csv_file.write(project["id"] + "," + project["name"] + "," + project["category"] + "," + project["main_category"] + "," + project["currency"] + "," + project["deadline"] + "," + project["goal"] + "," + project["launched"] + "," + project["pledged"] + "," + project["state"] + "," + project["backers"] + "," + project["country"] + "," + project["usd_pledged"] + "," + project["usd_pledged_real"] + "," + project["usd_goal_real"] + "\n")

    csv_file.close()
    
    return