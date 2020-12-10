from modules import search
from datetime import datetime

def getCountryStats(projectList):

    countryStats = {
        "AU": 0,
        "BE": 0,
        "CA": 0,
        "CH": 0,
        "DE": 0,
        "DK": 0,
        "ES": 0,
        "FR": 0,
        "GB": 0,
        "HK": 0,
        "IE": 0,
        "IT": 0,
        "JP": 0,
        "LU": 0,
        "MX": 0,
        "NL": 0,
        "NO": 0,
        "NZ": 0,
        "SE": 0,
        "SG": 0,
        "UNK": 0,
        "US": 0
    }

    for project in projectList:
        #Australia
        if project['country'] == "AU":
            countryStats["AU"] += 1
        #Belgium
        elif project['country'] == "BE":
            countryStats["BE"] += 1
        #Canada
        elif project['country'] == "CA":
            countryStats["CA"] += 1
        #China
        elif project['country'] == "CH":
            countryStats["CH"] += 1
        #Germany
        elif project['country'] == "DE":
            countryStats["DE"] += 1
        #Denmark
        elif project['country'] == "DK":
            countryStats["DK"] += 1
        #Spain
        elif project['country'] == "ES":
            countryStats["ES"] += 1
        #France
        elif project['country'] == "FR":
            countryStats["FR"] += 1
        #Great Britain
        elif project['country'] == "GB":
            countryStats["GB"] += 1
        #Hong Kong
        elif project['country'] == "HK":
            countryStats["HK"] += 1
        #Ireland
        elif project['country'] == "IE":
            countryStats["IE"] += 1
        #Italy
        elif project['country'] == "IT":
            countryStats["IT"] += 1
        #Japan
        elif project['country'] == "JP":
            countryStats["JP"] += 1
        #Luxembourg
        elif project['country'] == "LU":
            countryStats["LU"] += 1
        #Mexico
        elif project['country'] == "MX":
            countryStats["MX"] += 1
        #Netherlands
        elif project['country'] == "NL":
            countryStats["NL"] += 1
        #Norway
        elif project['country'] == "NO":
            countryStats["NO"] += 1
        #New Zealand
        elif project['country'] == "NZ":
            countryStats["NZ"] += 1
        #Sweden
        elif project['country'] == "SE":
            countryStats["SE"] += 1
        #Singapore
        elif project['country'] == "SG":
            countryStats["SG"] += 1
        #Unknown
        elif project['country'] == "UNK":
            countryStats["UNK"] += 1
        #United States
        elif project['country'] == "US":
            countryStats["US"] += 1
    return countryStats

def getCategoryStats(projectList):

    categoryStats = {
        "Comics": 0,
        "Crafts": 0,
        "Dance": 0,
        "Fashion": 0,
        #Amperstand (&) is weird on graph so we manually spell it out
        "Film and Video": 0,
        "Food": 0,
        "Journalism": 0,
        "Games": 0,
        "Music": 0,
        "Photography": 0,
        "Publishing": 0,
        "Technology": 0,
        "Theater": 0
    }
    
    for project in projectList:
        if project['main_category'] == "Comics":
            categoryStats["Comics"] += 1

        elif project['main_category'] == "Crafts":
            categoryStats["Crafts"] += 1

        elif project['main_category'] == "Dance":
            categoryStats["Dance"] += 1

        elif project['main_category'] == "Fashion":
            categoryStats["Fashion"] += 1

        elif project['main_category'] == "Film & Video":
            categoryStats["Film and Video"] += 1

        elif project['main_category'] == "Food":
            categoryStats["Food"] += 1

        elif project['main_category'] == "Journalism":
            categoryStats["Journalism"] += 1

        elif project['main_category'] == "Games":
            categoryStats["Games"] += 1

        elif project['main_category'] == "Music":
            categoryStats["Music"] += 1

        elif project['main_category'] == "Photography":
            categoryStats["Photography"] += 1

        elif project['main_category'] == "Publishing":
            categoryStats["Publishing"] += 1

        elif project['main_category'] == "Technology":
            categoryStats["Technology"] += 1
            
        elif project['main_category'] == "Theater":
            categoryStats["Theater"] += 1        

    return categoryStats

