import configparser
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

# If there is not exactly 1 argument, the app stop
if len(sys.argv) != 2:
    exit(-1)
# Else getting the argument
type_graph = sys.argv[1]

# DB connection
conf = configparser.ConfigParser()
conf.read("conf.ini")
db_connection = mysql.connector.connect(
    host=conf.get('Database', 'host'),
    user=conf.get('Database', 'user'),
    password=conf.get('Database', 'password'),
    database=conf.get('Database', 'db_name')
)

cursor = db_connection.cursor()

# Getting the useful data
cursor.execute("SELECT client.categorieSocioprofessionnelle, client.prixPanier, collecte.prixAlimentaire, "
               "collecte.prixMultimedia, collecte.prixVetements, collecte.prixJeux, collecte.prixElectromenager "
               "FROM client INNER JOIN collecte ON client.idCollecte = collecte.idCOLLECTE;")
# Stores the data in a dataframe
result = cursor.fetchall()
df = pd.DataFrame(result, columns=["sociopro", "prixPanier", "prixAlim", "prixMulti", "prixVet", "prixJeux", "prixElec"])

cursor.close()
db_connection.close()

os.makedirs("static", exist_ok=True)

if type_graph == "graph1":
    # preparing data for this specific graph
    rearranged_data = []
    for row in df.itertuples():
        tmp_list = []
        tmp_list.append(row.sociopro)
        tmp_list.append(row.prixAlim)
        tmp_list.append("Alimentation")
        rearranged_data.append(tuple(tmp_list))
        tmp_list = []
        tmp_list.append(row.sociopro)
        tmp_list.append(row.prixMulti)
        tmp_list.append("Multimedia")
        rearranged_data.append(tuple(tmp_list))
        tmp_list = []
        tmp_list.append(row.sociopro)
        tmp_list.append(row.prixVet)
        tmp_list.append("Vetements")
        rearranged_data.append(tuple(tmp_list))
        tmp_list = []
        tmp_list.append(row.sociopro)
        tmp_list.append(row.prixJeux)
        tmp_list.append("Jeux")
        rearranged_data.append(tuple(tmp_list))
        tmp_list = []
        tmp_list.append(row.sociopro)
        tmp_list.append(row.prixElec)
        tmp_list.append("Electromenager")
        rearranged_data.append(tuple(tmp_list))
    rearranged_df = pd.DataFrame(rearranged_data, columns=["sociopro", "prix", "categorie"])

    # Create a histogram for expenditure by product category according to socio-professional category
    plt.figure(figsize=(20, 12))
    ax = sns.barplot(data=rearranged_df, x='sociopro', y='prix', hue='categorie', errorbar=None)
    for i in ax.containers:
        ax.bar_label(i, )
    plt.xticks(rotation=5)
    plt.xlabel('Catégorie socioprofessionnelle')
    plt.ylabel('Dépense (en €)')
    # Saving the graph for displaying later
    plt.savefig("static/graph.png", dpi=80)

if type_graph == "graph2":
    # Create a histogram for average cart expenditure by socio-professional category
    plt.figure(figsize=(20, 12))
    ax = sns.barplot(data=df, x='sociopro', y='prixPanier', estimator='mean', errorbar=None)
    ax.bar_label(ax.containers[0])
    plt.xticks(rotation=5)
    plt.xlabel('Catégorie socioprofessionnelle')
    plt.ylabel('Dépense moyenne du panier (en €)')
    # Saving the graph for displaying later
    plt.savefig("static/graph.png", dpi=80)
