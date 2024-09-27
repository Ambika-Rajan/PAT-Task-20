import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to your WebDriver
driver = webdriver.Chrome()

# Create a folder to store the downloaded images
folder_name = "Photo_Gallery"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

try:
    # Step 1: Navigate to the Labour website
    driver.get("https://labour.gov.in/")
    time.sleep(5)  # Allow time for the page to load

    # Step 2: Click on the "Documents" menu
    documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
    documents_menu.click()
    time.sleep(5)  # Allow time for the documents page to load

    # Step 3: Download the Monthly Progress Report
    report_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Monthly Progress Report")
    report_url = report_link.get_attribute("href")

    # Download the report
    response = requests.get(report_url)
    with open("Monthly_Progress_Report.pdf", 'wb') as file:
        file.write(response.content)
    print("Downloaded Monthly Progress Report.")

    # Step 4: Go to the "Media" menu and then "Photo Gallery"
    media_menu = driver.find_element(By.LINK_TEXT, "Media")
    media_menu.click()
    time.sleep(5)  # Allow time for the media page to load

    photo_gallery = driver.find_element(By.LINK_TEXT, "Photo Gallery")
    photo_gallery.click()
    time.sleep(5)  # Allow time for the photo gallery page to load

    # Step 5: Download the first 10 photos
    images = driver.find_elements(By.TAG_NAME, "img")[:10]  # Get the first 10 image elements

    for i, img in enumerate(images):
        img_url = img.get_attribute("src")
        if img_url:  # Ensure the URL is valid
            img_response = requests.get(img_url)
            img_filename = os.path.join(folder_name, f"photo_{i + 1}.jpg")
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_response.content)
            print(f"Downloaded {img_filename}")

finally:
    # Close the browser
    driver.quit()
