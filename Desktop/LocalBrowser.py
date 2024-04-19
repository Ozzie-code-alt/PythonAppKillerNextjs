from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# List to store the URLs of visited websites
visited_websites = []

def get_current_url():
    try:
        return driver.current_url
    except Exception as e:
        print("Browser closed:", e)
        return None


def add_website(url):
    if url and url not in visited_websites:
        visited_websites.append(url)


def print_visited_websites():
    print("Visited Websites:")
    for url in visited_websites:
        print(url)


def print_all_tab_titles():
    print("Current Open Tabs:")
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        print(driver.title)

# Open a new tab
driver.execute_script("window.open('');")

# Print the titles of all open tabs
print_all_tab_titles()

# Real-time tracking of visited websites
last_url = get_current_url()

while True:
    current_url = get_current_url()
    if current_url is None:
        break # Browser is closed, break out of the loop
    elif current_url != last_url:
        add_website(current_url)
        print_visited_websites()
        last_url = current_url
    # Print the titles of all open tabs every 5 seconds
    print_all_tab_titles()
    time.sleep(5) # Check every second

print(visited_websites)
print("Closing browser...")
driver.quit()
