
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask
# Initialize the Chrome browser


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Güvenlik amacıyla bir anahtar belirtin


# Kullanıcı bilgileri (örnek, gerçek bir veritabanı kullanılması tavsiye edilir)
users = {
    "user1@example.com": "password1",
    "user2@example.com": "password2",
    "ziya@demirsoz.com": "1234",
    "gokalp@ehslogistics.com": "1234",
}

# Kullanıcının giriş yapmış olup olmadığını kontrol eden fonksiyon
def is_logged_in():
    return "user" in session

@app.route('/')
def home():
      # Kullanıcı giriş yapmışsa home.html sayfasına yönlendir
    # if is_logged_in():
    #     return render_template('home.html')
    # else:
    #     return render_template('index.html')

    # chromedriver_path = './pythonProj/FLASK/chromedriver-win64/chromedriver'
    options=Options()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get("https://gbs.gov.ct.tr/dby/detaylibeyanname")
    print("anan3")
    # try:
    #   element_present = WebDriverWait(driver, 10).until(
    #       EC.presence_of_element_located((By.ID, "j_username"))
    #   )
    #   print("Element is present on the page")
    # except TimeoutException:
    #   print("Timed out waiting for element to be present")

# Perform actions with the element, e.g., send keys
    # element_present.send_keys("your_username")

    # # element1=driver.find_element_by_id("j_username")
    # element1.send_keys("harunerhun@me.com")
    # element2=driver.find_element_by_id("j_password")
    # element2.send_keys("HEC2391-ehs1591")

    driver.maximize_window()
    # element = driver.find_element_by_xpath('//*[@id="form:declarationDataTable:j_idt235"]/div[2]/p')
    # print(element.text)

    driver.quit()
    


 
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email in users and users[email] == password:
        # Başarılı giriş, kullanıcıyı oturumuna ekleyin
        session["user"] = email
        return redirect(url_for('home'))
    else:
        # Hatalı giriş, hata mesajıyla birlikte ana sayfaya yönlendirin
        return redirect(url_for('home', error='Invalid email or password'))
@app.route('/fourThousand')
def fourThousand():
    print("anan")
    return render_template('4000.html')

@app.route('/logout')
def logout():
    # Kullanıcıyı oturumdan çıkartın
    session.pop("user", None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
