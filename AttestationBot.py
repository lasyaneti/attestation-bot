from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

form = webdriver.Chrome()
form.get("https://issaquah.az1.qualtrics.com/jfe/form/SV_6nepDReMDTALzMx")

time.sleep(2) #repeated after every page to avoid "no such element error"

nextButton: form.find_element_by_id("NextButton") #repetition due to stale element error. needs fixing
nextButton.click() 

time.sleep(2) 

email = form.find_element_by_id("QR~QID22~1")
myEmail = "XXX@gmail.com"
email.send_keys(myEmail)
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2) 

firstname = form.find_element_by_id("QR~QID24~1")
myFirstName = "Lasya"
firstname.send_keys(myFirstName)
lastname = form.find_element_by_id("QR~QID24~2")
myLastName = "Neti"
lastname.send_keys(myLastName)
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2) 

form.find_element_by_id("QID29-2-label").click() #select visitor type as current student
dropdown = form.find_element_by_id("QR~QID33")
myGrade = form.find_element_by_id("QR~QID33~13")
time.sleep(2) #time to load dropdown element
Select(dropdown).select_by_visible_text("Grade 12")
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2)

nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2)

form.find_element_by_id("QID21-1-label").click() #entering facility
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2)

form.find_element_by_id("QID69-21-label").click() #specify facility
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2)

form.find_element_by_id("QID11-1-label").click() #consent
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2)

form.find_element_by_id("QID34-19-label").click() #symptoms
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2)

form.find_element_by_id("QID63-6-label").click() #distancing from affected people
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2)

form.find_element_by_id("QID64-6-label").click() #COVID test result
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

time.sleep(2)

form.find_element_by_id("QID65-6-label").click() #quarantine 
nextButton = form.find_element_by_id("NextButton")
nextButton.click()

form.close()