import stripe
import time
import telebot
import threading

token = "7810214013:AAGAjs0Qmz2kpDOA7mhoTOD9T14b1rDqU08"
bot = telebot.TeleBot(token, parse_mode="HTML")

def check_sk(message, sk):
    chat_id = message.chat.id
    ko = bot.send_message(chat_id, "Checking Your Sk...")
    
    try:
        stripe.api_key = sk
        start_time = time.time()
        account = stripe.Account.retrieve()
        
        if account['charges_enabled'] and account['payouts_enabled']:
            balance = stripe.Balance.retrieve()
            
            if balance and 'available' in balance and balance['available'] and 'pending' in balance and balance['pending']:
                available_balance = balance['available'][0]['amount'] / 100
                pending_balance = balance['pending'][0]['amount'] / 100
                currency = balance['available'][0]['currency'].upper()
            else:
                available_balance = 0.0
                pending_balance = 0.0
                currency = "N/A"
                
            end_time = time.time()
            msgv = (f"⊗ SK ➺ {sk}\n\n"
                    f"⊗ Response: SK KEY VALID ✅\n"
                    f"⊗ Account is fully verified.\n\n"
                    f"⊗ Currency: {currency}\n\n"
                    f"⊗ Available Balance: {available_balance} {currency}\n\n"
                    f"⊗ Pending Balance: {pending_balance} {currency}\n\n"
                    f"⊗ Time Took: {round(end_time - start_time, 2)} Seconds")
            bot.edit_message_text(chat_id=chat_id, message_id=ko.message_id, text=msgv, parse_mode='HTML')
        else:
            end_time = time.time()
            msg = (f"⊗ SK ➺ {sk}\n"
                   f"⊗ Response: SK KEY DEAD ❌\n"
                   "⊗ Account is not fully verified.\n\n"
                   f"⊗ Time Took: {round(end_time - start_time, 2)} Seconds")
            bot.edit_message_text(chat_id=chat_id, message_id=ko.message_id, text=msg, parse_mode='HTML')
    except stripe.error.AuthenticationError:
        end_time = time.time()
        msgdd = (f"⊗ SK ➺ {sk}\n"
                 "⊗ Response: SK KEY DEAD ❌\n\n"
                 f"⊗ Time Took: {round(end_time - start_time, 2)} Seconds")
        bot.edit_message_text(chat_id=chat_id, message_id=ko.message_id, text=msgdd, parse_mode='HTML')
    except Exception as e:
        end_time = time.time()
        msg_error = (f"An error occurred: {e}\n\n"
                     f"⊗ Time Took: {round(end_time - start_time, 2)} Seconds")
        bot.edit_message_text(chat_id=chat_id, message_id=ko.message_id, text=msg_error, parse_mode='HTML')

@bot.message_handler(commands=["sk"])
def start(message):
    try:
        sk = message.text.split(' ', 1)[1]
        bot.send_message(message.chat.id, "Wait Until Checking Your Sk")
        threading.Thread(target=check_sk, args=(message, sk)).start()
    except IndexError:
        bot.send_message(message.chat.id, "Please provide the SK key after the command.")
        
time.sleep(6)
print("""
البوت اشتغل يعم

@aaka8h
""")
bot.infinity_polling()
