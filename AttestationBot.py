from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def nextpage(): 
    nextButton = driver.find_element_by_id("NextButton") #define var on every page to avoid slate element exception
    nextButton.click()
    time.sleep(2) #time to load elements of new page

driver = webdriver.Chrome()
driver.get("https://issaquah.az1.qualtrics.com/jfe/form/SV_6nepDReMDTALzMx")

time.sleep(2)
nextpage()


email = driver.find_element_by_id("QR~QID22~1")
myEmail = "XXX"
email.send_keys(myEmail)

nextpage()

firstname = driver.find_element_by_id("QR~QID24~1")
myFirstName = "Lasya"
firstname.send_keys(myFirstName)
lastname = driver.find_element_by_id("QR~QID24~2")
myLastName = "Neti"
lastname.send_keys(myLastName)

nextpage()
time.sleep(2)

driver.find_element_by_id("QID29-2-label").click() #select visitor type as current student
dropdown = driver.find_element_by_id("QR~QID33")
myGrade = driver.find_element_by_id("QR~QID33~13")
time.sleep(2) #time to load dropdown element
Select(dropdown).select_by_visible_text("Grade 12")

nextpage()

nextpage()

driver.find_element_by_id("QID21-1-label").click() #entering facility

nextpage()

driver.find_element_by_id("QID69-21-label").click() #specify facility

nextpage()

driver.find_element_by_id("QID11-1-label").click() #consent

nextpage()

driver.find_element_by_id("QID34-19-label").click() #symptoms

nextpage()

driver.find_element_by_id("QID63-6-label").click() #distancing from affected people

nextpage()

driver.find_element_by_id("QID64-6-label").click() #COVID test result

nextpage()

driver.find_element_by_id("QID65-6-label").click() #quarantine 

nextpage()

driver.close()