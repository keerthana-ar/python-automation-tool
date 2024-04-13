![built-with-python](https://github.com/keerthana-ar/python-automation-tool/assets/145217290/1bacc1f9-32d3-400d-b256-264ea206aa90)


# WhatsApp Bulk Message Sender with Google Sheets Integration

## Description

This Python automation tool utilizes Google Apps Script and the Selenium library to send bulk WhatsApp messages directly from your Google Sheets. It automates the process of exporting phone numbers and messages from a Google Sheet, generating a CSV file, and then using Selenium to send the messages through WhatsApp Web.

## Features:

Extracts phone numbers and messages from a designated Google Sheet.

Generates a CSV file containing the extracted data.

Automates WhatsApp Web login using QR code detection (manual scan required).

Sends personalized WhatsApp messages based on the data in the Google Sheet.


## Requirements:
Python 3.x

Google Apps Script access

A compatible web driver (e.g., Chrome WebDriver)

A Google account with access to a Google Sheet

Selenium WebDriver (Chrome or Firefox) : Install the python selenium library on your device.


## Installation

### 1. Set up Google Apps Script:

Create a new Google Sheet.

Go to Tools > Script editor.

Paste the provided Google Apps Script code (function exportDataToCSV() {...} ) into the script editor.

Save the script (e.g., "WhatsAppSender").


### 2. Install Python Libraries:

Open a terminal or command prompt.

Run the command: 
```bash
pip install selenium
```


### 3. Download WebDriver:

Download the appropriate WebDriver for your browser (e.g., Chrome WebDriver) from https://www.selenium.dev/downloads/.

Extract the downloaded WebDriver and place the executable file in a directory accessible by your Python script.


## How it Works:

Use the Google Apps Script to populate a CSV file named messages.csv with phone numbers (first column) and messages (second column) from a Google Sheet.

Update the Python script (whatsapp_bulk.py) with the path to your WebDriver and CSV file.

Run the Python script. It will open WhatsApp Web, prompt you to scan the QR code, and then send messages according to the information in the CSV file.

## Instructions:

### 1. Install Dependencies:

Install Python and Selenium WebDriver for your chosen browser (Chrome or Firefox).

Download the appropriate browser driver (e.g., chromedriver) and place it in a directory accessible by your system.

### 2. Google Apps Script:

Copy the provided google apps script into a new Google Apps Script project.

Update the script with the specific sheet name and column references where your phone numbers and messages reside.

Run the script to generate the messages.csv file.

Download the CSV file from your google drive to your system.

### 3. Python Script:

Replace placeholders in whatsapp_bulk.py:

Update driver_path with the absolute path to your downloaded browser driver.

Update file_name with the path to your messages.csv file.

Run the script in the command prompt. For example,
```bash
python whatsapp_bulk.py
```


## Disclaimer:

This tool is intended for personal use and educational purposes. Please use it responsibly and ethically.

Be aware that sending unsolicited bulk messages may violate WhatsApp's terms of service.

Consider implementing additional features like progress reporting or error handling for robustness.

## Additional Notes:

Consider error handling and progress reporting improvements for the Python script (e.g., using try-except blocks and informative messages).
Explore alternative locators in the Python script that are less prone to breaking with changes in the WhatsApp Web interface.

## Further Customization:

You can modify the Google Apps Script to handle more complex data formatting in the Google Sheet.
The Python script can be extended to include features like message scheduling or sending attachments (if supported by WhatsApp Web).
By following these instructions and customizing the scripts to your needs, you can automate sending WhatsApp messages using this project. Remember to use it responsibly and ethically.
