from selenium import webdriver
import time



def initialize_driver():
    return webdriver.Chrome()

def pass_visited_website(driver):
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
            print("Driver Function Handle:", handle)
            print(driver.title)

    last_url = get_current_url()

    current_window = driver.current_window_handle
    print("Current Window:", current_window)

    while True:
        current_url = get_current_url()
        if current_url is None:
            break
        elif current_url != last_url:
            add_website(current_url)
            print_visited_websites()
            last_url = current_url

        print_all_tab_titles()
        print("Current URL local:", current_url)

        # Check every second
        time.sleep(5)

    return visited_websites
