import requests
import re


def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text


def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})


url = input('Enter Instagram URL: ')
response = get_response(url)

vid_matches = re.findall('"video_url":"([^"]+)"', response)
pic_matches = re.findall('"display_url":"([^"]+)"', response)

vid_urls = prepare_urls(vid_matches)
pic_urls = prepare_urls(pic_matches)

if vid_urls:
    print('Videos Detected:\n{0}'.format('\n'.join(vid_urls)))

if pic_urls:
    print('Pictures Detected:\n{0}'.format('\n'.join(pic_urls)))

if not (vid_urls or pic_urls):
    print('Unrecognized Url')
