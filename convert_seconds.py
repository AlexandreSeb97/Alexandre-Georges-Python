sec = 7200
def convert_seconds(seconds):
	list = []
	mn = seconds//60
	hr = mn//60
	if hr<60:
			list.append(hr)
	else:
		list.append("1 jour")
		
	if mn<60:
		list.append(mn)
	if mn>60:
		list.append(mn)
		list.append("minutes")
	else:
		list.append("0mn")
	return list
print (convert_seconds(sec))
