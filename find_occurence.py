liste=("un","un","lol","un","monde","python","lol","lol","lol","lol","un","love","rock","rebellion")
numbers=(1,2,1,3,4,2,5,3,1,2,4,6,3,2,1,3,5,7,3,1)
def find_occurence(list):
  s=sorted(list, key=list.count)
  print ("L'élément qui se répète le plus souvent dans cette liste est:")
  n=s[-1]  
  return n 

print (find_occurence(liste))
print (find_occurence(numbers))