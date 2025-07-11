import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# 📥 1. Veriyi oku
df = pd.read_csv("harcamalar.csv")
df["Tarih"] = pd.to_datetime(df["Tarih"])

# 📊 2. Aylık toplam harcama
df["Ay"] = df["Tarih"].dt.to_period("M")
monthly_total = df.groupby("Ay")["Tutar"].sum()

# 📊 3. Kategori bazlı toplam harcama
category_total = df.groupby("Kategori")["Tutar"].sum()

# 📁 4. Çıktı klasörü oluştur
if not os.path.exists("output"):
    os.makedirs("output")

# 📈 5. Grafik 1 - Aylık harcama
plt.figure(figsize=(6,4))
monthly_total.plot(kind="bar", color="skyblue")
plt.title("Aylık Toplam Harcama")
plt.ylabel("Tutar (₺)")
plt.tight_layout()
plt.savefig("output/aylik_harcama.png")
plt.close()

# 📈 6. Grafik 2 - Kategori bazlı harcama
plt.figure(figsize=(6,4))
category_total.plot(kind="bar", color="orange")
plt.title("Kategori Bazlı Harcama")
plt.ylabel("Tutar (₺)")
plt.tight_layout()
plt.savefig("output/kategori_harcama.png")
plt.close()

# 📄 7. PDF Rapor oluştur
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Karacode SheetX - Harcama Raporu", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, "1. Aylik Harcama Grafigi:", ln=True)
pdf.image("output/aylik_harcama.png", w=170)

pdf.ln(10)
pdf.cell(200, 10, "2. Kategori Bazli Harcama Grafigi:", ln=True)
pdf.image("output/kategori_harcama.png", w=170)

rapor_yolu = "output/harcama_raporu.pdf"
pdf.output(rapor_yolu)

print(f"✅ Rapor başarıyla oluşturuldu: {rapor_yolu}")
