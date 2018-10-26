import api_wrapper
import urllib.request
import json

link = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
param = {'sol': 1000, 'api_key': 'XBiB0125PEUUcnBT3LEolXlnqHNwjHm31YViuL2l'}

def json_to_str(link,param):
    data = json.dumps((api_wrapper.get_request(link, param)))
    var = json.loads(data)
    return var

def parse_json(link, param):
    url = []
    i = 0
    data = json_to_str(link, param)
    while i <= 20:
        url.append(data['photos'][i]['img_src'])
        i += 1
    return url

def save_image(link, param):
    images = parse_json(link, param)
    i = 0
    while i <= 20:
        for img in images:
            save = urllib.request.urlopen(img).read()
            out = open('img{}.jpg'.format(i), 'wb')
            out.write(save)
            out.close
            i += 1






print(save_image(link, param))
