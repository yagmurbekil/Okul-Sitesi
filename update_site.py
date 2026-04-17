import os
import re

directory = r"c:\Users\MEHMETBEKİL\Desktop\Okul_Sitesi"
os.makedirs(os.path.join(directory, 'img'), exist_ok=True)

# Generate dummy image files for local testing
for img in ['kutuphane.jpg', 'spor_kompleksi.jpg', 'kafeterya.jpg', 'kulup.jpg']:
    open(os.path.join(directory, 'img', img), 'w').close()

def update_footer_and_script(content):
    # Remove script tags
    content = re.sub(r'<script>.*?</script>', '', content, flags=re.DOTALL)
    
    # Replace footer links
    old_links = """<div class="social-links">
                <a href="#">Instagram</a>
                <a href="#">Twitter</a>
                <a href="#">LinkedIn</a>
                <a href="#">YouTube</a>
            </div>"""
    new_links = """<div class="social-links">
                <a href="https://www.instagram.com/samsun.univ/" target="_blank">Instagram</a>
                <a href="https://x.com/samsun_univ" target="_blank">Twitter</a>
                <a href="https://www.linkedin.com/school/samsununiversitesi/about/" target="_blank">LinkedIn</a>
                <a href="https://www.youtube.com/@SamsunÜniversitesiTV" target="_blank">YouTube</a>
            </div>"""
    content = content.replace(old_links, new_links)
    return content

