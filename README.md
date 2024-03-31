# WhatsApp Bulk Messaging Tool
This project automates sending WhatsApp messages from a Google sheet using a Python script and a Google Apps Script.

## Components:

Python Script (whatsapp_bulk123.py):
Sends WhatsApp messages to phone numbers listed in a CSV file.
Uses Selenium WebDriver to interact with the WhatsApp Web interface.

## Requirements:
Python 3
Selenium WebDriver (Chrome or Firefox) : Install the python selenium library on your device by running the given command on your command prompt.
```bash
pip install selenium
```
Appropriate browser driver (e.g., chromedriver)

Google Apps Script: Creates a CSV file from phone numbers and messages entered in a Google Sheet.

## Requirements:
Google Workspace account with access to Google Sheets

## How it Works:

Use the Google Apps Script to populate a CSV file named messages.csv with phone numbers (first column) and messages (second column) from a Google Sheet.

Update the Python script (whatsapp_bulk123.py) with the path to your WebDriver and CSV file.

Run the Python script. It will open WhatsApp Web, prompt you to scan the QR code, and then send messages according to the information in the CSV file.

## Instructions:

1. Install Dependencies:
Install Python and Selenium WebDriver for your chosen browser (Chrome or Firefox).
Download the appropriate browser driver (e.g., chromedriver) and place it in a directory accessible by your system.

2. Google Apps Script:
Copy the provided google apps script into a new Google Apps Script project.
Update the script with the specific sheet name and column references where your phone numbers and messages reside.
Run the script to generate the messages.csv file.

3. Python Script:
Replace placeholders in whatsapp_bulk123.py:
Update driver_path with the absolute path to your downloaded browser driver.
Update file_name with the path to your messages.csv file.
Run the script (e.g., python send_whatsapp_message.py).

## Disclaimer:

Using this tool to automate sending messages might violate WhatsApp's terms of service. Use it responsibly and ethically.
Be mindful of potential rate limits imposed by WhatsApp to avoid overwhelming their servers or getting your account flagged.
This documentation provides a basic overview. Refer to the script code for detailed functionality.

## Additional Notes:

Consider error handling and progress reporting improvements for the Python script (e.g., using try-except blocks and informative messages).
Explore alternative locators in the Python script that are less prone to breaking with changes in the WhatsApp Web interface.

## Further Customization:

You can modify the Google Apps Script to handle more complex data formatting in the Google Sheet.
The Python script can be extended to include features like message scheduling or sending attachments (if supported by WhatsApp Web).
By following these instructions and customizing the scripts to your needs, you can automate sending WhatsApp messages using this project. Remember to use it responsibly and ethically.
