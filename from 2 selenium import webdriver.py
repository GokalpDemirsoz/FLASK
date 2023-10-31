from selenium import webdriver
import time



# Firefox sürücüsünün yürütülebilir dosyasının yolunu belirtin
driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')
print("Login...\n")

name = input('Göndereceğiniz Kişinin İsmini Girin: ')

# Kullanıcıdan girişi doğrulamak için hata işleme ekleyin
while True:
    count_input = input('Mesaj Sayısı: ')
    try:
        count = int(count_input)
        break  # Eğer giriş geçerliyse döngüyü kırın
    except ValueError:
        print(".")

msg = input('Mesajınızı Yazın: ')

# QR kodu okuyana kadar bir süre bekleyin
input("Lütfen WhatsApp QR kodunu tarayın ve Enter tuşuna basın.")

# Kişi/grup arama kutusunu bulun
search_box = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]')
search_box.send_keys(name)

# Beklemek için bir süre ekleyin
time.sleep(2)

# Kişiyi/grubu bulun ve tıklayın
user = driver.find_element_by_xpath(f'//span[@title="{name}"]')
user.click()

# Mesaj kutusunu bulun
msgBox = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]')

# Mesajları gönderin
for i in range(count):
    msgBox.send_keys(msg)
    sendButton = driver.find_element_by_xpath('//button[@class="_2Ujuu"]')
    sendButton.click()
    time.sleep(1)  # Mesaj gönderimi arasında kısa bir süre bekleyin

# İşiniz bittiğinde sürücüyü kapatın
driver.quit()
