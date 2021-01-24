# 這是一個密碼重試的程式
# password = 'a123456'
# 讓使用者最多輸入3次密碼
# 如果正確  就印出"登入成功!"
# 如果不正確  就印出"密碼錯誤! 還有__次機會!"
password = 'a123456'
input_chance = 3

while input_chance > 0:
	input_password = input('請輸入密碼: ')
	if input_password == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		input_chance = input_chance - 1
		print('密碼錯誤! 還有', input_chance, '次機會!')