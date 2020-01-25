num = 1
while num <= 100:
	if num % 7 == 0 or num % 10 ==7 or num // 10 == 7:
		num += 1
		continue
	else:
		print("shuziwei:{}".format(num))
		num += 1

		
	
