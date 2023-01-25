from typing import IO
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
from jobboard import linkedIn,indeed,ziprecruiter

class JobBot:
    userPassDict:dict
    isLoggedIn:bool
    resume:IO[str]
    sites:set
    jobDescDict:dict 
    def __init__(self,userPassDict:dict,sites:list) -> None:
        self.userPassDict = userPassDict
        self.sites = sites
        self


    def start(self,typeOfJobs:list,locations:list,employmentType:list,priceRange:tuple) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        chrome = webdriver.Chrome(executable_path="./chromedriver",chrome_options=options)
        numOfSites = len(self.sites)
        executor:ThreadPoolExecutor = ThreadPoolExecutor(max_workers=numOfSites)



        for i in range(executor._max_workers):
            executor.submit(self.task(chrome,typeOfJobs,locations,employmentType,priceRange))
        executor.shutdown(wait=True)

    # A helper function that will be used by the thread pool
    def task(self,driver,typeOfJobs,locations,employmentType,priceRange):
            for site in self.sites:
                if isinstance(site,str):
                    driver.get(site)
                    if driver.title.find("linkedin") != -1:
                        self.linkedIn(driver,typeOfJobs,locations,employmentType,priceRange)
                    elif driver.title.find("indeed") != -1:
                        self.indeed(driver,typeOfJobs,locations,employmentType,priceRange)
                    elif driver.title.find("ziprecruiter") != -1:
                        self.ziprecruiter(driver,typeOfJobs,locations,employmentType,priceRange)
                    else:
                        print(f'We do not have an implementation to login into {driver.title} yet....')        
                        pass
            else:
                print("Site given is not a string or url") 

    def load_resume(self)->None: 
        pass
    
    def linkedIn(self,driver,typeOfJobs:list,locations:list,employmentType:list,priceRange:tuple)->None:
        dash:linkedIn.LinkedinDashBoard = linkedIn.LinkedinDashBoard(typeOfJobs,locations,employmentType,priceRange)
        username,password = self.userPassDict.get("linkedIn")["username"],self.userPassDict.get("linkedIn")["password"]
        self.isLoggedIn = dash.login(username,password,driver)
        # Sleep Driver once logged in
        # Handles searching logic for Job Descriptions based on your preferences

        if self.isLoggedIn: 
            dash.search(driver)
            self.jobDescDict.setdefault("linkedIn",dash.getJDs())
        else:
            print("You are not logged into linkedIn, please check your credentials.")    


    def indeed(self,driver,typeOfJobs:list,locations:list,employmentType:list,priceRange:tuple) ->None:
        dash:indeed.IndeedDashBoard = indeed.IndeedDashBoard(typeOfJobs,locations,employmentType,priceRange)
        username,password = self.userPassDict.get("indeed")["username"],self.userPassDict.get("indeed")["password"]
        self.isLoggedIn = dash.login(username,password,driver)
        # Sleep Driver once logged in
        # Handles searching logic for Job Descriptions based on your preferences
        dash.search(driver)
        self.jobDescDict.setdefault("indeed",dash.getJDs())

    def ziprecruiter(self,driver,typeOfJobs:list,locations:list,employmentType:list,priceRange:tuple)->None:
        dash:ziprecruiter.ZipRecruiterDashBoard = ziprecruiter.ZipRecruiterDashBoard(typeOfJobs,locations,employmentType,priceRange)
        username,password = self.userPassDict.get("ziprecruiter")["username"],self.userPassDict.get("ziprecruiter")["password"]
        self.isLoggedIn = dash.login(username,password,driver)
        # Sleep Driver once logged in
        # Handles searching logic for Job Descriptions based on your preferences
        dash.search(driver)
        self.jobDescDict.setdefault("ziprecruiter",dash.getJDs())