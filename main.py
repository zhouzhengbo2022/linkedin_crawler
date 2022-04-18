from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Creating a webdriver instance
#driver = webdriver.Chrome("Enter-Location-Of-Your-Web-Driver")
# This instance will be used to log into LinkedIn
driver = webdriver.Chrome('@path2_chromedriver')

email = "@email_account"
password = "@password"
# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element_by_id("username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys(email)

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys(password)

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.
#profile_url = "https://www.linkedin.com/in/wanqin-chen-287309107/" https://www.linkedin.com/in/kenneth-z-yan/
#profile_url = "https://www.linkedin.com/in/zhengbo-zhou-5b18411b6/"
profile_url = "https://www.linkedin.com/in/janice-jackson-edd/"
driver.get(profile_url)

start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
# this command scrolls the window starting from
# the pixel value stored in the initialScroll
# variable to the pixel value stored at the
# finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000

    # we will stop the script for 3 seconds so that
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed

    end = time.time()

    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break

src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

time.sleep(5)

intro = soup.find('div', {'class': 'pv-text-details__left-panel'})



name_loc = intro.find("h1")

# Extracting the Name
name = name_loc.get_text().strip()
# strip() is used to remove any extra blank spaces

works_at_loc = intro.find("div", {'class': 'text-body-medium'})

# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
works_at = works_at_loc.get_text().strip()

location_loc = intro.find_all("span", {'class': 'text-body-small'})

# Ectracting the Location
# The 2nd element in the location_loc variable has the location
#location = location_loc[0].get_text().strip()

print("Name -->", name,"\nWorks At -->", works_at,"\nLocation -->", location_loc)

total = soup.find_all("section")
#print(total)
experiences = soup.find_all("span", {"class": "mr1 hoverable-link-text t-bold"})


#print(experiences)
for experience in experiences:
    skills = experience.find_all('span',{'class':'visually-hidden'})
    for skill in skills:
        print(f'skill is {skill.get_text().strip()}')
#skills = soup.find_all('span').get_text()
#print(skills)
#skills = soup.find_all("div", {"class": ""})
#all_skills = soup.find_all("span",{"class": "pvs-navigation__text"})
#all_skills = driver.find_element_by_xpath("//a[@target='_self']").click()

#job_src = driver.page_source

#with open("output1.txt", "wb") as file:
#    file.write(total.text)

