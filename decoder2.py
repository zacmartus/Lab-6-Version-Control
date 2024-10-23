def decode(encrypted):
	arr=""
	for i in arr:
		arr = arr + str((int(i)+7)%10)
	return arr

