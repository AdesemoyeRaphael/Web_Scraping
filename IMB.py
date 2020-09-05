import scrapy
import pandas as pd
import numpy as np
import re



class imb(scrapy.Spider):
	name = 'imb'
	start_urls = ['https://www.accaglobal.com/uk/en/member/find-an-accountant/find-firm/results.html?isocountry=GB&location=London&country=UK&firmname=&organisationid=ACCA&pagenumber=1&resultsperpage=25&requestcount=1&hid=']
	x = 1


	def parse(self,response):

		company = response.css(".detailsLink::attr(href)").extract()

		yield {'Company':company}



data = pd.read_csv('firmlinks.csv')
for x in data['Company']:
	y = x.split(",")

l=len(y)




class imb(scrapy.Spider):
	name = 'imb'
	z = y
	start_urls = ['https://www.accaglobal.com/uk/en/member/find-an-accountant/find-firm/results/details.html?isocountry=GB&location=London&country=UK&firmname=&organisationid=ACCA&pagenumber=1&resultsperpage=25&requestcount=1&hid=&advisorid=2841946']
	x = 1


	def parse(self,response):
		try:
			address = response.css(".firm-details-contact address::text").extract()
		except AttributeError :
			address = np.nan
		try:
			email = response.css("li:nth-child(1) .no-external::text").extract()
		except AttributeError:
			email = np.nan
		try:
			phone_num = response.css(".firm-details-panel li:nth-child(3)::text").extract()
		except AttributeError:
			phone_num = np.nan

		try:
			partner = response.css("address~ ul li::text").extract()
		except AttributeError:
			partner = np.nan

		yield {'Address':address,
			   'Email':email,
			   'Phone Number': phone_num,
			   'Firm Partner': partner}

		next_page = 'https://www.accaglobal.com'+imb.z[imb.x]
		if imb.x < l:
			imb.x +=1
			yield response.follow(next_page,callback=self.parse)


data = pd.read_csv('scrapyresult.csv')
print(data['Address'])
for x in data['Address']:
	x=x.strip()
	x = re.sub('\s+',' ',x)
	print(x)

Address =[]
data = pd.read_csv('firm.csv')
print(data['Address'])
for x in data['Address']:
	x=x.strip()
	x = re.sub('\s+',' ',x)

	def rewrite(text,there=re.compile(re.escape(', ')+'*')):
		return there.sub(' ',text)

	y=rewrite(x)
	Address.append(y)
# print(Address)

data['Address'] = Address
# print(data['Address'])

print(data['Firm Partner'])

print(data)

data.to_csv("Firm INFO.csv",index = False)
