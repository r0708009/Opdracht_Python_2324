import pandas as pd

dataframe = pd.read_csv('soldaten_en_wapens.csv')

excel_file_path = 'soldaten_en_wapens_excel.xlsx'

dataframe.to_excel(excel_file_path, index=False)

print(f"Gegevens zijn succesvol naar '{excel_file_path}' geschreven.")
