mois31=[1,3,5,7,8,10,12]
mois30=[4,6,9,11]
mois2=(2)

def  how_many_days(s):
 if s in mois31:
  return (31)
 elif s in mois30:
  return (30)
 elif s ==	mois2:
   return (29)
 else:
   return ("ce mois ne fait pas parti du calendrier")
 
print (how_many_days(2))
print (how_many_days(5))
print (how_many_days(15))