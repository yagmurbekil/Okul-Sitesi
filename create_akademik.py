import os
import re

directory = r"c:\Users\MEHMETBEKİL\Desktop\Okul_Sitesi"
template_path = os.path.join(directory, "hakkimizda.html")

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Replace title
content = template.replace("<title>Hakkımızda | Samsun Üniversitesi</title>", "<title>Akademik Kadro | Samsun Üniversitesi</title>")

# Replace the main section
academic_html = """
    <section class="page-hero">
        <h1>Akademik Kadro</h1>
    </section>

    <main class="container">
        <h2>Yazılım Mühendisliği Öğretim Elemanları</h2>
        <div class="academic-list">
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Doç. Dr. Muammer Türkoğlu</h3>
                </div>
                <div class="ac-role">Bölüm Başkanı</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Dr. Öğr. Üyesi Emel Soylu</h3>
                </div>
                <div class="ac-role">Bölüm Başkan Yardımcısı</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Dr. Öğr. Üyesi Özgür Tonkal</h3>
                </div>
                <div class="ac-role">Bölüm Başkan Yardımcısı</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Prof. Dr. Hüseyin Demir</h3>
                </div>
                <div class="ac-role">Öğretim Üyesi</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Prof. Dr. Zafer Cömert</h3>
                </div>
                <div class="ac-role">Öğretim Üyesi</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Doç. Dr. Abdulkadir Karacı</h3>
                </div>
                <div class="ac-role">Öğretim Üyesi</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Doç. Dr. Selçuk Çakmak</h3>
                </div>
                <div class="ac-role">Öğretim Üyesi</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Dr. Öğr. Üyesi Alper Talha Karadeniz</h3>
                </div>
                <div class="ac-role">Öğretim Üyesi</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Dr. Öğr. Üyesi Nurettin Şenyer</h3>
                </div>
                <div class="ac-role">Öğretim Üyesi</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Arş. Gör. Deniz Bora Küçük</h3>
                </div>
                <div class="ac-role">Öğretim Elemanı</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Arş. Gör. Ferhat Arat</h3>
                </div>
                <div class="ac-role">Öğretim Elemanı</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Arş. Gör. Furkancan Demircan</h3>
                </div>
                <div class="ac-role">Öğretim Elemanı</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Arş. Gör. İlker Gür</h3>
                </div>
                <div class="ac-role">Öğretim Elemanı</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Arş. Gör. Ömer Durmuş</h3>
                </div>
                <div class="ac-role">Öğretim Elemanı</div>
            </div>
            <div class="academic-row">
                <div class="ac-info">
                    <h3>Arş. Gör. Sarp Çoban</h3>
                </div>
                <div class="ac-role">Öğretim Elemanı</div>
            </div>
        </div>
    </main>
"""

content = re.sub(r'<section class=\"page-hero\">.*?</main>', academic_html, content, flags=re.DOTALL)

with open(os.path.join(directory, 'akademik.html'), 'w', encoding='utf-8') as f:
    f.write(content)
print("Akademik generated!")
