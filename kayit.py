from firebase import firebase
import flet
from flet import Page, Text, ElevatedButton, TextField, Column


firebase = firebase.FirebaseApplication('firebase_url',None)
def kayitsistemi(page: Page):

    page.title = "Kayıt Sistemi"

    def kayitol(e):
        col.controls = [username, password, passwordonayla, t1, onaylab2]
        col.update()

    def onaylab2(e):
        if (username.value.strip() in firebase.get(f"users/dogrulanmamis/", '') or
                username.value.strip() in firebase.get(f"admin/", '') or
             username.value.strip() in firebase.get(f"users/dogrulanmis/", '')):
            t1.value = 'Böyle Bir Hesap Zaten Mevcut!'

        else:
            if password.value == passwordonayla.value:
                data = {'username':username.value.strip(), 'password':int(password.value.strip()),'email':''}
                firebase.patch(f"users/dogrulanmamis/{username.value.strip()}",data)
                t1.value = 'Hesabınız Oluşturuldu! Lütfen Giriş Yapınız!'
            else:
                t1.value = 'Şifreler Uyuşmuyor. Tekrar Deneyiniz!'
        t1.update()

    username = TextField(label="Kullanıcı Adı", hint_text="Kullanıcı Adınızı Giriniz")
    password = TextField(label="Şifre", hint_text="Şifrenizi Giriniz",password=True)
    passwordonayla = TextField(label="Şifrenizi Onaylayın", hint_text="Şifrenizi Tekrar Giriniz", password=True)
    t1 = Text(value="")

    b2 = ElevatedButton(text="Kayıt Ol", on_click=kayitol, width=page.width)

    onaylab2 = ElevatedButton(text="Onayla",on_click=onaylab2, width=page.width)


    col = Column(controls=[t1,b2],width=page.width,height=page.height,alignment="center", horizontal_alignment="center")

    page.controls.append(col)
    page.update()

flet.app(target=kayitsistemi)