def getFailedTakeoffStats(projectList):
    zeroBackersList = (search.search("0", "backers", projectList))

    failedTakeoffStats = {
        "Comics": 0,
        "Crafts": 0,
        "Dance": 0,
        "Fashion": 0,
        #Amperstand (&) is weird on graph so we manually spell it out
        "Film and Video": 0,
        "Food": 0,
        "Journalism": 0,
        "Games": 0,
        "Music": 0,
        "Photography": 0,
        "Publishing": 0,
        "Technology": 0,
        "Theater": 0
    }
    
    for project in zeroBackersList:
        if project['main_category'] == "Comics":
            failedTakeoffStats["Comics"] += 1

        elif project['main_category'] == "Crafts":
            failedTakeoffStats["Crafts"] += 1

        elif project['main_category'] == "Dance":
            failedTakeoffStats["Dance"] += 1

        elif project['main_category'] == "Fashion":
            failedTakeoffStats["Fashion"] += 1

        elif project['main_category'] == "Film & Video":
            failedTakeoffStats["Film and Video"] += 1

        elif project['main_category'] == "Food":
            failedTakeoffStats["Food"] += 1

        elif project['main_category'] == "Journalism":
            failedTakeoffStats["Journalism"] += 1

        elif project['main_category'] == "Games":
            failedTakeoffStats["Games"] += 1

        elif project['main_category'] == "Music":
            failedTakeoffStats["Music"] += 1

        elif project['main_category'] == "Photography":
            failedTakeoffStats["Photography"] += 1

        elif project['main_category'] == "Publishing":
            failedTakeoffStats["Publishing"] += 1

        elif project['main_category'] == "Technology":
            failedTakeoffStats["Technology"] += 1

        elif project['main_category'] == "Theater":
            failedTakeoffStats["Theater"] += 1        

    return failedTakeoffStats

def getMostSuccessfulCategoryStats(projectList):
    successfulStateList = (search.search("successful", "state", projectList))

    mostSuccessfulStats = {
        "Comics": 0,
        "Crafts": 0,
        "Dance": 0,
        "Fashion": 0,
        #Amperstand (&) is weird on graph so we manually spell it out
        "Film and Video": 0,
        "Food": 0,
        "Journalism": 0,
        "Games": 0,
        "Music": 0,
        "Photography": 0,
        "Publishing": 0,
        "Technology": 0,
        "Theater": 0
    }
    
    for project in successfulStateList:
        if project['main_category'] == "Comics":
            mostSuccessfulStats["Comics"] += 1

        elif project['main_category'] == "Crafts":
            mostSuccessfulStats["Crafts"] += 1

        elif project['main_category'] == "Dance":
            mostSuccessfulStats["Dance"] += 1

        elif project['main_category'] == "Fashion":
            mostSuccessfulStats["Fashion"] += 1

        elif project['main_category'] == "Film & Video":
            mostSuccessfulStats["Film and Video"] += 1

        elif project['main_category'] == "Food":
            mostSuccessfulStats["Food"] += 1

        elif project['main_category'] == "Journalism":
            mostSuccessfulStats["Journalism"] += 1

        elif project['main_category'] == "Games":
            mostSuccessfulStats["Games"] += 1

        elif project['main_category'] == "Music":
            mostSuccessfulStats["Music"] += 1

        elif project['main_category'] == "Photography":
            mostSuccessfulStats["Photography"] += 1

        elif project['main_category'] == "Publishing":
            mostSuccessfulStats["Publishing"] += 1

        elif project['main_category'] == "Technology":
            mostSuccessfulStats["Technology"] += 1

        elif project['main_category'] == "Theater":
            mostSuccessfulStats["Theater"] += 1  

    #We have the stats on successful projects from each category, now we need the total number of projects from each category to divide and get percentages
    categoryStats = getCategoryStats(projectList)      
    mostSuccessfulStats["Comics"] = round((mostSuccessfulStats["Comics"]/categoryStats["Comics"] * 100), 2)
    mostSuccessfulStats["Crafts"] = round((mostSuccessfulStats["Crafts"]/categoryStats["Crafts"] * 100), 2)
    mostSuccessfulStats["Dance"] = round((mostSuccessfulStats["Dance"]/categoryStats["Dance"] * 100), 2)
    mostSuccessfulStats["Fashion"] = round((mostSuccessfulStats["Fashion"]/categoryStats["Fashion"] * 100), 2)
    mostSuccessfulStats["Film and Video"] = round((mostSuccessfulStats["Film and Video"]/categoryStats["Film and Video"] * 100), 2)
    mostSuccessfulStats["Food"] = round((mostSuccessfulStats["Food"]/categoryStats["Food"] * 100), 2)
    mostSuccessfulStats["Journalism"] = round((mostSuccessfulStats["Journalism"]/categoryStats["Journalism"] * 100), 2)
    mostSuccessfulStats["Games"] = round((mostSuccessfulStats["Games"]/categoryStats["Games"] * 100), 2)
    mostSuccessfulStats["Music"] = round((mostSuccessfulStats["Music"]/categoryStats["Music"] * 100), 2)
    mostSuccessfulStats["Photography"] = round((mostSuccessfulStats["Photography"]/categoryStats["Photography"] * 100), 2)
    mostSuccessfulStats["Publishing"] = round((mostSuccessfulStats["Publishing"]/categoryStats["Publishing"] * 100), 2)
    mostSuccessfulStats["Technology"] = round((mostSuccessfulStats["Technology"]/categoryStats["Technology"] * 100), 2)
    mostSuccessfulStats["Theater"] = round((mostSuccessfulStats["Theater"]/categoryStats["Theater"] * 100), 2)  

    return mostSuccessfulStats

