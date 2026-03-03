import openpyxl

wb = openpyxl.load_workbook("Bordro 2025 2. YY.xlsx", data_only=False)
sheet = wb["2026 Şubat Bütçe"]

print("L4:", sheet["L4"].value)
print("M4:", sheet["M4"].value)
