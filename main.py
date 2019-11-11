# header file imported
from bs4 import BeautifulSoup
from selenium import webdriver

# path = path of the chrome drive from the folder and r is raw file
path= r"C:\\Users\\Jothi\\Desktop\\Mukilan\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = path)

# creating a file name
file = "Details.csv"
f = open(file, "w") #open the file
Headers = "Name,Score,State,Country,Area,Lang\n" #heading part
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
    Title = soup.find_all("div", {"class":"user-details"})
    # print(len(Title)) #total lenth of the user in the page
    # PTag = soup.find_all("div", {"class":"user-tags"})
    # loop for getting the name 
    for i in Title:
        try:
            name = i.find('a').get_text()
            score = i.find('span', class_ ='reputation-score').get_text()
            location = i.find('span', class_ ='user-location').get_text()
            # lang = i.find_all('a')
            # print(name)
            # print(location)
            # print(score)
            name_list = (name)
            score_list = (score)
            location_list = (location)
            # lang_list = (lang)
            f.write(name_list)
            f.write(",")
            f.write(score_list)
            f.write(",")
            f.write(location_list)
            # f.write(",")
            # f.write(lang_list)
            f.write("\n")    
        except: AttributeError
f.close()