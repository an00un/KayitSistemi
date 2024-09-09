[**_`TurkHackTeam`_**](https://www.turkhackteam.org)

[**_`an0un TurkHackTeam`_**](https://www.turkhackteam.org/uye/an0un.1013653/)

[**_`an0un GitHub`_**](https://www.github.com/an00un)

[**_`an0un Telegram`_**](t.me/an00un)

![https://www.turkhackteam.org](https://github.com/user-attachments/assets/85d6960a-05ba-4c45-b83c-4a074eeaee02)

Python ve Firebase kullanarak oluşturduğumuz Kayıt Sistemi'ne büyük güncelleme getirmiş bulunmaktayım. Bu güncelleme sayesinde artık kullanıcılar hesaplarına kendi e-Posta adreslerini ekleyebilecekler ve Admin'ler istediği kullanıcıyı doğrulayabilecekler. Şundan bahsetmem gerekiyor: 3 farklı kullanıcı türümüz var.

![ayrac2](https://github.com/user-attachments/assets/0c410a92-ae3b-40b9-9409-6715a82606a3)

1. **Adminler**
2. **Doğrulanmış Kullanıcılar**
3. **Doğrulanmamış Kullanıcılar**

![ayrac2](https://github.com/user-attachments/assets/0c410a92-ae3b-40b9-9409-6715a82606a3)

Admin'lerin amacı zaten belli, henüz sadece doğrulanmamış kullanıcıları onaylamak. Daha sonraki güncellemelerde kullanıcılar istediği gibi profil fotoğrafı yükleyebilecekler ve Admin'ler de kullanıcılara timeout veya Ban dediğimiz kavramları uygulayabilecekler. Takipte kalın, her an yeni güncelleme gelebilir!

![nasilkullanilir](https://github.com/user-attachments/assets/ba1aaf95-f56e-4642-965b-199ab705cecd)

**`kayit.py`** dosyamız kullanıcının sisteme kayıt olmasını sağlar.

**`userpanel.py`** dosyamız kullanıcının hesabına giriş yapması ve hesabı ile ilgili işlemleri yapabilmesini sağlar. (Şimdilik sadece e-Posta ekleyebilirler)

**`admin.py`** dosyamız Admin'lerin hesabına giriş yapabilmesi, kendi hesabı ile ilgili işlemleri yapabilmesini ve kullanıcıların hesapları ile ilgili işlemleri yapabilmesini sağlar. (Şimdilik sadece Doğrulanmamış Kullanıcı'ları doğrulayabilirler.)

