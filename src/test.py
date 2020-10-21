import modules.importCSV as importCSV
import modules.search as search

projectList = importCSV.buildList("data/projects.csv")

searchTerm = 'DE'
searchFilter = 'country'

print(search.search(searchTerm, searchFilter, projectList))