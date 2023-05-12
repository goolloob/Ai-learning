import requests
import time
import ctypes
    
def get_weather():
        # OpenWeatherMap的API密钥
    api_key = '189d434a3384f5583b49d5eb597228af'

    # 获取本地IP地址
    response = requests.get('https://ifconfig.me/ip')
    ip_address = response.text.strip()

    # 使用ipapi.co API查询位置信息
    url = f'https://ipapi.co/{ip_address}/json/'
    response = requests.get(url)
            # 解析JSON数据并获取地理名称
    if response.status_code == 200:
        data = response.json()
        city = data.get('city', '')
        region = data.get('region', '')
        country_code = data.get('country_code', '')
# 请求OpenWeatherMap API获取天气信息
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{region},{country_code}&appid={api_key}&lang=zh_cn&units=metric'
        response = requests.get(url)

        # 解析JSON数据并输出天气信息
        if response.status_code == 200:
            data = response.json()
            weather = data.get('weather', [{}])[0].get('description', '')
            temperature = data.get('main', {}).get('temp', '')
            feels_like = data.get('main', {}).get('feels_like', '')
            humidity = data.get('main', {}).get('humidity', '')
            wind_speed = data.get('wind', {}).get('speed', '')
            wind_direction = data.get('wind', {}).get('deg', '')
            print(f"{city}天气状况：{weather}，当前温度：{temperature}℃，体感温度：{feels_like}℃，湿度：{humidity}%，风速：{wind_speed}m/s，风向：{wind_direction}°")
            return city,weather
        else:
            print("无法获取天气信息")
    else:
        print("无法查询该IP地址的位置信息")

# 每小时执行一次
while True:
    # get_weather()
    data = get_weather()
    a = ['雨','小雨','大雨','阵雨','暴雨']
    b = ['晴']
    if data[1] in a:
        #图片文件的路径
        image_path = "D:\data\Desktop\\noahweb\weather_wallpaper\\rain\\a6b303fe9d150d326e6707f26f21aeff.png"
        # 将图片文件设置为桌面壁纸
        ctypes.windll.user32.SystemParametersInfoA(20, 0, image_path.encode('utf-8'), 0)
    elif data[1] in b:
        #图片文件的路径
        image_path = "D:\data\Desktop\\noahweb\weather_wallpaper\snow\R-C.jpg"
        # 将图片文件设置为桌面壁纸
        ctypes.windll.user32.SystemParametersInfoA(20, 0, image_path.encode('utf-8'), 0)
    else:
        print('失败')
    break
    # time.sleep(60)  # 等待1小时







