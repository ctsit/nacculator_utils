import sys
import os
import datetime
import time

import ConfigParser
import pyautogui
import shutil
from selenium import webdriver


def read_config(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    return config

def upload_file(driver,filepath,email):
    elem1 = driver.find_element_by_name("UPLOADR_X")
    driver.execute_script("(arguments[0]).click();", elem1)
    driver.find_element_by_name("FILEUP").send_keys(filepath)
    driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]/font/center/button").click()

    #Try uploading file
    try:
        print "Attempting to upload: " + filepath
        driver.find_element_by_css_selector("input[type='RADIO'][value='1']").click()
        driver.find_element_by_name("TYPEUP").click()
        driver.find_element_by_name("EMAIL").send_keys(email)
        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]/pre/b/input")
        driver.execute_script("(arguments[0]).click();",elem)
        print "File uploaded Succesfully"
    #Error in input file or upload process
    except:
        print "Errors in uploading file"
    return



def get_nacc_data(driver):
    elem = driver.find_element_by_name("FINCHK_X")
    # Above element is Hidden. To click the hidden element we are making use of Js
    driver.execute_script("(arguments[0]).click();", elem)
    # The getPacket.js fetches data from Nacc
    print("Trying to download")
    driver.execute_script(open("./getpacket.js").read())
    time.sleep(10)
    return


def replace_link(element, username, password):
    link = element.get_attribute('href')
    link = link.replace("https://","")
    link  = "https://"+username+":"+password+"@"+link
    return link


def generate_report(driver):
    elem = driver.find_element_by_name("certc_X")
    # Above element is Hidden. To click the hidden element we are making use of Js
    driver.execute_script("(arguments[0]).click();", elem)
    elem1 = driver.find_element_by_name("TYPEP")
    driver.execute_script("(arguments[0]).click();", elem1)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(5)
    time.sleep(5)
    pyautogui.hotkey('enter')
    return


def main(argv):
    config = read_config("packet_config_example.ini")
    try:
        nacc_options = argv
        username = config.get('credentials','username')
        password = config.get('credentials','password')
        email = config.get('credentials', 'email')
        filepath = config.get('uploadpath','path')
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
        if nacc_options == "upload":
            upload_file(driver,filepath,email)
        if nacc_options == "getdata":
            print("getting data")
            get_nacc_data(driver)
        if nacc_options == "report":
            import parse_report
            generate_report(driver)
            new_filename = downloadpath + '/' + 'broker93_' + datetime.datetime.now().strftime("%Y%m%d") + '.pdf'
            shutil.move(os.path.join(downloadpath, 'broker93.pdf'), new_filename)
            # output_file = config.get('reportpath', 'path') +
            # 'report_' + datetime.datetime.now().strftime("%Y%m%d") + '.csv'
            parse_report.generate_report_csv(new_filename)


        driver.close()

    except Exception as e:
        print e
        if nacc_options == "report":
            import send_email as sm
            msg = 'Failed to generate report. Error: ' + e.msg
            sm.send_email(subject='UDS REPORT', message=msg)

        # driver.close()


if __name__ == '__main__':
    main(sys.argv[1])
