from selenium import webdriver

def get_driver():
    # Set options to make browsing easier
    chrome_settings = webdriver.ChromeOptions()
    chrome_settings.add_argument("disable-infobars") # Disable the info bar if website has it
    chrome_settings.add_argument("start-maximized") # Start browser as maximized
    chrome_settings.add_argument("disable-dev-shm-usage") # Disabled devshm for Linux
    chrome_settings.add_argument("no-sandbox") # Disable sandboxing mode
    # Enable script to access browser
    chrome_settings.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_settings.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_settings)# Initialize driver with above options
    driver.get("https://www.icy-veins.com/wow-classic/priest-healer-pve-guide")
    return driver

def main():
    driver = get_driver() # Creates browser instance
    list_items = driver.find_elements(by="xpath", value='//*[@id="center"]/div[3]/div[4]/div[2]/div[1]/div[2]/ul/li') # Finds all <li> elements
    texts = [item.find_element(by="xpath", value='./span').text for item in list_items] # Get the text of each <span> within <li>

    for text in texts:
        print(text) # Print each text line by line

main()
