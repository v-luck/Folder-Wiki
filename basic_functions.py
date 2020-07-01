import os
from datetime import datetime

class page():
    def __init__(self, title, date_created, location):
        self.title = title
        self.date_created = date_created
        self.location = location

created_page = page(input("Input a title:"), datetime.now(tz=None), os.getcwd())

print(created_page.title)





