import openpyxl

wb = openpyxl.load_workbook("Bordro 2025 2. YY.xlsx", data_only=True)
sheet = wb["2024 Ocak Bodro"]

# Row 19 is Kadir Şişman (Usta Öğretici), Let's look closely at his columns
# C: TC, D: Ad, E: Görev, F: 1 saat ücreti, G: İşlenen saat, H: Aylık Tutar
# M: Tahakkuk Toplamı (Gross)
# P: Gelir Vergisi
# Q: Damga Vergisi
# R: Sigorta Pirimi İşçi
# T: İşsizlik Sigorta Pirimi İşçi
# W: Vergi Muafiyeti
# X: Net Maaş

print("--- Kadir Sisman Data ---")
cols = ['C', 'D', 'E', 'F', 'G', 'H', 'M', 'P', 'Q', 'R', 'T', 'W', 'X']
for c in cols:
    val = sheet[f"{c}19"].value
    print(f"Col {c}: {val}")

print("\n--- Yıldırım Kara Data (Müdür) ---")
for c in cols:
    val = sheet[f"{c}12"].value
    print(f"Col {c}: {val}")
