# Samsun Üniversitesi Yazılım Mühendisliği Bölüm Sitesi

Bu proje, Samsun Üniversitesi Yazılım Mühendisliği Bölümü için geliştirilmiş modern, kurumsal ve estetik standartlara uygun (Oxford tasarımı ilham alınarak hazırlanmış) bir kurumsal web sitesi çalışmasıdır.

Sıfırdan, tamamıyla **HTML5** ve **CSS3** standartları kurallarına bağlı kalınarak geliştirilmiş olup, herhangi bir JavaScript kütüphanesi veya script kodu kullanılmamıştır (No-JS policy).

## ✨ Başlıca Özellikler

* **Modern "Glassmorphism" Tasarım:** Yarı saydam menü butonları, akademik kadro kartları ve yumuşatılmış geçişler (blur efekti).
* **Kurumsal Kimlik ve Renk Yönetimi:** Üniversite kurumsal rengi olan "Lacivert (#002147)" ana renk olarak belirlenmiş, temizliği simgeleyen beyaz ve kırık beyaz arka plan dokusu (#f9f9fb) ile zenginleştirilmiştir. 
* **Responsive (Duyarlı) Düzen:** Flexbox ve CSS Grid mimarileri kullanılarak; mobil, tablet ve masaüstü bilgisayarlarda kusursuz görünen uyarlanabilir tasarım yapısı.
* **Akıcı Animasyonlar:** CSS tabanlı hover (üzerine gelme) etkileşimleri, yumuşak dönüştürmeler (transition: all 0.4s ease) ve zarif kart gölgeleri kullanıldı.
* **Görsel Zenginleştirme:** Tam ekran video arka planlı ana sayfa (Hero Section) yapısı ve modern haber listesi kartları.
* **Gelişmiş Tipografi:** Temiz satır ve harf aralıkları (letter-spacing) ile oluşturulmuş estetik alt başlık hiyerarşisi.

## 📂 Proje Dosya Yapısı

Proje 10 adet statik sayfadan ve ortak bileşenleri içeren bir stil dosyasından oluşmaktadır:

* `index.html`: Tam ekran videolu giriş yapısı ve genel tanıtım ana sayfası.
* `hakkimizda.html`: Bölümün akademik vizyonu ve teknik donanımı hakkında bilgiler.
* `haberler.html`: Sektör buluşmaları, teknofest ve proje başarılarının yer aldığı modern haber kartları bölümü.
* `akademik.html`: Çizgisel satır tasarımlı akademik personel listesi.
* `birimler.html`, `kampus.html`, `takvim.html`, `ogrenci.html`, `aday.html`, `iletisim.html` ve diğer kurumsal bilgilendirme sayfaları.
* `style.css`: Sitenin UI özelliklerini, tüm sayfa kurallarını ve medya sorgularını barındıran temel CSS dosyası.
* `/img` klasörü: Haber, galeri ve takım fotoğrafları barındıran görsel deposu.
* `/video` klasörü: Hero sekmesindeki arkaplan videoları.

## 🚀 Kurulum & Kullanım

Proje statik bir HTML/CSS mimarisine sahip olduğundan dolayı, kurulum için herhangi bir derleyiciye, sunucu tarafı programlamaya (Backend) ya da pakete ihtiyaç duymaz.

1. Proje dosyalarını bilgisayarınıza indirin veya klonlayın.
2. Dilerseniz dosyaların bulunduğu klasöre gidip doğrudan `index.html` dosyasını favori tarayıcınız (Chrome, Safari, Firefox vb.) ile açarak projeyi inceleyebilirsiniz.
3. Live Server gibi bir eklenti (VS Code) kullanıyorsanız sayfaları lokal bir port üstünde açabilirsiniz.

## 🛠️ Tasarım Stili Kararları

- Tasarımın nefes almasını ve göz yormamasını sağlamak amacıyla her bölüm (`section` / `container`) arasında özel %10 opaklıkta ayırıcı çizgiler ve temiz boşluklar bırakılmıştır.
- Tüm `border-radius` (köşe yumuşatma), `box-shadow` (gölge) değerleri modern trend standartlarında dengeli bir biçimde tutulmuştur.

## 📜 Lisans

Bu çalışma konsept/demo amacı ile hazırlanmıştır. Tasarımlar ve içerikler Samsun Üniversitesi fikri mülkiyet standartlarına uygun olarak örnek niteliğindedir.
