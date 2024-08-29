from firebase import firebase
import flet
from flet import Page, Text, ElevatedButton, TextField, Column

firebase = firebase.FirebaseApplication('API_URL',None)
def kayitsistemi(page: Page):
    page.title = "Kayıt Sistemi"
    def girisyap(e):
        col.controls = [username, password, t1,onaylab1,geri]

        col.update()
    def kayitol(e):
        col.controls = [username, password,passwordonayla, t1,onaylab2,geri]
        col.update()
    def onaylab1(e):
        if username.value.strip() in firebase.get('',''):
            oku = firebase.get(username.value.strip(), '')
            deger = 0
            for i, v in oku.items():
                if password.value.strip() == v:
                    deger += 1
                if username.value.strip() == v:
                    deger += 1
                if deger == 2:
                    t1.value = 'Giriş Başarılı'
                else:
                    t1.value = 'Kullanıcı Adı veya Şifre Hatalı'
        else:
            t1.value = 'Kullanıcı Adı Hatalı'

        t1.update()
    def onaylab2(e):
        if username.value.strip() in firebase.get('',''):
            t1.value = 'Böyle Bir Hesap Zaten Mevcut!'
        else:
            if password.value == passwordonayla.value:
                data = {'username':username.value.strip(), 'password':password.value.strip()}
                firebase.patch(username.value.strip(),data)
                t1.value = 'Hesabınız Oluşturuldu! Lütfen Giriş Yapınız!'
            else:
                t1.value = 'Şifreler Uyuşmuyor. Tekrar Deneyiniz!'
        t1.update()
    def geri(e):
        col.controls = [t1,b1,b2]
        username.value = ""
        password.value = ""
        passwordonayla = ""
        t1.value = ""
        page.update()
    username = TextField(label="Kullanıcı Adı", hint_text="Kullanıcı Adınızı Giriniz")
    password = TextField(label="Şifre", hint_text="Şifrenizi Giriniz",password=True)
    passwordonayla = TextField(label="Şifrenizi Onaylayın", hint_text="Şifrenizi Tekrar Giriniz", password=True)
    t1 = Text(value="")
    b1 = ElevatedButton(text="Giriş Yap",on_click=girisyap,width=page.width)
    b2 = ElevatedButton(text="Kayıt Ol", on_click=kayitol, width=page.width)
    onaylab1 = ElevatedButton(text="Onayla",on_click=onaylab1, width=page.width)
    onaylab2 = ElevatedButton(text="Onayla",on_click=onaylab2, width=page.width)
    geri = ElevatedButton(text="Geri",on_click=geri, width=page.width)

    col = Column(controls=[t1,b1,b2],width=page.width,height=page.height,alignment="center", horizontal_alignment="center")

    page.controls.append(col)
    page.update()

flet.app(target=kayitsistemi)