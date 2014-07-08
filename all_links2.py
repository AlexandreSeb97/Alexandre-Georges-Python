website = ("www.google.com")
def print_all_links(page):
	import urllib
	links = urllib.urlopen(page)
	for item in links:
		if "http://" in item:
			return item[item.index("http://"):]
		else:
			break
print (print_all_links(website))
