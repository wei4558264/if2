# else if 另外如果
age = input("你的年齡是？")
age = int(age)
if age < 13:
	print('你是國小生')
elif age >= 13 and age < 18:
	print('你是中學生')
elif age >= 18 and age <= 22:
	print('你是大學生')
else:
	print('你應該是社會人士了!')
