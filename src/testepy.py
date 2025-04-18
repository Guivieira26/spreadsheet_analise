from openpyxl import load_workbook

valor = 'string daquenipe'
print (valor)
valor = 3
valor = valor+1
print (valor)

plan_dest = load_workbook('new_tabel.xlsx')
aba_dest = plan_dest.active

aba_dest[f'A3']=valor

plan_dest.save("new_tabel_editBy.xlsx")