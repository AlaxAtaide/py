import pandas as pd
import matplotlib.pyplot as plt


valores_vazios = ["?", "-"]
x = pd.read_excel(
    r"C:\Users\AlaxAtaide\Desktop\DashPython\dados.xlsx", sheet_name="TESTE")

x = x.dropna(how="any", axis=1)

labels = list(x.Data)
labels = ["ECC/CEB"
          "Contabilidade", "IPREV", "Pecúnia", "Portabilidade", "Estorno", "Provisionamento", "Baixa", "BRBSERV", "Outros",
          "Total"]

fig, ax = plt.subplots(nrows=1, ncols=1)
x.plot(stacked="true", x="Data", kind="bar", rot=30)
plt.title("Evolução por Datas", fontsize="16")
plt.legend(loc="upper right", bbox_to_anchor=(1, 1))
ylabel = "Porcentagem"
xlabel = ""
ax = ax
ax.set_xticklabels(labels)


plt.show()
