from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# initialize the Chrome driver
driver = webdriver.Chrome(executable_path="C:/Users/ozlemt/Downloads/chromedriver.exe")

# Credentials
email = "xxx@gmail.com"
password = "password"
correct_email = "AlekseyVolkov@gmail.com"
correct_password = "jjjjj"
name = "xxx"
surname= "yyy"
date="01.01.2021"
email_examiner= "examiner@gmail.com"
group_name="G--1"


def run():
    teacher_adds_exam_group()
    incorrect_username_login()
    correct_login_test()
    incorrect_password_login()
    #correct_user_type_logged_in()
    register_teacher_test()
    register_student_test()
    

def incorrect_username_login():
    # head to main page
    
    driver.get("http://127.0.0.1:5000")
    
    # find email field and send the email itself to the input field
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)

    driver.implicitly_wait(90)
    WebDriverWait(driver=driver, timeout=100)
    # click login button
    driver.find_element_by_name("commit").click()
    
    #driver.close()

def correct_login_test():

    correct_email = "AlekseyVolkov@gmail.com"
    correct_password = "jjjjj"
    # head to main page
    driver.get("http://127.0.0.1:5000")
    
    # find email field and send the email itself to the input field
    driver.find_element_by_id("email").send_keys(correct_email)
    driver.find_element_by_id("password").send_keys(correct_password)

    driver.implicitly_wait(90)
    
    # click login button
    driver.find_element_by_name("commit").click()

    #driver.close()

def incorrect_password_login():

    correct_email = "AlekseyVolkov@gmail.com"
    password = "password"
    # head to main page
    driver.get("http://127.0.0.1:5000") 
    # find email field and send the email itself to the input field
    driver.find_element_by_id("email").send_keys(correct_email)
    driver.find_element_by_id("password").send_keys(password)
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
    #driver.find_element_by_class_name("error").text
    WebDriverWait(driver, 10).until(driver.find_element_by_name("commit").click())

    ######It doesnt want to wait :(( ######
    #driver.implicitly_wait(10)

    #driver.close()

# we should consider if the person is already registered(we should write another test for that)
def register_teacher_test():
    email_examiner= "examiner@gmail.com"

    driver.get("http://127.0.0.1:5000/register")

    driver.find_element_by_id("email1").send_keys(email_examiner)
    driver.find_element_by_id("name1").send_keys(name)
    driver.find_element_by_id("Surname1").send_keys(surname)
    driver.find_element_by_id("password1").send_keys(password)
    driver.find_element_by_id("password2").send_keys(password)
    driver.find_element_by_id("date1").send_keys(date)
    driver.find_element_by_id("examiner").click()
    driver.find_element_by_name("loginbutton").click()
    #driver.close()

# we should consider if the person is already registered
def register_student_test():
    driver.get("http://127.0.0.1:5000/register")

    driver.find_element_by_id("email1").send_keys(email)
    driver.find_element_by_id("name1").send_keys(name)
    driver.find_element_by_id("Surname1").send_keys(surname)
    driver.find_element_by_id("password1").send_keys(password)
    driver.find_element_by_id("password2").send_keys(password)
    driver.find_element_by_id("date1").send_keys(date)
    driver.find_element_by_id("Student").click()
    driver.find_element_by_name("loginbutton").click()
    #driver.close()

def teacher_adds_exam_group():
    group_name="G--1"

    ## You can create several groups with the same name! (Group ID changes each time)
    driver.get("http://127.0.0.1:5000//teacherpage/2021003/1")
    driver.find_element_by_id("enterAGroup").send_keys(group_name)
    driver.find_element_by_name("btn-creategroup").click()
    driver.find_element_by_id("enterAGroup").send_keys(group_name)
    driver.find_element_by_name("btn-creategroup").click()
    #driver.close()



if __name__ == "__main__":
    run()
