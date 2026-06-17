"""
天气查询 CLI
练习点：requests、JSON 解析、API Key 管理（.env）、数据格式化
API 来源：Open-Meteo（完全免费，无需注册 Key）
文档：https://open-meteo.com/en/docs
"""
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WMO_CODES = {
    0: "晴天", 1: "大部晴天", 2: "局部多云", 3: "阴天",
    45: "雾", 51: "小毛毛雨", 61: "小雨", 63: "中雨", 65: "大雨",
    71: "小雪", 73: "中雪", 75: "大雪", 80: "阵雨", 95: "雷雨",
}


def search_city(city_name: str) -> dict | None:
    """用地理编码 API 搜索城市，返回第一个结果（含经纬度）。"""
    # TODO: 请求 GEO_URL，参数：name=city_name, count=1, language=zh
    # TODO: 解析结果，返回 {"name": ..., "latitude": ..., "longitude": ...}
    raise NotImplementedError


def fetch_weather(latitude: float, longitude: float) -> dict:
    """获取当前天气数据。"""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weathercode,windspeed_10m",
        "timezone": "auto",
    }
    # TODO: 请求 WEATHER_URL，返回 response.json()["current"]
    raise NotImplementedError


def format_weather(city: dict, weather: dict) -> str:
    """将天气数据格式化为可读字符串。"""
    code = weather.get("weathercode", 0)
    desc = WMO_CODES.get(code, "未知")
    # TODO: 返回包含城市名、天气描述、温度、湿度、风速的格式化字符串
    raise NotImplementedError


def main():
    city_name = input("请输入城市名（中/英文均可）：").strip()
    if not city_name:
        return

    city = search_city(city_name)
    if not city:
        print(f"未找到城市：{city_name}")
        return

    weather = fetch_weather(city["latitude"], city["longitude"])
    print(format_weather(city, weather))


if __name__ == "__main__":
    main()
