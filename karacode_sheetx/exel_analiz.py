import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# Excel dosyasını oku
df = pd.read_excel("harcamalar.xlsx", engine='openpyxl')

# Temel istatistikler
toplam_harcama = df["Tutar"].sum()
kategori_toplam = df.groupby("Kategori")["Tutar"].sum()

# Çıktı klasörü oluştur
os.makedirs("output", exist_ok=True)

# Grafik 1: Tarihe göre harcama
plt.figure(figsize=(10, 5))
plt.plot(df["Tarih"], df["Tutar"], marker='o', color='teal')
plt.title("Aylik Harcama Grafigi")
plt.xlabel("Tarih")
plt.ylabel("Tutar (TL)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("output/aylik_harcama_xlsx.png")
plt.close()

# Grafik 2: Kategoriye göre harcama
plt.figure(figsize=(8, 5))
kategori_toplam.plot(kind="bar", color="coral")
plt.title("Kategori Bazli Harcama")
plt.xlabel("Kategori")
plt.ylabel("Toplam Tutar (TL)")
plt.tight_layout()
plt.grid(axis="y")
plt.savefig("output/kategori_harcama_xlsx.png")
plt.close()
