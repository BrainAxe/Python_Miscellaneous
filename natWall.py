import requests
from lxml.html import fromstring
from lxml import etree
from datetime import datetime 


def download_national_geographic_wallpaper():
    url = 'http://www.nationalgeographic.com/photography/photo-of-the-day/'
    
    r = requests.get(url)
    if r.status_code == 200:
        doc = fromstring(r.text)
        for meta in doc.cssselect('meta'):
            prop = meta.get('property')
            if prop == 'og:image':
                image_url = meta.get('content')
                print image_url
                r = requests.get(image_url, stream=True)
                print r.status_code
                now = datetime.now()
                fname = 'image-' + str(now) + ".jpg"
                if r.status_code == 200:
                    try:
                        with open(fname, 'wb') as f:
                            for chunk in r.iter_content(1024):
                                f.write(chunk)
                        print "-----Download Complete-------"
                        
                    except Exception as e:
                        print e


if __name__=="__main__":
    download_national_geographic_wallpaper()