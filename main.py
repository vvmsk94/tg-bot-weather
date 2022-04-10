import requests
import datetime
import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="your_tg_token")
open_weather_token = "your_weather_token"
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю прогноз")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r=requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data=r.json()


        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["pressure"]

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе:{city}\n Температура:{cur_weather}\n ***Хорошего дня***")

    except:
        await message.reply("Проверьте название города")

if __name__ == "__main__":
    executor.start_polling(dp)
