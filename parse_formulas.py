import openpyxl

wb = openpyxl.load_workbook("Bordro 2025 2. YY.xlsx", data_only=False)
sheet = wb["2024 Ocak Bodro"]

print("--- Hamit Yazıcı Formulas ---")
cols = ['M', 'P', 'Q', 'R', 'T', 'V', 'W', 'X']
for c in cols:
    val = sheet[f"{c}24"].value
    print(f"Col {c}: {val}")
