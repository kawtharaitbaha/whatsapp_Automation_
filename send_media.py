import pywhatkit as kit

def send_image(phone_number, image_path, caption):
    kit.sendwhats_image(phone_number, image_path, caption)
