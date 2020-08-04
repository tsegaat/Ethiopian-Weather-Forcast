from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame

html = get("https://weather.com/weather/tenday/l/Addis+Ababa+Addis+Ababa+Ethiopia?placeId=f890160b83d5f985b270195431638541ad2c9fb5bc40db1428c449078c223b84")
bsObj = BeautifulSoup(html.content, "html.parser")

Dates_not_fixed = bsObj.find_all(class_ = "_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc")
Tempratures_not_fixed = bsObj.find_all(class_ = "_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp")
Description_not_fixed = bsObj.find_all(class_ = "_-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax")

Dates = [Date.get_text()for Date in Dates_not_fixed]
Tempratures = [Temprature.get_text()for Temprature in Tempratures_not_fixed]
# Descriptions = []


weather_deatils = DataFrame({
    "Days": Dates,
    "Temprature": Tempratures,
})

weather_deatils.to_csv("weather.csv")