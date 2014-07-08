list=[1,2,3,"georges"]
def find_element(list, input):
 if input in list:
  n= list[input]
  return n 
 else:
  return (-1)
print (find_element(list,1))