def getSuccessPercentageStats(projectList):
    successfulStateList = (search.search("successful", "state", projectList))
    mostSuccessfulStats = {
        "Total Success": 0,
        
        #Amperstand (&) is weird on graph so we manually spell it out
    }
    
    for project in successfulStateList:
        mostSuccessfulStats["Total Success"] += 1
    
    totalProj= 0
    
    for project in projectList:
        totalProj +=1
    categoryStats = getCategoryStats(projectList)      
    mostSuccessfulStats["Total Success"] = round((mostSuccessfulStats["Total Success"]/totalProj* 100), 2)
    
    return mostSuccessfulStats

def getFundingVersusSuccessStats(projectList):

    #Count all of the successes and failures in each bracket, so we can divide them and get percentages afterward. Probably a way more efficient way to do this, look into it later!
    rawFundingVersusSuccessStats = {
        "0-100 Success": 0,
        "0-100 Failed": 0,
        "101-1,000 Success": 0,
        "101-1,000 Failed": 0,
        "1,001-10,000 Success": 0,
        "1,001-10,000 Failed": 0,
        "10,001-100,000 Success": 0,
        "10,001-100,000 Failed": 0,
        "100,001-1,000,000 Success": 0,
        "100,001-1,000,000 Failed": 0,
        "1,000,001+ Success": 0,
        "1,000,001+ Failed": 0
    }

    for project in projectList:
        if project["state"] == "successful" and float(project["usd_goal_real"]) <= 100:
            rawFundingVersusSuccessStats["0-100 Success"] += 1
        elif project["state"] == "failed" and float(project["usd_goal_real"]) <= 100:
            rawFundingVersusSuccessStats["0-100 Failed"] += 1

        elif project["state"] == "successful" and float(project["usd_goal_real"]) > 100 and float(project["usd_goal_real"]) <= 1000:
            rawFundingVersusSuccessStats["101-1,000 Success"] += 1
        elif project["state"] == "failed" and float(project["usd_goal_real"]) > 100 and float(project["usd_goal_real"]) <= 1000:
            rawFundingVersusSuccessStats["101-1,000 Failed"] += 1
            
        elif project["state"] == "successful" and float(project["usd_goal_real"]) > 1000 and float(project["usd_goal_real"]) <= 10000:
            rawFundingVersusSuccessStats["1,001-10,000 Success"] += 1
        elif project["state"] == "failed" and float(project["usd_goal_real"]) > 1000 and float(project["usd_goal_real"]) <= 10000:
            rawFundingVersusSuccessStats["1,001-10,000 Failed"] += 1
            
        elif project["state"] == "successful" and float(project["usd_goal_real"]) > 10000 and float(project["usd_goal_real"]) <= 100000:
            rawFundingVersusSuccessStats["10,001-100,000 Success"] += 1
        elif project["state"] == "failed" and float(project["usd_goal_real"]) > 10000 and float(project["usd_goal_real"]) <= 100000:
            rawFundingVersusSuccessStats["10,001-100,000 Failed"] += 1

        elif project["state"] == "successful" and float(project["usd_goal_real"]) > 100000 and float(project["usd_goal_real"]) <= 1000000:
            rawFundingVersusSuccessStats["100,001-1,000,000 Success"] += 1
        elif project["state"] == "failed" and float(project["usd_goal_real"]) > 100000 and float(project["usd_goal_real"]) <= 1000000:
            rawFundingVersusSuccessStats["100,001-1,000,000 Failed"] += 1

        elif project["state"] == "successful" and float(project["usd_goal_real"]) > 1000000:
            rawFundingVersusSuccessStats["1,000,001+ Success"] += 1
        elif project["state"] == "failed" and float(project["usd_goal_real"]) > 1000000:
            rawFundingVersusSuccessStats["1,000,001+ Failed"] += 1

    fundingVersusSuccessStats = {
        "$0-$100": round((rawFundingVersusSuccessStats["0-100 Success"] / (rawFundingVersusSuccessStats["0-100 Success"] + rawFundingVersusSuccessStats["0-100 Failed"]) * 100), 2),
        "$101-$1,000": round((rawFundingVersusSuccessStats["101-1,000 Success"] / (rawFundingVersusSuccessStats["101-1,000 Success"] + rawFundingVersusSuccessStats["101-1,000 Failed"]) * 100), 2),
        "$1,001-$10,000": round((rawFundingVersusSuccessStats["1,001-10,000 Success"] / (rawFundingVersusSuccessStats["1,001-10,000 Success"] + rawFundingVersusSuccessStats["1,001-10,000 Failed"]) * 100), 2),
        "$10,001-$100,000": round((rawFundingVersusSuccessStats["10,001-100,000 Success"] / (rawFundingVersusSuccessStats["10,001-100,000 Success"] + rawFundingVersusSuccessStats["10,001-100,000 Failed"]) * 100), 2),
        "$100,001-$1,000,000": round((rawFundingVersusSuccessStats["100,001-1,000,000 Success"] / (rawFundingVersusSuccessStats["100,001-1,000,000 Success"] + rawFundingVersusSuccessStats["100,001-1,000,000 Failed"]) * 100), 2),
        "$1,000,001+": round((rawFundingVersusSuccessStats["1,000,001+ Success"] / (rawFundingVersusSuccessStats["1,000,001+ Success"] + rawFundingVersusSuccessStats["1,000,001+ Failed"]) * 100), 2)
    }

    return fundingVersusSuccessStats

