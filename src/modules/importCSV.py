#Takes in a row of the csv_file and returns a dictionary of the project's data
def importProject(row):
    #Strip all extra whitespace, split the row by commas and add each piece of data into a list.
    row = row.strip().split(',')

    #Python dictionary https://www.w3schools.com/python/python_dictionaries.asp
    project = {
        'id': row[0],
        'name': row[1],
        'category': row[2],
        'main_category': row[3],
        'currency': row[4],
        'deadline': row[5],
        'goal': row[6],
        'launched': row[7],
        'pledged': row[8],
        'state': row[9],
        'backers': row[10],
        'country': row[11],
        'usd_pledged': row[12],
        'usd_pledged_real': row[13],
        'usd_goal_real': row[14]
    }

    return project

#Takes the specified CSV file and builds a list of project dictionaries 
def buildList(fileName):
    csvFile = open(fileName, encoding='utf-8')
    #Skip the header line before building the list 
    next(csvFile)

    #Python list https://www.w3schools.com/python/python_lists.asp
    projectList = []

    for row in csvFile:
        project = importProject(row)
        projectList.append(project)

    csvFile.close()
    
    return projectList