# Base class for all dashboards
class DashBoard:
    setOfJDLinks:set
    profilelink:str
    typeOfJobs:set
    locations:set
    employmentType:set
    priceRange:tuple

    def __init__(self,typeOfJobs:set,locations:set,employmentType:set,priceRange:tuple) -> None:
        self.typeOfJobs = typeOfJobs
        self.locations = locations
        employmentType = employmentType
        self.setOfJDLinks = set()
        self.profilelink = ""
        self.priceRange = priceRange
        pass


    # ------------------------------ GETTERS AND SETTERS -----------------------------
    def setProfileLink(self,driver)->None:
        pass

    def getJDs(self) -> set:
        return self.setOfJDLinks

    # -------------------------------- REGULAR METHODS -------------------------------- 

    # Does a deep search on a job board site and will gather
    # links to jobs that actual correlate to what you are
    # looking for.
    def search(self,driver) -> None:
        pass

    # Logs the user in of their profile.
    def login(self,username:str,password:str,driver)-> bool:
        pass

    # Logs the user out of their profile.
    def logout(self,driver) -> None:
        pass