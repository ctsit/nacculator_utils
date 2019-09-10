
import sys
import time
import ConfigParser
import pyautogui
import shutil
from selenium import webdriver

def download_excel(driver):
     excel = driver.find_element_by_name("excel_x")
     driver.execute_script("(arguments[0]).click();", excel)
     driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]/select/option[62]").click()
     driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]/p/input[1]").click()
     driver.implicitly_wait(60)
     driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]/a").click()
     pyautogui.hotkey('ctrl', 's')
     time.sleep(5)
     time.sleep(5)
     pyautogui.hotkey('enter')
     return
    

def read_config(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    return config

def replace_link(element, username, password):
    link = element.get_attribute('href')
    link = link.replace("https://","")
    link  = "https://"+username+":"+password+"@"+link
    return link

def main(argv):
    config = read_config("packet_config_example.ini")
    try:
        username = config.get('credentials','username')
        password = config.get('credentials','password')
        downloadpath = config.get('downloadpath', 'path')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
          "download.default_directory": downloadpath,
          "download.prompt_for_download": False,
          "download.directory_upgrade": True,
          "safebrowsing.enabled": True,
          "plugins.always_open_pdf_externally": True
        })

        
        driver = webdriver.Chrome(chrome_options = options)
        # Sign In credentials along with nacc url
        str = "https://"+username+":"+password+"@www.alz.washington.edu/MEMBER/sitesub.htm"
        driver.get(str)
        # Get the 1Florida ADRC project url
        nacc_project_elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]/font/ul[1]/li[5]/a")
        florida_adrc_link = replace_link(nacc_project_elem, username, password)
        driver.get(florida_adrc_link)
        # get the uds link
        uds_project = driver.find_element_by_xpath("//*[@id='m_3subsystem_graphicC']/area[1]")
        uds_link = replace_link(uds_project, username, password)
        # Navigate to uds link
        driver.get(uds_link)
        uds_nacc_results = driver.find_element_by_xpath("//*[@id='bodytable']/form/font/b/button").click()
        

        print "Downloading Excel file"

        download_excel(driver)

        driver.close()

        

    except Exception as e:
        print(e)
        

        # driver.close()


if __name__ == '__main__':
    main(sys.argv[0])
