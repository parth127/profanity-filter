 
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template,request

class FaceBookBot :
    login_basic_url = 'https://mbasic.facebook.com/login'
    login_mobile_url = 'https://m.facebook.com/login'
    payload = {
            'email': "gandhidhwanil28@gmail.com",
            'pass': "Shrikrishnaram@123"
        }    
    def parse_html(self, request_url):
        with requests.Session() as session:
            post = session.post(self.login_basic_url, data=self.payload)
            parsed_html = session.get(request_url)
        return parsed_html

    def post_content(self,post_id,url):
        self.post_ID = int(post_id)
       
        #REQUEST_URL = f'https://mbasic.facebook.com/Treyarch/photos/a.10150344869682724/10158037864662724'
        #REQUEST_URL = f'https://mbasic.facebook.com/Treyarch/photos/a.10150344869682724/10158045170162724'
        REQUEST_URL = url

        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        content = soup.find_all('div', class_ = "_2vj8")
        post_content1 = []
        for lines in content:
            post_content1.append(lines.text)
        
        post_content1 = ' '.join(post_content1)    
        
        # print(post_content)
        return post_content1
        #return render_template('result_page.html', result="scaraper")

    
#bot = FaceBookBot()
#print(bot.post_content("4948996235154195"))