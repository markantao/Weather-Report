import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.X0PAqMhKhjU')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
#print(week)

items = (week.find_all(class_='tombstone-container'))
#print(items[0])

# Getting the items just in text
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

# For loop so that it runs through each item and then it will print out the period names.
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
#print(period_names)
#print(short_descriptions)
#print(temperatures)


weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
        'temperatures': temperatures,
    })
print(weather_stuff)

# Changing to csv so that we can make a spreadsheet
weather_stuff.to_csv('weather.csv')

