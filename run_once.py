def main():
    from ai_briefing import generate_ai_briefing
    from telegram_sender import send_telegram_message

    report = generate_ai_briefing()
    send_telegram_message(report)

if __name__ == "__main__":
    main()
