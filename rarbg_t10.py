from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import time 
from PIL import Image, ImageEnhance, ImageFilter 
from datetime import datetime 
import pytesseract
import os 
import re 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = "https://rarbg.to/top10"
os.chdir('/home/rizwan/Program Files/scripts/rarbgT10/files')



def get_captcha(driver, element, path):
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']
    top = location['y'] 
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'png')  # saves new cropped image




chrome_options = Options()
chrome_options.add_argument('--headless')


driver = webdriver.Chrome(chrome_options=chrome_options) 

try:

    driver.get(url)

    time.sleep(5)

    img_file = driver.find_element_by_xpath('/html/body/form/div/div/table[1]/tbody/tr[2]/td[2]/img')

    now = datetime.now()
    img_name =  './captchas/cap-' + str(now) + ".png"

    get_captcha(driver, img_file, img_name)

    im = Image.open(img_name)

    im = im.convert('L')                            
    im = im.filter(ImageFilter.MedianFilter())       
    im = im.point(lambda x: 0 if x < 140 else 255) 

    captcha_text = pytesseract.image_to_string(im)

    captcha = driver.find_element_by_xpath('//*[@id="solve_string"]')
    captcha.send_keys(captcha_text)
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="button_submit"]').click()
    time.sleep(5)
    driver.get(url)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table[1]/tbody')))

    table_data = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table[1]/tbody')

    movies = []
    for t_data in table_data.find_elements_by_tag_name('tr')[1:]:

        m_name = t_data.find_element_by_css_selector('td:nth-of-type(2)').text
        m_name = m_name.split('\n')[0]
        m_name = m_name.replace(".", " ")

        name = re.compile(r'.*\d{4}\b')
        movie = re.match(name, m_name).group(0)
        

        if movie in open('movies.txt').read():
            pass
            
        else:
            with open('movies.txt','a') as wfile:
                today = datetime.now().date()
                today = today.strftime('%d-%b-%Y')
                wfile.write(movie + ", " + today + "\n")
                movies.append(movie)

    if movies:
        title = "New Movies Arrived"
        os.system('notify-send " '+title+' " " '+'\n'.join(movies)+' " ')


    driver.close()



except Exception as e:
	raise e
	with open('error.txt','a') as wfile:
				wfile.write(e + "\n")