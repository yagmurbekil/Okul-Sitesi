import os
import re

directory = r"c:\Users\MEHMETBEKİL\Desktop\Okul_Sitesi"
new_nav = """<nav>
                <ul>
                    <li><a href="index.html">Ana Sayfa</a></li>
                    <li><a href="hakkimizda.html">Hakkımızda</a></li>
                    <li><a href="birimler.html">Birimler</a></li>
                    <li><a href="akademik.html">Ak. Kadro</a></li>
                    <li><a href="haberler.html">Haberler</a></li>
                    <li><a href="kampus.html">Kampüs</a></li>
                    <li><a href="takvim.html">Takvim</a></li>
                    <li><a href="ogrenci.html">Öğr. İşleri</a></li>
                    <li><a href="aday.html">Aday</a></li>
                    <li><a href="iletisim.html">İletişim</a></li>
                </ul>
            </nav>"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace navigation block
        content = re.sub(r'<nav>.*?</nav>', new_nav, content, flags=re.DOTALL)
        
        # Make sure no external links points to samsun.edu.tr (already did before but just to be sure, using regex or simple replace)
        content = content.replace('https://www.samsun.edu.tr/fakulteler', 'birimler.html')
        content = content.replace('https://www.samsun.edu.tr/', '#')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
print("Nav replaced!")
