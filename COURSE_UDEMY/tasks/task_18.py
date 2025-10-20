example_url = "https://www.udemy.com/python-full-course"
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
            self.domain =remainder
            self.bread_crumbs = None
    def get_protocol(self):
        return self.protocol
    def get_domain(self):
        return self.domain
    def get_bread_crumbs(self):
        return self.bread_crumbs
x = URL("https://www.udemy.com/python-full-course")
print(x.get_protocol())
print(x.get_domain())
print(x.get_bread_crumbs())
print(x.url)
print(x.protocol)
print(x.domain)
print(x.bread_crumbs)
