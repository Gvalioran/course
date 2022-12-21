"""#int
number = 10
#float
price = 100.5
#str
name = "Seld"
#boll
status = True
status1 = False
Типы переменных  и комментарии # - Однострочный комментарий """
""" многострочный комментарий """
"""
name = 'Manua'
sum = 150
print('Hi,'+ name) # Канкатанация (совмещение переменных)
print("I have " + str(sum)) #Преобразование типов переменных для совмещения(type casting)
print(' Hi, cod open the door \'1234\'') # Для того чтобы не распознавалось завершение строки ставим \текст\ (экранирование) """
"""# print('Good \n day') #Переход на след строку
# print('Good \t day') #Табуляция
# f строки
name = 'Gruha'
weather = 'Дубачелло'
sum = 00.5
print(f'Hi,{name}! you have ${sum} and on street {weather}')"""
# weight = input() # Запрос данных
# print(f'You weight {weight}')
# import random

# print(random.randint(1,5))
# +, -, *, /, // без остатка,** возв в степень, % деление по модулю,-a унарный минус, округление, Пи
"""a = 5
print(5 + a)
print(a % 5)# деление по модулю
print(-a) #унарный минус или инверсия знака числа
print(round(a))#округлени по общим правилам в большу сторону
#iport math библиотека математических функций math.floor в мерьшую сторону math.ceil в большую сторону
# math.pi число пи"""
"""import random
a = random.randint(1,5)
print(f'Give me a number from 1 to 5')
print(a)
b = input()
if int(a) == int(b): # ==(равенство) >= больше или равно
    print("Well done!")
else:
    print("Fail")
if int(a) == int(b) and b <= 5: # and or и или
    print("Well done!")
else:
    print("Fail")"""
# Глава вторая каркулятор
"""from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.CYAN)
a = float(input(f"Give me number 1= "))
b = float(input(f"Give me number 2= "))
operation = input('Select operation (+,-,*,/) ')
result = 0
if operation == '+':
    result = a + b
    print(f'result {result}')
elif operation == "-": #дополнительные условия
    result = a - b
    print(f'result {result}')
elif operation == "*":
    result = a * b
    print(f'result {result}')
elif operation == "/":
    result = a / b
    print(f'result {result}')
else:
    print("incorrect operation")"""
# Применение библеотек
"""import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.CYAN)
expr = input("Give operation ")
result = numexpr.evaluate(expr)
print(f'result {result}')
input()"""
# Глава 3 телеграмм бот
# import the module
"""import python_weather
import asyncio
import os
async def getweather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather = await client.get("Moskow")
        celsius = (weather.current.temperature -32) / 1.8
        print(str(round(celsius)) + "*")
        #for forecast in weather.forecasts:
       #     print(forecast.date, forecast.astronomy)
         #   for hourly in forecast.hourly:
          #      print(f' --> {hourly!r}')
if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather())"""
import asyncio
import os
from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="5840102073:AAFB8tcwHuw-QCnrqKfoI8V3hWpxdJk0UWg")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL)



@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)
    celsius = (weather.current.temperature - 32) / 1.8

    resp_msg = f'Температура в этом городе ', round(celsius)

    await message.answer(str(resp_msg))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)