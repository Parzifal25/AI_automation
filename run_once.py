<<<<<<< HEAD
from ai_briefing import generate_ai_briefing
from telegram_sender import send_telegram_message

def main():

    report = generate_ai_briefing()

    send_telegram_message(report)

if __name__ == "__main__":
    main()
=======
def main():
    from ai_briefing import generate_ai_briefing
    from telegram_sender import send_telegram_message

    report = generate_ai_briefing()
    send_telegram_message(report)

if __name__ == "__main__":
    main()
>>>>>>> fba49e2ed82e3084ce601d978ebec102dcec0d6f
