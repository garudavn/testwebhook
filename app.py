from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'https://valuation.homify.com.vn/RealEstatePriceService/landprice'
post_fields = {'cuoi':'','dau':'','diadiem':'HN','dientich':'80','duong':'Cầu Giấy','loaiBDS':'D','loaiduong':'D','mattien':'','nam':'2016','phuong':'Quan Hoa','quan':'Cầu Giấy'}
request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)

# movies.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
  params = {'cuoi':'','dau':'','diadiem':'HN','dientich':'80','duong':'Cầu Giấy','loaiBDS':'D','loaiduong':'D','mattien':'','nam':'2016','phuong':'Quan Hoa','quan':'Cầu Giấy'}
  r = requests.get(
      'https://valuation.homify.com.vn/RealEstatePriceService/landprice',
      params=params)
  return render_template('result.html', movies=json.loads(r.text)['Gia'])

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
