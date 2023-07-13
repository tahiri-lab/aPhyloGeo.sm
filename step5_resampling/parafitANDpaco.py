import pandas as pd

parafit = pd.read_csv("filteredByParaFit.csv")
parafit_v_lt = parafit.V_Accession_full.to_list()

print(len(parafit_v_lt))

paco = pd.read_csv("filterdByPACo.csv")

paco_v_lt = paco.V_Accession_full.to_list()
print(len(paco_v_lt))

paco_host_lt = set(paco.Host_Accession.to_list())
print("PACo, number of related host", len(paco_host_lt))
print("Host List: ", paco_host_lt)

df = paco.drop_duplicates()
print("PACo dataset without duplicate", len(df))


# ---------------------------------------
to_remove = []

for i in paco_v_lt:
    if i not in parafit_v_lt:
        to_remove.append(i)

print(to_remove)
print(len(to_remove))
