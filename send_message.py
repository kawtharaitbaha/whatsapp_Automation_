import pywhatkit as kit

def send_text_message(phone_number, message, hour, minute):
    kit.sendwhatmsg(phone_number, message, hour, minute)
