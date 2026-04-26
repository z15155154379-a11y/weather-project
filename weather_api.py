import requests
import csv

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 35,
    "longitude": 139,
    "hourly": "temperature_2m"
}

response = requests.get(url, params=params)

# 检查请求是否成功
if response.status_code != 200:
    print("请求失败:", response.status_code)
    exit()

data = response.json()

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

with open("weather.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "temperature"])

    for t, temp in zip(times, temps):
        writer.writerow([t, temp])

print("✅ 数据已保存到 weather.csv")