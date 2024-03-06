import telepot
import time
import RPi.GPIO as GPIO  # We use the Raspberry Pi GPIO library to read the GPIO pin to which the power failure sensor is connected

# Set the GPIO pin to which the power failure sensor is connected
GPIO_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Add your Telegram bot's token here
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'  # Telegram user or group chat ID to send notifications to

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)

def send_telegram_message(message):
    bot.sendMessage(CHAT_ID, message)

def check_power_outage():
    while True:
        try:
            if GPIO.input(GPIO_PIN) == GPIO.LOW:
                send_telegram_message("Power outage detected!")
            time.sleep(10)  # Check every 10 seconds
        except KeyboardInterrupt:
            GPIO.cleanup()
            break

if __name__ == "__main__":
    try:
        check_power_outage()
    except Exception as e:
        print("Error:", str(e))
        GPIO.cleanup()
