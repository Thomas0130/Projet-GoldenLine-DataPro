import configparser
import mysql.connector
import random

# Number of lines of data to generate
NB_LINES = 100

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

# Insert data
categorieSocioprofessionnelle = ["Agriculteurs", "Artisans, commerçants et chefs d'entreprise",
                                 "Cadres et professions intellectuelles supérieures", "Professions intermédiaires",
                                 "Employés", "Ouvriers", "Non déterminé"]
for i in range(NB_LINES):
    # Generate random Collecte data
    prixAlimentaire = random.randint(0, 70)
    prixMultimedia = random.randint(0, 100)
    prixVetements = random.randint(0, 50)
    prixJeux = random.randint(0, 50)
    prixElectromenager = random.randint(0, 200)
    # Collecte data insertion
    insert_query = ("INSERT INTO collecte (prixAlimentaire, prixMultimedia, prixVetements, prixJeux, "
                    "prixElectromenager) VALUES (%s, %s, %s, %s, %s);")
    data = (prixAlimentaire, prixMultimedia, prixVetements, prixJeux, prixElectromenager)
    total_cart = sum(data)
    cursor.execute(insert_query, data)
    # Generate random Client data
    nbEnfants = random.randint(0, 4)
    categorie = categorieSocioprofessionnelle[random.randint(0, len(categorieSocioprofessionnelle)-1)]
    # Getting the related foreign key
    cursor.execute("SELECT MAX(idCOLLECTE) FROM collecte;")
    foreign_key = cursor.fetchall()[0][0]
    # Client data insertion
    insert_query = ("INSERT INTO client (nbEnfants, categorieSocioprofessionnelle, prixPanier, idCollecte) "
                    "VALUES (%s, %s, %s, %s);")
    data = (nbEnfants, categorie, total_cart, foreign_key)
    cursor.execute(insert_query, data)

db_connection.commit()
cursor.close()
db_connection.close()
