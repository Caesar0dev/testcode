from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
import os
from PyPDF2 import PdfReader


print("-----------Automation Scraping is successfully started------------")
driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
driver.maximize_window()
URL = "https://www.ampol.com.au/about-ampol/investor-centre/annual-reports/2022"
driver.get(URL)
driver.find_element(By.XPATH, '//*[@id="mod-hero-1"]/div/div/a').click()

def go_to_page_in_downloads(filename, page_number):
    global page_content
    downloads_folder = os.path.expanduser("~") + "/Downloads"
    file_path = os.path.join(downloads_folder, '2022 Ampol Australia Annual Report.pdf')
    while not os.path.exists(file_path):
        time.sleep(1)  # Wait for 1 second before checking again    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            total_pages = len(reader.pages)
            
            if page_number > total_pages:
                print(f"The PDF file only has {total_pages} pages.")
                return
            
            page = reader.pages[page_number - 1]
            page_content = page.extract_text()
            
            # Process or display the content of the page
            print(f"Page {page_number} content:")
            # print(page_content)
    else:
        print(f"File '{filename}' does not exist in the Downloads folder.")
        
def get_last_string_starting_with(text, start):
    rows = text.split('\n')  # Split the text into rows

    for row in rows:
        if row.startswith(start):
            words = row.split()  # Split the row into words
            last_word = words[-1]  # Get the last word
            return last_word
        
filename = 'myfile.pdf'
page_number = 41
go_to_page_in_downloads(filename, page_number)

print(page_content)
text = page_content
# start = 'Scope 1'
Emission_Scope1 = float(str(get_last_string_starting_with(text, "Scope 1")).replace(',', ''))
Emission_Scope2 = float(str(get_last_string_starting_with(text, "Scope 2")).replace(',', ''))
Emission_Total_Scope = float(str(get_last_string_starting_with(text, "Total Scope")).replace(',', ''))

print("Emission Scope1:", Emission_Scope1)
print("Emission Scope2:", Emission_Scope2)
print("Emission Total_Scope:", Emission_Total_Scope)


while True:
    pass