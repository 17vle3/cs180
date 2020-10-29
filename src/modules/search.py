#Takes in the projectList (list of project dictionaries). Returns either one project(unique ID) or a list of matches for the search term
def search(searchTerm, searchFilter, projectList):
    if searchFilter == 'id' : #for ID searches, there can only be one, so
        for project in projectList:
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
    else: #for other types of searches
        matches = list(filter(lambda project: project[searchFilter].lower()==(searchTerm.lower())  , projectList))
        if not matches:
            return None
        return matches
