'''
import scrapy
import json
from ..items import ImagesItem
class ImageSpiderSpider(scrapy.Spider):
    name = "image_spider"
    #allowed_domains = ["www.google.com"]
    start_urls = [
        #'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q=intext:"kevin+hart"+site:facebook.com'
        'https://www.google.com/search?q=intext%3A%22kevin-+hart%22+site%3Afacebook.com&tbm=isch&ved=2ahUKEwid8a7NxNGAAxXkoUwKHYKcCjsQ2-cCegQIABAA&oq=intext%3A%22kevin-+hart%22+site%3Afacebook.com&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BggAEAgQHjoLCAAQgAQQsQMQgwE6CAgAELEDEIMBOgQIABADOgcIABCKBRBDOgoIABCKBRCxAxBDOggIABCABBCxA1D3CVi2mwNgkKoDaANwAHgFgAGqBIgBmmOSAQoyLTM3LjQuNS4xmAEAoAEBqgELZ3dzLXdpei1pbWewAQDAAQE&sclient=img&ei=Vo3UZJ3uOOTDsgKCuarYAw&bih=968&biw=1848&client=ubuntu&hs=JfX#imgrc=wKiOf0hBjbWKIM'
        'https://www.google.com/search?client=ubuntu&hs=JfX&channel=fs&q=famous+persons+images&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiZyfzirMKAAxXiVaQEHcITCaEQ0pQJegQICBAB&biw=1848&bih=968&dpr=1',
        'https://www.google.com/search?q=malcolm+x&tbm=isch&source=lnms&sa=X&ved=2ahUKEwi_jP_B88eAAxXi1AIHHdzMAToQ0pQJegQIDBAB&biw=1848&bih=944&dpr=1',
        'https://www.google.com/search?q=clint+eastwood&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjlrse-1siAAxVB4qQKHfmqDs8Q0pQJegQIDRAB&biw=1848&bih=944&dpr=1',
        'https://www.google.com/search?q=imran+khan&tbm=isch&ved=2ahUKEwi3rem_1siAAxWbmycCHSD4C9cQ2-cCegQIABAA&oq=imran+&gs_lcp=CgNpbWcQARgAMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAgAELEDEIMBMggIABCxAxCDATIFCAAQgAQyCAgAELEDEIMBMggIABCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMggIABCxAxCDAToKCAAQigUQsQMQQzoHCAAQigUQQzoICAAQgAQQsQM6BAgAEANQrAJYwzZg-ztoAHAAeAGAAc0CiAG8HZIBBzAuMS45LjWYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAMABAQ&sclient=img&ei=JOjPZLeLLJu3nsEPoPCvuA0&bih=944&biw=1848',
        'https://www.google.com/search?q=tom+cruise&tbm=isch&ved=2ahUKEwjzlo_r1siAAxXjsEwKHTI_DFAQ2-cCegQIABAA&oq=tom+cr&gs_lcp=CgNpbWcQARgAMgoIABCKBRCxAxBDMg0IABCKBRCxAxCDARBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDOgUIABCABDoICAAQgAQQsQNQ9gpY1R1g_iNoAHAAeACAAYECiAGEE5IBBDItMTGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=f-jPZLPbH-PhsgKy_rCABQ&bih=944&biw=1848',
        'https://www.google.com/search?q=johnny+depp&tbm=isch&ved=2ahUKEwjK153u1siAAxXOmScCHew2A7EQ2-cCegQIABAA&oq=john&gs_lcp=CgNpbWcQARgAMgoIABCKBRCxAxBDMg0IABCKBRCxAxCDARBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgoIABCKBRCxAxBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDOgQIABAeOgUIABCABFDQA1jTHWDbJGgBcAB4BIAB5QGIAbESkgEEMi0xMZgBAKABAaoBC2d3cy13aXotaW1nsAEAwAEB&sclient=img&ei=hujPZMr8As6znsEP7O2MiAs&bih=944&biw=1848'
    ]
    def parse(self, response):
        items = ImagesItem()
        #image_urls = response.xpath('//img/@src').extract()
        #image_urls = response.xpath('//img[not(contains(@src, ".gif"))]/@src').extract()
        image_urls = response.xpath('//a[@role="link"]//img[1][not(contains(@src,".gif"))]/@src').extract()
        for img_url in image_urls:
            items = ImagesItem()
            items['image_urls'] = [img_url]
            yield items
'''            

