# 這是一個密碼重試的程式
# password = 'a123456'
# 讓使用者最多輸入3次密碼
# 如果正確  就印出"登入成功!"
# 如果不正確  就印出"密碼錯誤! 還有__次機會!"
password = 'a123456'
input_chance = 3

while input_chance > 0:
	input_chance = input_chance - 1 #這一行可以寫在最前面, 讓它每進入一次迴圈就扣1
	input_password = input('請輸入密碼: ')
	if input_password == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		if input_chance > 0:
			print('密碼錯誤! 還有', input_chance, '次機會!')
		else: # 把 input_chance = 0 時印出其他的訊息
			print('密碼錯誤! 沒機會嘗試了! 要被鎖帳號啦!')
