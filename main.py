from send_message import send_text_message
from send_media import send_image
from interact import reply_to_message
import schedule
import time

def main():
    # Planification de l'envoi de messages
    schedule.every().day.at("15:30").do(send_text_message, "+1234567890", "Bonjour, ceci est un message automatisé", 15, 30)
    schedule.every().day.at("16:00").do(send_image, "+1234567890", "path/to/image.jpg", "Ceci est une image automatisée")

    # Exécution de la planification
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
