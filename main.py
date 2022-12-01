import pandas as pd
import matplotlib.pyplot as plt


valores_vazios = ["?", "-"]
x = pd.read_excel(
    r"C:\Users\AlaxAtaide\Desktop\DashPython\dados.xlsx", sheet_name="TESTE")

x = x.dropna(how="any", axis=1)

# colors = [""]
plt.rcParams["font.size"] = 10
plt.figure(figsize=(7, 7))
plt.pie(x["Total Geral"], labels=x["Data"],
        autopct="%1.2f%%", startangle=0, shadow=True)


plt.title("GEPEF ANALYTICS", fontsize=22)
plt.legend(loc=(1.1, 0.30))


plt.show()

# Mostra informações da tabela
print(x.info)

# Mostra informações da tabela mostrando a quantidade de caracteres
print(x.isna().sum())
