listes=[1,2,3,4,5,6,7,8,10,9]
def greatest(list):
	s=0
	for e in list:
		if s<e:
			s=e
		else:
			break
	return s
print (greatest(listes))