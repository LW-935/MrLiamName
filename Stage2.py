import requests
from datetime import datetime

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    bot_token = "6715587533:AAFAroET16pO4odIrm6EZK6R1kl9Vtu8ZNM"  # Replace with your Telegram bot token
    chat_id = "-4186941317"      # Replace with your chat ID

    # Custom message with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    custom_message = f"Execution confirmed at {timestamp}"
    
    # Send the message
    result = send_telegram_message(bot_token, chat_id, custom_message)
    print(result)
