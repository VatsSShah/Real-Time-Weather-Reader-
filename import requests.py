import requests
from bs4 import BeautifulSoup

def weather(city):
    city = city.replace(" ", "+")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching in Google...\n")
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()

        print(f"Location: {location}")
        print(f"Time: {time}")
        print(f"Description: {info}")
        print(f"Weather: {weather}°C")
    except IndexError:
        print("Weather information not found.")

print("Enter the city name: ")
city = input()
city = city + " weather"
weather(city)
