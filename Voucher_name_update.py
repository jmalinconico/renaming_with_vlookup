import os
import pandas as pd

invoices = os.listdir(r'C:\Users\Rutland Products\Documents\Invoices\2022\Need renaming')
df1 = pd.read_excel(r'C:\Users\Rutland Products\Documents\Excel Docs for Python Test\AP Voucher numbers with Vendor names.xlsx', sheet_name=0)
df2 = pd.DataFrame(invoices, columns=['Voucher'])
list_2 = []
count = 0

for i in range(len(invoices)):
    voucher = invoices[count]
    vouchers = voucher[:6]
    list_2.append(vouchers)
    count += 1

#print(df1)
#print(list_2)

df_v = pd.DataFrame(list_2, columns=['Voucher']).astype(int)

#print(df_v)

df_f = pd.merge(df_v, df1, how='left', on=['Voucher'])

df_f.fillna(0)
#print(df_f)

df_f['New Name'] = df_f['Vendor #'].astype(str) + " " + df_f['Vendor Name'] + " " + df_f['Invoice #'].astype(str)

#print(df_f['New Name'])
#print(invoices[0])
#print(invoices[0][-4:])

file_name = (df_f['New Name'])

#print(file_name[0][:-2])
#print(invoices[0][:-4] + " " + file_name[0][:-2] + invoices[0][-4:])

cont = 0

for i in range(len(invoices)):
    new_file_name = invoices[cont][:-4] + ' ' + file_name[cont] + invoices[cont][-4:]
    src = r'C:\Users\Rutland Products\Documents\Invoices\2022\Need renaming\{}'.format(invoices[cont])
    dst = r'C:\Users\Rutland Products\Documents\Invoices\2022\03 March\{}'.format(new_file_name)
    print(src)
    print(dst)
    #os.rename(src, dst)
    print(cont)
    cont += 1
