from bs4 import BeautifulSoup
import requests

class Instagram:
    def get_page(self,user_name):
        try:
            r = requests.get("https://www.instagram.com/"+user_name)
        except Exception as ex:
            print("Failed to get instagram account")
            r = None
        return r

instaobj = Instagram()
username = "saurav_mgr"
page_resp = instaobj.get_page(username)
print("status code" , page_resp.status_code)
# print("text : ",page_resp.text)
