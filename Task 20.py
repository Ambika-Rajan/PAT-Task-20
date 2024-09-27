from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to your WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the CoWIN website
    driver.get("https://www.cowin.gov.in/")

    # Allow some time for the page to load
    time.sleep(5)

    # Click on the "FAQ" anchor tag
    faq_link = driver.find_element(By.LINK_TEXT, "FAQ")
    faq_link.click()

    # Allow some time for the new window to open
    time.sleep(2)

    # Fetch and display the current window handles
    all_windows = driver.window_handles
    print("Window handles after clicking FAQ:", all_windows)

    # Switch to the new window (FAQ)
    driver.switch_to.window(all_windows[1])

    # Allow some time for the FAQ page to load
    time.sleep(5)

    # Print the page title of the FAQ page
    print("FAQ Page Title:", driver.title)

    # Close the FAQ window
    driver.close()

    # Switch back to the original window (CoWIN homepage)
    driver.switch_to.window(all_windows[0])

    # Click on the "Partners" anchor tag
    partners_link = driver.find_element(By.LINK_TEXT, "Partners")
    partners_link.click()

    # Allow some time for the new window to open
    time.sleep(2)

    # Fetch and display the current window handles again
    all_windows = driver.window_handles
    print("Window handles after clicking Partners:", all_windows)

    # Switch to the new window (Partners)
    driver.switch_to.window(all_windows[1])

    # Allow some time for the Partners page to load
    time.sleep(5)

    # Print the page title of the Partners page
    print("Partners Page Title:", driver.title)

    # Close the Partners window
    driver.close()

    # Switch back to the original window
    driver.switch_to.window(all_windows[0])

    # Print the title of the home page to confirm we are back
    print("Home Page Title:", driver.title)

finally:
    # Close the original window
    driver.quit()
