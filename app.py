from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'https://valuation.homify.com.vn/RealEstatePriceService/landprice'
post_fields = {'cuoi':'','dau':'','diadiem':'HN','dientich':'80','duong':'Cầu Giấy','loaiBDS':'D','loaiduong':'D','mattien':'','nam':'2016','phuong':'Quan Hoa','quan':'Cầu Giấy'}
request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)