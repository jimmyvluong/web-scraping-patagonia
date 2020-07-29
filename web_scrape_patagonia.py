# webscraping tutorial
# ctrl+z exits to regular command line
# https://www.youtube.com/watch?v=XQgXKtPSzUI

# urllib is going to grab the web page
from urllib.request import urlopen as uReq

# BeautifulSoup is going to parse the HTML text
from bs4 import BeautifulSoup as soup

# Save your URL to a variable
my_url = 'https://eu.patagonia.com/gb/en/shop/black-hole-duffel-bags'
# Call the function 'URL open' inside of a module called 'request' inside of a package called 'URL lib'
# Opening up connection, grabbing the page
uClient = uReq(my_url)

# Assign it to variable because once it reads it dumps the page
page_html = uClient.read()
uClient.close()

# Now to parse the HTML
page_soup = soup(page_html, "html.parser")
# Take a look around
page_soup.h1 # Looks at header
page_soup.p # Looks at p type?

# Grabs each product
containers = page_soup.findAll("div", {"class":"product-tile__wrapper col-6 col-lg-6 col-xl-4 col-xxxxl-3"})

filename = "patagonia_products.csv"
f = open(filename, "w")

headers = "product_id, product_name, product_price\n"

f.write(headers)
#container = containers[4]
#container.div.div.a
for container in containers:

	product_id = container.div["data-pid"]
	
	name_container = container.findAll("h4", {"class":"product-tile__name"})
	product_name = name_container[0].text
	
	price_container = container.findAll("span",{"class":"value"})
	price = price_container[0].text.strip()

	print("product_id: " + product_id)
	print("product_name: " + product_name)
	print("product_price: " + price)

	f.write(product_id + "," + product_name.replace("®", "") + "," + price + "\n")
#product_name.replace(",", "|")
f.close()
