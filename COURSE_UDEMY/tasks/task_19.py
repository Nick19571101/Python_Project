urls = ["https://www.udemy.com/python-full-course",
        "https://www.udemy.com",
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.youtube.com/shorts",
        "https://www.youtube.com/feed/subscriptions"
        ]
class URL:
    def __init__(self, url):
        self.url = url

        if "://" in self.url:
            self.protocol, remainder = self.url.split("://", 1)
        else:
            self.protocol = None
            remainder = self.url
        if "/" in remainder:
            self.domain, bread_crumbs = remainder.split("/", 1)
            self.bread_crumbs = "/" + bread_crumbs if bread_crumbs else None
        else:
            self.domain = remainder
            self.bread_crumbs = None

    def get_protocol(self):
        return self.protocol

    def get_domain(self):
        return self.domain

    def get_bread_crumbs(self):
        return self.bread_crumbs

    def __str__(self):
        return self.url
urls_like_obj = []

for url in urls:
    obj = URL(url)
    urls_like_obj.append(obj)
for i in range(len(urls_like_obj) - 1, -1, -1):
    if urls_like_obj[i].get_bread_crumbs():
        urls_like_obj.pop(i)

print(urls_like_obj)

for item in urls_like_obj:
    print(item)
