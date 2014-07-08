phrase=("la vie est un chapelet de petites misères que le philosophe égrène en riant. Soyons philosophe mon ami!")
page=('<a href="http://udacity.com">')
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link!=-1:
     start_quote = page.find('"', start_link)
     end_quote = page.find('"', start_quote + 1)
     url = page[start_quote + 1:end_quote]
     return url
	 
print (get_next_target(page))
print (get_next_target(phrase))


 
  

  
