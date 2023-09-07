import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_links(link):
    options = Options()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')

    # Initialize the WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(link)

    links = []

    def scroll_to_bottom():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_show_more_button():
        try:
            show_more_button = driver.find_element_by_xpath("//button[contains(@class, 'infinite-scroller__show-more-button')]")
            driver.execute_script("arguments[0].scrollIntoView();", show_more_button)
            show_more_button.click()
            time.sleep(2)
            return True
        except:
            return False

    while True:
        if click_show_more_button():
            scroll_to_bottom()
        else:
            break

    links = driver.execute_script("return [...document.querySelectorAll('ul.jobs-search__results-list > li > a[data-control-name=\"job_card_click\"]')].map(link => link.href);")

    driver.quit()

    with open('./Job_Applier/DATA/links.txt', 'w') as fp:
        for link in links:
            fp.write("%s\n" % link)
        print(f'{len(links)} links extracted and saved.')

def main():
    URL = "https://www.linkedin.com/jobs/search?keywords=Full-Stack%20Development&location=India&locationId=&geoId=102713980&f_TPR=&f_E=2&f_WT=2&position=1&pageNum=0"
    scrape_links(URL)

if __name__ == "__main__":
    main()
