search= ("chocolat")
target= ("du chocolat, bla bla du chocolat, et encore du chocolat")
def find_second(search, target):
  start_link=target.find(search)
  s=target.find(search, start_link+1)
  return s

print (find_second(search, target))

































































