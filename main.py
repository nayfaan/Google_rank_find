import services.startDriver
import os
import traceback

def find_rank(driver, term):
    search_bar = driver.find_element_by_css_selector("input[aria-label=Search]")
    search_bar.send_keys(term + "\n")
    
    return 0
    
def run():
    os.system('clear')
    
    term = input("Search Query: ")
    
    driver = services.startDriver.start()

    google_url = 'https://www.google.com/'
    
    driver.get(google_url)
    
    try:
        input("Search Query: " + str(find_rank(driver, term)))
    except:
        print(traceback.format_exc())
    finally:
        driver.close()

if __name__ == "__main__":
    run()
