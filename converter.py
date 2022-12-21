file = open('main.py', 'r', encoding='utf-8')
a = (file.read())
old = "driver.find_element_by_xpath("
old2 = "            u"
new ="driver.find_element(By.XPATH,"
new2 = " "
a = str(a)
a = a.replace(old, new)
a = a.replace(old2, new2)
file = open('main.py', 'w', encoding='utf-8')
print(a)
file.write(a)