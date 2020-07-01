from basic_functions import page
import os
from datetime import datetime

created_page = page(input("Input a title:"), datetime.now(tz=None), os.getcwd())
os.mkdir(created_page.title)
open("{}.txt".format(created_page.title), "x")






