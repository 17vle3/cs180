#Takes in the projectList (list of project dictionaries). Returns either one project(unique ID) or a list of matches for the search term. Name searches can include substrings and are case insensitive
def search(searchTerm, searchFilter, projectList):
    if searchFilter == 'id':
        for project in projectList:
            #Immediately return the match instead of searching the rest of the list
            if project[searchFilter] == searchTerm:
                matches = []
                matches.append(project)
                return matches
    elif searchFilter == 'name':
        matches = []
        for project in projectList:
            if searchTerm.lower() in project[searchFilter].lower():
                matches.append(project)
        return matches
    else:
        matches = list(filter(lambda project: project[searchFilter].lower()==(searchTerm.lower())  , projectList))
        if not matches:
            return None
        return matches
