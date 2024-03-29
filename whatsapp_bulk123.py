import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_whatsapp_message(phone_number, message):
    # Path to your WebDriver
    #driver_path = 'C:\Users\Keerthana A R\Downloads\chromedriver_win32'
    # Choose the browser (Chrome or Firefox)
    browser = webdriver.Chrome()
    # or use webdriver.Firefox(executable_path=driver_path)

    # Open WhatsApp Web
    browser.get('https://web.whatsapp.com/')
    time.sleep(15) # Wait for QR code scan

    # Find the search box
    search_box = browser.find_element(By.XPATH,'//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(phone_number)
    search_box.send_keys(Keys.ENTER)

    # Wait for the chat to open and then for the message input box to appear
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='6']")))

    # Type the message
    message_box = browser.find_element(By.XPATH,'//div[@contenteditable="true"][@data-tab="6"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

    # Close the browser
    time.sleep(2) # Wait for the message to send
    browser.quit()

# Read the CSV file
def read_csv(file_name):
    contacts=[]
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip the header
        for row in reader:
            contacts.append((row[0], row[1])) # Assuming phone number is in the first column and message in the second
    return contacts


contacts = read_csv('messages.csv')
for contact in contacts:
    send_whatsapp_message(contact[0], contact[1])
    time.sleep(2) # Wait before sending the next message