def getDeadlineStats(projectList):

    deadlineStats = {
        "January": 0,
        "February": 0,
        "March": 0,
        "April": 0,
        "May": 0,
        "June": 0,
        "July": 0,
        "August": 0,
        "September": 0,
        "October": 0,
        "November": 0,
        "December": 0
    }

    launchStats = {
        "January": 0,
        "February": 0,
        "March": 0,
        "April": 0,
        "May": 0,
        "June": 0,
        "July": 0,
        "August": 0,
        "September": 0,
        "October": 0,
        "November": 0,
        "December": 0
    }

    for project in projectList:
        deadlineDate = project["deadline"].split('/')
        if deadlineDate[0] == '1':
            deadlineStats["January"] += 1
        elif deadlineDate[0] == '2':
           deadlineStats["February"] += 1
        elif deadlineDate[0] == '3':
           deadlineStats["March"] += 1
        elif deadlineDate[0] == '4':
            deadlineStats["April"] += 1
        elif deadlineDate[0] == '5':
            deadlineStats["May"] += 1
        elif deadlineDate[0] == '6':
            deadlineStats["June"] += 1
        elif deadlineDate[0] == '7':
            deadlineStats["July"] += 1
        elif deadlineDate[0] == '8':
            deadlineStats["August"] += 1
        elif deadlineDate[0] == '9':
            deadlineStats["September"] += 1
        elif deadlineDate[0] == '10':
            deadlineStats["October"] += 1
        elif deadlineDate[0] == '11':
            deadlineStats["November"] += 1
        elif deadlineDate[0] == '12':
            deadlineStats["December"] += 1

        launchDate = project["launched"].split('/')
        if launchDate[0] == '1':
            launchStats["January"] += 1
        elif launchDate[0] == '2':
           launchStats["February"] += 1
        elif launchDate[0] == '3':
           launchStats["March"] += 1
        elif launchDate[0] == '4':
            launchStats["April"] += 1
        elif launchDate[0] == '5':
            launchStats["May"] += 1
        elif launchDate[0] == '6':
            launchStats["June"] += 1
        elif launchDate[0] == '7':
            launchStats["July"] += 1
        elif launchDate[0] == '8':
            launchStats["August"] += 1
        elif launchDate[0] == '9':
            launchStats["September"] += 1
        elif launchDate[0] == '10':
            launchStats["October"] += 1
        elif launchDate[0] == '11':
            launchStats["November"] += 1
        elif launchDate[0] == '12':
            launchStats["December"] += 1

    return deadlineStats, launchStats