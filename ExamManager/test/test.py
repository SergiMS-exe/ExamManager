from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import random
import time

# initialize the Chrome driver
driver = webdriver.Chrome(executable_path="chromedriver.exe")

# Credentials
email = "xxx@gmail.com"
password = "123456"

name = "John"
surname= "Smith"
date="01.01.2021"
email_examiner= "examiner@gmail.com"
group_name="G--1"
t =4

def run():
    
    incorrect_username_login()
    time.sleep(t)
    correct_login_test()
    time.sleep(t)
    incorrect_password_login()
    time.sleep(t)
    #correct_user_type_logged_in()
    register_teacher_test()
    time.sleep(t)
    register_student_test()
    time.sleep(t)
    teacher_adds_exam_group()
    time.sleep(t)
    register_with_existent_email()
    time.sleep(t)
    
    participant_added_to_group() #Throws an error if the id is not correct
    time.sleep(10)
    exam_group_shows_up_on_the_student_page()
    time.sleep(t)
    
    

def incorrect_username_login():
    
    wrong_email="wrongperson@gmail.com"
    # head to main page
    driver.get("http://127.0.0.1:5000")
    
    # find email field and send the email itself to the input field
    driver.find_element_by_id("email").send_keys(wrong_email)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(t)
    #driver.implicitly_wait(90)
    WebDriverWait(driver=driver, timeout=100)
    # click login button
    driver.find_element_by_name("commit").click()
    
    #driver.close()

def correct_login_test():
    # head to register page
    driver.get("http://127.0.0.1:5000/register")
    n = random.randint(0,1000)
    email = ("username" + str(n) + "@gmail.com")
    driver.find_element_by_id("email1").send_keys(email)
    driver.find_element_by_id("name1").send_keys(name)
    driver.find_element_by_id("Surname1").send_keys(surname)
    driver.find_element_by_id("password1").send_keys(password)
    driver.find_element_by_id("password2").send_keys(password)
    driver.find_element_by_id("date1").send_keys(date)
    driver.find_element_by_id("examiner").click()
    time.sleep(t)
    driver.find_element_by_name("loginbutton").click()
    
    # head to main page
    driver.get("http://127.0.0.1:5000")
    # find email field and send the email itself to the input field
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(t)
    # click login button
    driver.find_element_by_name("commit").click()
    #driver.close()
    

def incorrect_password_login():

    correct_email = "AlekseyVolkov@gmail.com"
    password = "wrongpassword"
    # head to main page
    driver.get("http://127.0.0.1:5000") 
    # find email field and send the email itself to the input field
    driver.find_element_by_id("email").send_keys(correct_email)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(t)
    #driver.implicitly_wait(90)
    WebDriverWait(driver=driver, timeout=100)
    # click login button
    driver.find_element_by_name("commit").click()
   
    #driver.close()

### This test is not done #####
def correct_user_type_logged_in():
    # I dont know how to print a message on the screen#####
    correct_email_examiner = "AlekseyVolkov@gmail.com"
    correct_password_examiner = "jjjjj"
    correct_email_student = "MaximeLeBlanc@gmail.com"
    correct_password_student= "kkkkk"
    # head to main page
    driver.get("http://127.0.0.1:5000")
        
    # find email field and send the email itself to the input field
    driver.find_element_by_id("email").send_keys(correct_email_examiner)
    driver.find_element_by_id("password").send_keys(correct_password_examiner)
    time.sleep(t)
    #driver.find_element_by_class_name("error").text
    WebDriverWait(driver, 10).until(driver.find_element_by_name("commit").click())

    ######It doesnt want to wait :(( ######
    #driver.implicitly_wait(10)

    #driver.close()

# Each time provide new email address 
def register_teacher_test():
    n = random.randint(0,1000)
    email = ("username" + str(n) + "@gmail.com")


    driver.get("http://127.0.0.1:5000/register")

    driver.find_element_by_id("email1").send_keys(email)
    driver.find_element_by_id("name1").send_keys(name)
    driver.find_element_by_id("Surname1").send_keys(surname)
    driver.find_element_by_id("password1").send_keys(password)
    driver.find_element_by_id("password2").send_keys(password)
    driver.find_element_by_id("date1").send_keys(date)
    driver.find_element_by_id("examiner").click()
    time.sleep(t)
    driver.find_element_by_name("loginbutton").click()
    #driver.close()

# Each time provide new email address 
def register_student_test():
    n = random.randint(0,1000)
    email = ("username" + str(n) + "@gmail.com")

    driver.get("http://127.0.0.1:5000/register")

    driver.find_element_by_id("email1").send_keys(email)
    driver.find_element_by_id("name1").send_keys(name)
    driver.find_element_by_id("Surname1").send_keys(surname)
    driver.find_element_by_id("password1").send_keys(password)
    driver.find_element_by_id("password2").send_keys(password)
    driver.find_element_by_id("date1").send_keys(date)
    driver.find_element_by_id("Student").click()
    time.sleep(t)
    driver.find_element_by_name("loginbutton").click()
    #driver.close()

def register_with_existent_email():
    email = "username@gmail.com"

    driver.get("http://127.0.0.1:5000/register")

    driver.find_element_by_id("email1").send_keys(email)
    driver.find_element_by_id("name1").send_keys(name)
    driver.find_element_by_id("Surname1").send_keys(surname)
    driver.find_element_by_id("password1").send_keys(password)
    driver.find_element_by_id("password2").send_keys(password)
    driver.find_element_by_id("date1").send_keys(date)
    driver.find_element_by_id("Student").click()
    time.sleep(t)
    #WebDriverWait(driver, 10).until(driver.find_element_by_name("loginbutton").click())
    driver.find_element_by_name("loginbutton").click()
    #driver.find_element_by_name("loginbutton").click()

    #driver.close()


def teacher_adds_exam_group():
    group_name="examGroup1"

    ## You can create several groups with the same name! (Group ID changes each time)
    driver.get("http://127.0.0.1:5000//teacherpage/2021001/3")
    driver.find_element_by_id("enterAGroup").send_keys(group_name)
    driver.find_element_by_name("btn-creategroup").click()
    time.sleep(t)
    driver.implicitly_wait(10)
    
    #driver.close()

def correct_exam_name_saved():
    pass


def participant_added_to_group():
    # input a non-exist particapant in the participants list
    participant_id = 251236
    driver.get("http://127.0.0.1:5000//teacherpage/2021001/3")
    driver.find_element_by_name("ParticipantId").send_keys(participant_id)
    time.sleep(2)
    driver.find_element_by_name("AddParticipant").click()
    time.sleep(t)
    driver.find_element_by_id("Participants").click()
    #driver.close()

def exam_group_shows_up_on_the_student_page():
    # Goes to the student page and shows the exam_group that created in the participant_added_to_group()
    driver.get("http://127.0.0.1:5000//studentpage/251236/2")
    #driver.close()

    




if __name__ == "__main__":
    run()
