from flask import Flask, render_template, request, session, redirect, url_for
from flask import session


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
def index():
    # Kullanıcı giriş yapmışsa home.html sayfasına yönlendir
    if is_logged_in():
        return redirect(url_for('home'))
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in users and users[email] == password:
            # Başarılı giriş, kullanıcıyı oturumuna ekleyin
            session["user"] = email

            # Kullanıcı index sayfasına yönlendir
            return redirect(url_for('index'))
        else:
            # Hatalı giriş, hata mesajıyla birlikte index sayfasına yönlendirin
            return redirect(url_for('index', error='Invalid email or password'))

@app.route('/home')
def home():
    # Kullanıcı giriş yapmışsa home.html sayfasına yönlendir
    if is_logged_in():
        return render_template('home.html')
    else:
        # Kullanıcı giriş yapmamışsa index sayfasına yönlendir
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Kullanıcıyı oturumdan çıkartın
    session.pop("user", None)
    return redirect(url_for('index'))

@app.route('/4000')
def page_4000():
    return render_template('4000.html')

@app.route('/1000')
def page_1000():
    return render_template('1000.html')

@app.route('/2100')
def page_2100():
    return render_template('2100.html')

@app.route('/5321')
def page_5321():
    return render_template('5321.html')



if __name__ == '__main__':
    app.run(debug=True)



