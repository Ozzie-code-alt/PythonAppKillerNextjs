
import pygetwindow as gw
def get_browser_urls():
    browser_urls = []
    for window in gw.getWindowsWithTitle('Google Chrome') +  gw.getWindowsWithTitle('Opera GX'):
        print(window.title)
        if window.visible:
            browser_urls.append(window.title)
    print(browser_urls)
    return browser_urls
# Example usage:


def get_urls():
    urls = get_browser_urls()
    print(urls)
    

get_urls()