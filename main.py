import telebot, time, requests
bot = telebot.TeleBot("6435418706:AAHvQrdDhNZrcAG88MrpVBwcw8-kjSPrINQ")
while True:
    try:
        response = requests.get('https://boredhumans.com/api_anime_images.php').text
        img = response.split('<img src=')[1].split('"')[1]
        link = "https://boredhumans.com"+img
        bot.send_photo(chat_id="-1001737756503", photo=link)
    except Exception as e:
        time.sleep(10) #every 2 mins #by:@Teamon404
