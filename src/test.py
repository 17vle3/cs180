import modules.importCSV as importCSV
import modules.exportCSV as exportCSV
import modules.search as search

projectList = importCSV.buildList("data/projects2.csv")
#exportCSV.exportList("backup", projectList)

print(search.search("SEK", "currency", projectList))

