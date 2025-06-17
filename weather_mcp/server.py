import requests
from fastmcp import FastMCP

mcp = FastMCP("Weather", dependencies=["requests"])

def get_lat_lon(city):
    city_coords = {
        "서울": (37.5665, 126.9780),
        "부산": (35.1796, 129.0756),
        "대구": (35.8714, 128.6014),
        "인천": (37.4563, 126.7052),
        "광주": (35.1595, 126.8526),
        "대전": (36.3504, 127.3845),
        "울산": (35.5384, 129.3114),
        "수원": (37.2636, 127.0286),
        "창원": (35.2285, 128.6811),
        "고양": (37.6584, 126.8320)
    }
    if city in city_coords:
        return city_coords[city]
    else:
        return None

@mcp.tool()
def get_weather(city="서울"):
    """Get weather information using Open-Meteo API."""
    latitude, longitude = get_lat_lon(city)
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,weather_code&timezone=GMT&forecast_days=1'
    try:
        response = requests.get(url)
        weather_data = response.json()
        return weather_data
    except Exception as e:
        print("날씨 정보 요청 오류:", e)
        return None

def main():
    mcp.run()

if __name__ == "__main__":
    main()
