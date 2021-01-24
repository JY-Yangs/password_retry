# 這是一個密碼重試的程式
# password = 'a123456'
# 讓使用者最多輸入3次密碼
# 如果正確  就印出"登入成功!"
# 如果不正確  就印出"密碼錯誤! 還有__次機會!"
password = 'a123456'
input_chance = 3

while True: #不一定要寫"while True", 也可寫"while input_chance > 0:"
	input_password = input('請輸入密碼: ')
	if input_password == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		input_chance = input_chance - 1
		print('密碼錯誤! 還有', input_chance, '次機會!')
		if input_chance == 0: # 前面如果寫while input_chance > 0:可以不用寫這兩行, 因為條件不合後就部會在進入迴圈
			break # 前面如果寫while input_chance > 0:可以不用寫這兩行, 因為條件不合後就部會在進入迴圈
		