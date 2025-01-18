import requests
import re
import random
import time
import user_agent
import string
from fake_useragent import UserAgent
import base64
from bs4 import BeautifulSoup
from faker import Faker
def pp(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#saoud
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()