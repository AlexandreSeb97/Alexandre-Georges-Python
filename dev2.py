page = ('"<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="/">"')
start_link =  ("<a href=")

print (page.find(start_link))
print (page.find(start_link, 150))