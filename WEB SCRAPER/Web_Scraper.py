from selenium import webdriver
import datetime


class webScrapper():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def openSite(self):
        self.driver.get('https://www.dramexchange.com/')                                                                #opens the site
        dataExtracted = self.driver.find_elements_by_xpath('//*[@id="tb_NationalDramSpotPrice"]/tr[3]/td[5]')           #points to the targeted data      
        self.data=("The data extracted is :- " + dataExtracted[0].text)                                                 #extracts the data
        print (self.data)
        
        #save the data in a text file everytime the code will run with time and date
        self.f=open("WebScraper.txt","a")                                                                               #opens file
        self.date=str(datetime.datetime.now())
        self.writeData=(self.data + "   " + "Date and time :- " + self.date + "\n")
        self.f.write(self.writeData)                                                                                     #writes in file
        self.f.close()
        
        
        #closes browser
        self.driver.close()



w=webScrapper()
w.openSite()