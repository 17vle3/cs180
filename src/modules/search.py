#Takes in the projectList (list of project dictionaries). Returns either one project(unique ID) or a list of matches for the search term
def search(searchTerm, searchFilter, projectList):
    if searchFilter == 'id':
        for project in projectList:
            if project[searchFilter] == searchTerm:
                return project

    else:
        matches = list(filter(lambda project: project[searchFilter] == searchTerm, projectList))
        if not matches:
            return None
        return matches
