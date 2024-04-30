from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

# Set options for the Chromium browser
chrome_options = Options()
chrome_options.binary_location = 'chrome-linux64/chrome'

# Initialize the Chromium WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Google
    driver.get("https://www.google.com/")
    
    # Find the search box
    search_box = driver.find_element("name", "q")
    
    # Clear any existing text in the search box
    search_box.clear()
    
    # Send the search query
    search_box.send_keys("maize prices India")
    
    # Submit the search query (press Enter)
    search_box.submit()

    # Wait for the search results to load (you might need to adjust the wait time)
    driver.implicitly_wait(10)

    # Extract the price from the search results
    try:
        price_element = driver.find_element("css selector", "tr.ztXv9 th:nth-of-type(2)")
        price = price_element.text
        
        # Get the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write the output to a new text file
        with open("price.txt", "w") as file:
            file.write("Date and Time: " + current_datetime + "\n")
            file.write("Live maize price: " + price)
        
        print("Date and Time:", current_datetime)
        print("Live maize price:", price)
    except NoSuchElementException:
        print("Maize prices not found in search results.")

finally:
    # Close the browser
    driver.quit()