for file in os.listdir(directory):
    if file.endswith('.html'):
        filepath = os.path.join(directory, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = update_footer_and_script(content)

        if file == 'index.html':
            content = content.replace(
                'https://www.youtube.com/embed/uB8GS0YQo8Y?autoplay=1&mute=1&loop=1&playlist=uB8GS0YQo8Y&controls=0&showinfo=0&rel=0&disablekb=1&modestbranding=1',
                'https://www.youtube.com/embed/uB8GS0YQo8Y?autoplay=1&mute=1&loop=1&playlist=uB8GS0YQo8Y'
            )
            content = content.replace(
                '<a href="fakulteler.html" class="btn">Tüm Fakülteler</a>',
                '<a href="https://www.samsun.edu.tr/fakulteler" class="btn">Detayları İncele</a>'
            )

        if file == 'iletisim.html':
            content = content.replace(
                '<p><strong>E-Posta:</strong> iletisim@samsun.edu.tr</p>',
                '<p><strong>E-Posta:</strong> oibd@samsun.edu.tr</p>'
            )
            content = content.replace(
                '<button type="submit" class="btn"',
                '<button type="reset" class="btn"'
            )
            content = content.replace(
                '<form action="#" method="POST"',
                '<form>'
            )
            content = content.replace(
                '<div style="width: 100%; height: 250px; background-color: var(--bg-light); border: 1px solid #e2e8f0; border-radius:12px; display:flex; align-items:center; justify-content:center; color: var(--text-secondary); font-weight:600;">Harita İstemcisi Yükleniyor...</div>',
                '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d143003.5286461427!2d36.10309990595305!3d41.442974441589414!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40887df924ea5ec9%3A0xe54d913d806a6dd2!2zU2Ftc3Vuw5xuaXZlcnNpdGVzaSBCYWxswrFjYSBLYW1ww7xzw7w!5e0!3m2!1str!2str!4v1700" width="100%" height="250" style="border:0; border-radius:12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
            )

        if file == 'ogrenci.html':
            content = content.replace(
                '<a href="#" class="btn">Sisteme Giriş</a>',
                '<a href="https://obs.samsun.edu.tr/" class="btn">Sisteme Giriş</a>'
            )
            content = content.replace(
                '<a href="#" class="btn">Başvuru Sayfası</a>',
                '<a href="https://sks.samsun.edu.tr/" class="btn">Burs Başvurusu</a>'
            )
            
        if file == 'fakulteler.html':
            content = content.replace(
                '<a href="muhendislik.html" class="btn">Detaylı İncele</a>',
                '<a href="https://muhendislik.samsun.edu.tr/" class="btn">Detayları İncele</a>'
            )
            content = content.replace(
                '<a href="#" class="btn">Detaylı İncele</a>',
                '<a href="https://www.samsun.edu.tr/" class="btn">Detayları İncele</a>'
            )

        if file == 'kampus.html':
            old_divs = """<div style="background-color: var(--bg-light); border: 1px solid #e2e8f0; height: 250px; border-radius: 12px; display:flex; align-items:center; justify-content:center; color: var(--text-secondary); font-weight:600; font-size:1.1rem; box-shadow: inset 0 2px 10px rgba(0,0,0,0.02);">Yeni Nesil Kütüphane</div>
                <div style="background-color: var(--bg-light); border: 1px solid #e2e8f0; height: 250px; border-radius: 12px; display:flex; align-items:center; justify-content:center; color: var(--text-secondary); font-weight:600; font-size:1.1rem; box-shadow: inset 0 2px 10px rgba(0,0,0,0.02);">Kapalı Spor Kompleksi</div>
                <div style="background-color: var(--bg-light); border: 1px solid #e2e8f0; height: 250px; border-radius: 12px; display:flex; align-items:center; justify-content:center; color: var(--text-secondary); font-weight:600; font-size:1.1rem; box-shadow: inset 0 2px 10px rgba(0,0,0,0.02);">Merkezi Kafeterya ve Açık Alan</div>
                <div style="background-color: var(--bg-light); border: 1px solid #e2e8f0; height: 250px; border-radius: 12px; display:flex; align-items:center; justify-content:center; color: var(--text-secondary); font-weight:600; font-size:1.1rem; box-shadow: inset 0 2px 10px rgba(0,0,0,0.02);">Öğrenci Kulüpleri Etkinliği</div>"""
            new_imgs = """<img src="img/kutuphane.jpg" alt="Yeni Nesil Kütüphane" class="modern-img">
                <img src="img/spor_kompleksi.jpg" alt="Kapalı Spor Kompleksi" class="modern-img">
                <img src="img/kafeterya.jpg" alt="Merkezi Kafeterya ve Açık Alan" class="modern-img">
                <img src="img/kulup.jpg" alt="Öğrenci Kulüpleri Etkinliği" class="modern-img">"""
            content = content.replace(old_divs, new_imgs)

        if file == 'takvim.html':
            old_calendar = """<tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 15px;">Ders Kayıtları (Güz Yarıyılı)</td>
                            <td style="padding: 15px;">15 Eylül 2026</td>
                            <td style="padding: 15px;">22 Eylül 2026</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 15px;">Derslerin Başlaması</td>
                            <td style="padding: 15px;">28 Eylül 2026</td>
                            <td style="padding: 15px;">-</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 15px;">Ara Sınavlar (Vize)</td>
                            <td style="padding: 15px;">20 Kasım 2026</td>
                            <td style="padding: 15px;">30 Kasım 2026</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px;">Yarıyıl Sonu Sınavları (Final)</td>
                            <td style="padding: 15px;">08 Ocak 2027</td>
                            <td style="padding: 15px;">20 Ocak 2027</td>
                        </tr>"""
            new_calendar = """<tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 15px;">Ders Kayıtları (Güz Yarıyılı)</td>
                            <td style="padding: 15px;">15 Eylül 2025</td>
                            <td style="padding: 15px;">22 Eylül 2025</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 15px;">Derslerin Başlaması</td>
                            <td style="padding: 15px;">29 Eylül 2025</td>
                            <td style="padding: 15px;">-</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 15px;">Ara Sınavlar (Vize)</td>
                            <td style="padding: 15px;">17 Kasım 2025</td>
                            <td style="padding: 15px;">28 Kasım 2025</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 15px;">Yarıyıl Sonu Sınavları (Final)</td>
                            <td style="padding: 15px;">05 Ocak 2026</td>
                            <td style="padding: 15px;">16 Ocak 2026</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                            <td style="padding: 15px;">Bahar Yarıyılı Ders Kayıtları</td>
                            <td style="padding: 15px;">09 Şubat 2026</td>
                            <td style="padding: 15px;">13 Şubat 2026</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px;">Bahar Yarıyılı Ders Başlangıcı</td>
                            <td style="padding: 15px;">16 Şubat 2026</td>
                            <td style="padding: 15px;">-</td>
                        </tr>"""
            content = content.replace(old_calendar, new_calendar)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
