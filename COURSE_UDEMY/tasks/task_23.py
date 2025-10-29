"""Зробити атрибути protocol, domain, bread_crumbs приватними.
Додати метод is_secure, який повертає True якщо протокол із шифруванням (https), якщо http, то False.
Додати метод just_domain, який видалить з об'єкта всю інформацію про "хлібні крихти".
"""

example_url = "https://www.udemy.com/python-full-course"
class URL:
    def __init__(self, url):
        self.url = url
        if "://" in self.url:
            self.__protocol, remainder = self.url.split("://", 1)
        else:
            self.__protocol = None
            remainder = self.url
        if "/" in remainder:
            self.__domain, bread_crumbs = remainder.split("/", 1)
            self.__bread_crumbs = "/" + bread_crumbs if bread_crumbs else None
        else:
            self.__domain = remainder
            self.__bread_crumbs = None
    def get_protocol(self):
        return self.__protocol
    def get_domain(self):
        return self.__domain
    def get_bread_crumbs(self):
        return self.__bread_crumbs
    def is_secure(self):
        if self.__protocol == 'https':
            return True
        elif self.__protocol == 'http':
            return False
    def just_domain(self):
        if self.__bread_crumbs:
            self.url = self.url[:self.url.index(self.__bread_crumbs)]
            self.__bread_crumbs = None
        return self
    def __str__(self):
        return self.url
x =URL(example_url)
print(x.url)
