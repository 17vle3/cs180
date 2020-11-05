from modules import search

def getCountryStats(projectList):
    #Australia
    AU = len(search.search("AU", "country", projectList))
    #Belgium
    BE = len(search.search("BE", "country", projectList))
    #Canada
    CA = len(search.search("CA", "country", projectList))
    #China
    CH = len(search.search("CH", "country", projectList))
    #Germany
    DE = len(search.search("DE", "country", projectList))
    #Denmark
    DK = len(search.search("DK", "country", projectList))
    #Spain
    ES = len(search.search("ES", "country", projectList))
    #France
    FR = len(search.search("FR", "country", projectList))
    #Great Britain
    GB = len(search.search("GB", "country", projectList))
    #Hong Kong?
    HK = len(search.search("HK", "country", projectList))
    #Ireland
    IE = len(search.search("IE", "country", projectList))
    #Italy
    IT = len(search.search("IT", "country", projectList))
    #Japan
    JP = len(search.search("JP", "country", projectList))
    #Luxembourg
    LU = len(search.search("LU", "country", projectList))
    #Mexico
    MX = len(search.search("MX", "country", projectList))
    #Netherlands
    NL = len(search.search("NL", "country", projectList))
    #Norway
    NO = len(search.search("NO", "country", projectList))
    #New Zealand
    NZ = len(search.search("NZ", "country", projectList))
    #Sweden
    SE = len(search.search("SE", "country", projectList))
    #Singapore
    SG = len(search.search("SG", "country", projectList))
    #UNKNOWN OR UNDEFINED
    UNK = len(search.search("UNK", "country", projectList))
    #United States
    US = len(search.search("US", "country", projectList))
    
    countryStats = {
        "AU": AU,
        "BE": BE,
        "CA": CA,
        "CH": CH,
        "DE": DE,
        "DK": DK,
        "ES": ES,
        "FR": FR,
        "GB": GB,
        "HK": HK,
        "IE": IE,
        "IT": IT,
        "JP": JP,
        "LU": LU,
        "MX": MX,
        "NL": NL,
        "NO": NO,
        "NZ": NZ,
        "SE": SE,
        "SG": SG,
        "UNK": UNK,
        "US": US
    }

    return countryStats

def getFailedTakeoffStats(projectList):
    zeroBackers = (search.search("0", "backers", projectList))

    Comics = len(search.search("Comics", "main_category", zeroBackers))
    Crafts = len(search.search("Crafts", "main_category", zeroBackers))
    Dance = len(search.search("Dance", "main_category", zeroBackers))
    Fashion = len(search.search("Fashion", "main_category", zeroBackers))
    FilmAndVideo = len(search.search("Film & Video", "main_category", zeroBackers))
    Food = len(search.search("Food", "main_category", zeroBackers))
    Games = len(search.search("Games", "main_category", zeroBackers))
    Journalism = len(search.search("Journalism", "main_category", zeroBackers))
    Music = len(search.search("Music", "main_category", zeroBackers))
    Photography = len(search.search("Photography", "main_category", zeroBackers))
    Publishing = len(search.search("Publishing", "main_category", zeroBackers))
    Technology = len(search.search("Technology", "main_category", zeroBackers))
    Theater = len(search.search("Theater", "main_category", zeroBackers))

    print(Comics + Crafts + Dance + Fashion + FilmAndVideo + Food + Games + Journalism + Music + Photography + Publishing + Technology + Theater)

    failedTakeoffStats = {
        "Comics": Comics,
        "Crafts": Crafts,
        "Dance": Dance,
        "Fashion": Fashion,
        #Amperstand (&) is weird on graph so we manually spell it out
        "Film and Video": FilmAndVideo,
        "Food": Food,
        "Journalism": Journalism,
        "Games": Games,
        "Music": Music,
        "Photography": Photography,
        "Publishing": Publishing,
        "Technology": Technology,
        "Theater": Theater
    }
        

    return failedTakeoffStats