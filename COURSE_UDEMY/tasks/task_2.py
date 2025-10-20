url = 'youtube.com'

if 'www' not in url:
    url = 'https://www.' + url
elif 'https://' not in url:
    url = 'https://' + url

print(url)