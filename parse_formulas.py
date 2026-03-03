import openpyxl

wb = openpyxl.load_workbook("Bordro 2025 2. YY.xlsx", data_only=False)
sheet = wb["2024 Ocak Bodro"]

print("--- Kadir Sisman Formulas ---")
cols = ['M', 'P', 'Q', 'R', 'T', 'W', 'X']
for c in cols:
    val = sheet[f"{c}19"].value
    print(f"Col {c}: {val}")

print("\n--- Yıldırım Kara Formulas ---")
for c in cols:
    val = sheet[f"{c}12"].value
    print(f"Col {c}: {val}")
