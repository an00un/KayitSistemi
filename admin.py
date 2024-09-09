from firebase import firebase
import firebase_admin
import flet
from flet import Page, Text, ElevatedButton, TextField, Column
import os
from firebase_admin import credentials, db

cred = credentials.Certificate('serviceAccount.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'firebase_url'
})


isimliste = []

firebase = firebase.FirebaseApplication('firebase_url', None)

bilgisayar_adi = os.getlogin()

def adminsistem(page: Page):

    result = firebase.get('/users/dogrulanmamis', None)

    if result:
        for key in result.keys():
            isimliste.append(key)
            print(key)
    else:
        print("No data found.")

    page.title = "Admin Paneli"

    dogrulanmamiskullanicilar = Text(value=isimliste)

    page.update()

    def onaylab1(e):
        if username.value.strip() in firebase.get(f'admin/', ''):
            if ((username.value.strip() == firebase.get(f'admin/{username.value.strip()}', 'username')) and
                    (int(password.value.strip()) == firebase.get(f'admin/{username.value.strip()}','password'))):
                t1.value = f"Giriş Başarılı, Hoşgeldiniz {username.value.strip()}"
                col.controls = [t1, dogrulanmamiskullanicilar, dogrulakullanici, dogrula]
            else:
                t1.value = "Kullanıcı Adı veya Şifre Hatalı!"
        if username.value.strip() in firebase.get(f'users/dogrulanmis/', ''):
            if (username.value.strip() == firebase.get(f'users/dogrulanmis/{username.value.strip()}', 'username')):
                t1.value = f"Doğrulanmış Hesap. Lütfen Kullanıcı Paneli Üzerinden Giriş Yapınız."
            else:
                t1.value = "Kullanıcı Adı veya Şifre Hatalı!"
        if username.value.strip() in firebase.get(f'users/dogrulanmamis/', ''):
            if (username.value.strip() == firebase.get(f'users/dogrulanmamis/{username.value.strip()}','username')):
                t1.value = f"Doğrulanmamış Hesap. Lütfen Kullanıcı Paneli Üzerinden Giriş Yapınız."
            else:
                t1.value = "Kullanıcı Adı veya Şifre Hatalı!"

        page.update()

    def kullanicidogrula2(e):
        old_ref_path = f'users/dogrulanmamis/{dogrulakullanici.value.strip()}'

        old_data = firebase.get(old_ref_path, None)

        if old_data:
            try:
                firebase.put('/users/dogrulanmis', dogrulakullanici.value.strip(), old_data)

                firebase.delete(old_ref_path, None)
                t1.value = f'{username.value.strip()} | {dogrulakullanici.value.strip()} Adlı Kullanıcı Doğrulandı'
            except Exception as e:
                t1.value = f'{username.value.strip()} | Bir Şeyler Ters Gitti. Lütfen Tekrar Deneyiniz. Hata: {str(e)}'
        else:
            print("Veri bulunamadı.")
        page.update()

    username = TextField(label="Kullanıcı Adı", hint_text="Kullanıcı Adınızı Giriniz")
    password = TextField(label="Şifre", hint_text="Şifrenizi Giriniz", password=True)
    dogrulakullanici = TextField(label="Kullanıcı Adı", hint_text="Doğrulanacak Kullanıcı Adını Giriniz")
    t1 = Text(value="")

    dogrula = ElevatedButton(text="Kullanıcıyı Doğrula", on_click=kullanicidogrula2, width=page.width)
    onaylab1 = ElevatedButton(text="Giriş Yap", on_click=onaylab1, width=page.width)

    col = Column(controls=[username, password, t1, onaylab1], width=page.width, height=page.height, alignment="center", horizontal_alignment="center")

    page.controls.append(col)
    page.update()

flet.app(target=adminsistem)
