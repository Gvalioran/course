from selenium import webdriver  # Импорт вебдрайвера
from selenium_stealth import stealth  # Импорт оболочки для селениум
from selenium.webdriver.common.keys import Keys  # Импорт ключей ввода клавиш с клавиатуры
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()  # Подключение опций драйвера
option.add_argument("start-maximized") #Максимальное разрешение
option.add_experimental_option("excludeSwitches", ["enable-automation"]) #Опции для сокрытия автоматизации
option.add_experimental_option("useAutomationExtension", False) #Опции для сокрытия автоматизации

option.headless = False #Опция работы браузера в фоновом режиме
browser = webdriver.Chrome(options=option)  # Ввод опций
stealth(browser,
        languages=["em-US", "EN"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        ) #Настройки для теневого входа

browser.get('https://chrome.google.com/')  # Открываем страницу
browser.get('https://www.youtube.com/')  # Открываем страницу
browser.refresh()  # Перезапускаем страницу браузера
html = browser.find_element(By.TAG_NAME, 'html')  # Присваиваем переменной html команду поиска на странице  по имени тега html
for i in range(50):  # Цикл иммитации прокрутки браузера вниз
    html.send_keys(Keys.DOWN)
loginin = ('#buttons > ytd-button-renderer > yt-button-shape > a > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill')  # CSS селектор элемента на странице загоняем в переменную
browser.find_element(By.CSS_SELECTOR, loginin).click()
loginin = ('#identifierId')  # CSS селектор элемента на странице загоняем в переменную
browser.find_element(By.CSS_SELECTOR, loginin).send_keys("12345")  # Ввод логина ютуб
browser.save_screenshot('1.png')  # Делаем скрин
browser.get('https://mynickname.com/generate')  # Открываем страницу

 #Запускаем нажатие кнопки сгенерировать никнейм
batton_css = ("#generate") #css селектор кнопки сгенерировать
browser.find_element(By.CSS_SELECTOR, batton_css).click() # Жмем кнопку сгенерировать

link = browser.find_element(By.CSS_SELECTOR, '#register').get_attribute('href')[36:] #Присваиваем переменной сгенерированую строку
print(f'Nickname: {link}') # Выводим результаты

#Изменение юзер агента для сайта только мозила
"""option = webdriver.ChromeOptions()
option.set_preference('general.useragent.override', 'fuck sistem')
browse = webdriver.Chrome(options=option)"""


browser.quit()  # Закрываем браузер