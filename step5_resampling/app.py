import streamlit as st
import pandas as pd

v_id_lt = ['EF065505', 'KJ473822', 'EF065509', 'KJ473820', 'KJ473821', 'NC_014470', 'GU190215', 'MG772933', 'MG772934', 'MN996532', 'DQ022305', 'DQ084200', 'GQ153545', 'GQ153544', 'GQ153546', 'GQ153548', 'GQ153540', 'GQ153539', 'GQ153541', 'DQ084199', 'GQ153547', 'GQ153543', 'GQ153542', 'DQ648857', 'DQ412043', 'KJ473814', 'KJ473812', 'KJ473813', 'KJ473811', 'JX993987', 'KY770859', 'KY770858', 'KJ473816', 'KT444582',
           'KY417150', 'KY417146', 'KY417144', 'KC881005', 'KF367457', 'KC881006', 'KY417152', 'KY417151', 'MK211376', 'KY417147', 'KY417148', 'KY417143', 'KY417149', 'MK211377', 'KY417142', 'FJ588686', 'DQ071615', 'KJ473815', 'KF569996', 'JX993988', 'KU973692', 'KF636752', 'KJ473795', 'EU420138', 'KJ473796', 'EU420137', 'EU420139', 'KJ473797', 'KJ473800', 'KJ473798', 'KJ473799', 'KJ473807', 'KJ473806', 'EF203065', 'KJ473808']
bat_id_lt = ['ON640726', 'AB085735', 'ON640722', 'AB085738', 'AB085739', 'AB106608', 'AB085731', 'MZ936290',
             'KP972690', 'HM134917', 'ON012504', 'KX261916', 'JX502551', 'OP894116', 'DQ888677', 'ON640662', 'MN366288']

# print(len(v_id_lt), len(bat_id_lt))
df = pd.read_csv("data.csv")
df = df[['V_Accession_full', 'Host_Accession', 'ORF1ab', 'spike']]

# ===============================================


@st.cache_resource()
def removeRow(virus_accession, bat_accession):
    global df
    df = df[~((df['V_Accession_full'] == virus_accession)
              & (df['Host_Accession'] == bat_accession))]
    return df


@st.cache_resource()
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


st.markdown("# Check sample by index")

Num_virus = st.number_input(
    "Please enter the virus number (for which p > 0.05)", min_value=1, max_value=69, step=1)

Num_bat = st.number_input(
    "Please enter the host number corresponding to the above virus", min_value=1, max_value=17, step=1)

virus_accession = v_id_lt[int(Num_virus)-1]
st.write(f'selected virus accession: {virus_accession}')
bat_accession = bat_id_lt[int(Num_bat)-1]
st.write(f'selected host accession: {bat_accession}')

if st.button("Remove this row"):

    df = removeRow(virus_accession, bat_accession)

    st.write(f"{df.shape[0]} rows of data remain")
    st.dataframe(df)


st.download_button(
    "Press to Download",
    convert_df(df),
    "filteredByParaFit.csv",
    "./filtered",
    key='download-csv'
)


# ===============================================


@st.cache_resource()
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


st.markdown("# Check sample by accession")

Id_virus = st.text_input(
    "Please enter the virus accession (for which p > 0.05)")

Id_bat = st.text_input(
    "Please enter the host number corresponding to the above virus")


st.write(f'selected virus accession: {Id_virus}')

st.write(f'selected host accession: {Id_bat}')

if st.button("Remove the row"):

    df = removeRow(Id_virus, Id_bat)

    st.write(f"{df.shape[0]} rows of data remain")
    st.dataframe(df)


st.download_button(
    "Press to Download",
    convert_df(df),
    "filterdByPACo.csv",
    "./filtered",
    key='download-csv2'
)
