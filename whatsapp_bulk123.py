import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Path to your webdriver
# Choose the browser (Chrome or Firefox)
browser = webdriver.Chrome()
# or use webdriver.Firefox(executable_path=driver_path)

# Open WhatsApp Web
browser.get('https://web.whatsapp.com/')
time.sleep(15) # Wait for QR code scan

def send_whatsapp_message(phone_number, message):
    # Find the search box
    try:
        # Use WebDriverWait for reliable element location
        search_box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p")))
        search_box.send_keys(phone_number)
        search_box.send_keys(Keys.ENTER)
       
        message_box = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"))
        )
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Message sent to {phone_number}")
        
    except NoSuchElementException as e:
        print("Error: Element not found.", e)

#Read the CSV file
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
    
# Close the browser
time.sleep(2) # Wait for the message to send
browser.quit()