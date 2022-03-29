import services.startDriver
import os
import traceback

global target_site
target_site = "facedrivesupply"

def find_rank(driver, term):
    search_bar = driver.find_element_by_css_selector('input[name="q"]')
    search_bar.send_keys(term + "\n")
    
    rank = None
    
    while not rank:
        try:
            next_pg = driver.find_element_by_id("pnnext")
        except:
            next_pg = None
            
        try:
            all_page_no = driver.find_element_by_css_selector('div[role="navigation"] table[role="presentation"]')
        except:
            all_page_no = None
        
        results = driver.find_element_by_id("res")
        
        if target_site in results.text():
            if not all_page_no:
                rank = 1
            else:
                rank = all_page_no.find_element_by_class_name("YyVfkd").text()
                
        else:
            if next_pg:
                next_pg.click()
            else:
                rank = "*NOT FOUND*"
    
    return rank
    
def run():
    os.system('clear')
    
    term = input("Search Query: ")
    
    driver = services.startDriver.start()

    google_url = 'https://www.google.com/'
    
    driver.get(google_url)
    
    try:
        input("Found on: " + str(find_rank(driver, term)) + "\nPress enter to continue...")
    except:
        print(traceback.format_exc())
    finally:
        driver.close()

if __name__ == "__main__":
    run()