import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os
from PIL import Image
import io
import hashlib
from ..items import ImagesItem            
            
class ImageSpiderSpider(scrapy.Spider):
    name = 'image_spider'
    start_urls = ['https://www.google.com/']  # Replace with your starting URL

    def __init__(self, *args, **kwargs):
        super(ImageSpiderSpider, self).__init__(*args, **kwargs)
        self.wd = webdriver.Edge()  # Change the webdriver as needed
        self.num_of_images = 5  # Number of images to scrape
    
    
    def fetch_image_urls(self,query):
        def scroll_to_end(wd):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)    
    
        # build the google query
        search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

        # load the page
        self.wd.get(search_url.format(q=query))
        image_urls = set()
        image_count = 0
        results_start = 0
        while image_count < self.num_of_images:
            scroll_to_end(self.wd)

            # get all image thumbnail results
            thumbnail_results = self.wd.find_elements(By.CLASS_NAME,"Q4LuWd")
            number_results = len(thumbnail_results)
        
            print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
            for img in thumbnail_results[results_start:number_results]:
                # try to click every thumbnail such that we can get the real image behind it
                try:
                    img.click()
                    time.sleep(1)
                except Exception:
                    continue

                # extract image urls    
                actual_images = self.wd.find_elements(By.CLASS_NAME,'r48jcc')
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))

                image_count = len(image_urls)

                if len(image_urls) >= self.num_of_images:
                    print(f"Found: {len(image_urls)} image links, done!")
                    break
                else:
                    print("Found:", len(image_urls), "image links, looking for more ...")
                    time.sleep(30)
                    return
                    load_more_button = self.wd.find_element(By.CSS_SELECTOR,".mye4qd")
                    if load_more_button:
                        self.wd.execute_script("document.querySelector('.mye4qd').click();")

                # move the result startpoint further down
                results_start = len(thumbnail_results)

            return image_urls
    
    def persist_image(self, folder_path:str,file_name:str,url:str):
        try:
            image_content = requests.get(url).content

        except Exception as e:
            print(f"ERROR - Could not download {url} - {e}")

        try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            # Get the original dimensions
            width, height = image.size
            min_size = 1000
            if width < height:
                new_width = min_size
                new_height = int((min_size / width) * height)
            else:
                new_height = min_size
                new_width = int((min_size / height) * width)
            image = image.resize((new_width, new_height), Image.LANCZOS)

            folder_path = os.path.join(folder_path,file_name)
            if os.path.exists(folder_path):
                file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
            else:
                os.mkdir(folder_path)
                file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            print(f"SUCCESS - saved {url} - as {file_path}")
        except Exception as e:
            print(f"ERROR - Could not save {url} - {e}")
    
    
    def parse(self, response):
        # Example: Scraping search queries from the website
        queries = ["Malcolm X","clint eastwood","Hasan al banna","Tom cruise"]

        for query in queries:
            #search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
            self.wd.get('https://google.com')#search_url.format(q=query))
            search_box = self.wd.find_element(By.NAME,'q')
            search_box.send_keys(query)
            links = self.fetch_image_urls(query)
            images_path = 'images'

            for link in links:
                #items = ImagesItem()
                #items['image_urls'] = [link]
                #yield items
                self.persist_image(images_path, query, link)

        self.wd.quit()

            
    
    
    
    
    '''
    start_urls = ["https://www.google.com/search?sca_esv=562432527&rlz=1C1BNSD_enPK971PK971&q=ayrton+senna&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjro-WQkJCBAxUPTKQEHeMhA00Q0pQJegQIDRAB&biw=1536&bih=747&dpr=1.25"]

    def parse(self, response):
        # Extract the JSON data containing image URLs
        data = json.loads(response.xpath('//script[@id="islrg"]//text()').get())

        # Extract image URLs from the JSON data
        image_urls = [item['ou'] for item in data['data']]

        # Yield the image URLs
        for img_url in image_urls:
            yield {'image_url': img_url}
'''

