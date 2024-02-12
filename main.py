import time
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook

url = "TamilDhool_Show_URL" # Replace
webhook_url = "Webhook_URL" # Replace

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

def save_title_to_file(title):
    with open('last_title.txt', 'w') as file:
        file.write(title)

def read_title_from_file():
    try:
        with open('last_title.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def send_discord_alert(title):
    print(f"New Episode for {title} is released. ")
    # Send an alert to Discord
    discord_webhook = DiscordWebhook(url=webhook_url, content=f"@everyone\nNew Episode for **{title}** is released.")
    response = discord_webhook.execute()

while True:
    response = requests.get(url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find('h3', class_='entry-title').text
    # print(title)

    last_title = read_title_from_file()

    if title != last_title:
        save_title_to_file(title)
        send_discord_alert(title)

    time.sleep(900)