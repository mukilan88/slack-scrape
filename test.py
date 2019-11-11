# header file imported
from bs4 import BeautifulSoup
from selenium import webdriver

# path = path of the chrome drive from the folder and r is raw file
path= r"C:\\Users\\Jothi\\Desktop\\Mukilan\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = path)

# creating a file name
file = "Details.csv"
f = open(file, "w") #open the file
Headers = "Name,Score,State,Country\n" #heading part
f.write(Headers) #inserting the heading

# range = [0 to 2]
# loop for multi page open

for i in range(1,3):
    print(i)
    # opening the url
    url = "https://stackoverflow.com/users?page=" + format(i) + "&tab=reputation&filter=week"
    driver.get(url)
    # scraping using bs4
    soup = BeautifulSoup(driver.page_source,'html.parser')
    # print(soup)
    # finding the name of the user inside the class file
    # Title = soup.find_all("div", {"class":"user-details"})
    # print(len(Title)) #total lenth of the user in the page
    PTag = soup.find_all("div", {"class":"user-tags"})
   
    # loop for getting the name 
    for i in PTag:
        try:
            # name = i.find('a', {"href":"/questions/tagged/python"}).get_text()
            name = i.find_all('a')

            print(i.text)
             
        except: AttributeError
f.close()