"""
Ce module contient des fonctions pour interagir avec la base de données SQLite.

voici le script de création de la base de données :

CREATE TABLE CLIENT(
   idClient INTEGER,
   username TEXT NOT NULL,
   PRIMARY KEY(idClient)
);

CREATE TABLE LOGICIEL(
   IdLogiciel INTEGER,
   LibLogiciel TEXT NOT NULL,
   PRIMARY KEY(IdLogiciel)
);

CREATE TABLE PASSERELLE(
   IdPasserelle INTEGER,
   LibPasserelle TEXT NOT NULL,
   PRIMARY KEY(IdPasserelle)
);

CREATE TABLE LOGICIEL_CLIENT(
   idLogicielClient INTEGER,
   IdLogiciel INTEGER NOT NULL,
   idClient INTEGER NOT NULL,
   PRIMARY KEY(idLogicielClient),
   FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel),
   FOREIGN KEY(idClient) REFERENCES CLIENT(idClient)
);

CREATE TABLE LOGICIEL_CLIENT_EBP(
   idLogicielClient INTEGER,
   Folder_Id TEXT,
   Client_Id TEXT NOT NULL,
   Client_Secret TEXT NOT NULL,
   Subscription_Key TEXT NOT NULL,
   Token TEXT,
   PRIMARY KEY(idLogicielClient),
   FOREIGN KEY(idLogicielClient) REFERENCES LOGICIEL_CLIENT(idLogicielClient)
);

CREATE TABLE LOGICIEL_CLIENT_ZEENDOC(
   idLogicielClient INTEGER,
   Index_Statut_Paiement TEXT,
   Index_Ref_Doc TEXT,
   Classeur TEXT,
   Login TEXT NOT NULL,
   Password TEXT NOT NULL,
   UrlClient TEXT NOT NULL,
   PRIMARY KEY(idLogicielClient),
   FOREIGN KEY(idLogicielClient) REFERENCES LOGICIEL_CLIENT(idLogicielClient)
);

CREATE TABLE Connecte_Logiciel_Source(
   IdPasserelle INTEGER,
   IdLogiciel INTEGER NOT NULL,
   PRIMARY KEY(IdPasserelle),
   FOREIGN KEY(IdPasserelle) REFERENCES PASSERELLE(IdPasserelle),
   FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel)
);

CREATE TABLE Connecte_Logiciel_Destination(
   IdPasserelle INTEGER,
   IdLogiciel INTEGER NOT NULL,
   PRIMARY KEY(IdPasserelle),
   FOREIGN KEY(IdPasserelle) REFERENCES PASSERELLE(IdPasserelle),
   FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel)
);

CREATE TABLE CLIENT_PASSERELLE(
   idClient INTEGER,
   IdPasserelle INTEGER,
   PRIMARY KEY(idClient, IdPasserelle),
   FOREIGN KEY(idClient) REFERENCES CLIENT(idClient),
   FOREIGN KEY(IdPasserelle) REFERENCES PASSERELLE(IdPasserelle)
);

"""


import sqlite3


#########################################################################################
#                            Connexion à la base de données                             #
#########################################################################################


def get_db_connexion():
    """Retourne une connexion à la base de données SQLite."""
    conn = sqlite3.connect("BDPasserelleV2.db")
    conn.row_factory = sqlite3.Row
    return conn


#############################################################################################
#                                        CREATE DATABASE                                    #
#############################################################################################


def create_database():
    """
    Crée les tables nécessaires dans la base de données si elles n'existent pas déjà.

    Cette fonction exécute une série d'instructions SQL pour créer les tables suivantes :
    - CLIENT
    - LOGICIEL
    - LOGICIEL_CLIENT
    - PASSERELLE
    - API
    - API_EBP
    - API_ZEENDOC
    - EBP_CLIENT
    - ZEENDOC_CLIENT

    Si l'une des tables existe déjà, l'instruction CREATE TABLE correspondante est ignorée.

    Returns:
        None
    """
    conn = get_db_connexion()
    cursor = conn.cursor()

    # Creation des tables

    # CLIENT
    if not execute_query("SELECT name FROM sqlite_master WHERE type='table' AND name='CLIENT';"):
        cursor.execute(
            """
            CREATE TABLE CLIENT(
                idClient INTEGER,
                username TEXT NOT NULL,
                PRIMARY KEY(idClient)
            );""")

    # LOGICIEL
    if not execute_query("SELECT name FROM sqlite_master WHERE type='table' AND name='LOGICIEL';"):
        cursor.execute(
            """
            CREATE TABLE LOGICIEL(
                IdLogiciel INTEGER,
                LibLogiciel TEXT NOT NULL,
                PRIMARY KEY(IdLogiciel)
            );""")

    # PASSERELLE
    if not execute_query("""
                         SELECT name
                         FROM sqlite_master
                         WHERE type='table'
                         AND name='PASSERELLE';"""):
        cursor.execute(
            """
            CREATE TABLE PASSERELLE(
                IdPasserelle INTEGER,
                LibPasserelle TEXT NOT NULL,
                PRIMARY KEY(IdPasserelle)
            );""")

    # LOGICIEL_CLIENT
    if not execute_query("""
                         SELECT name
                         FROM sqlite_master
                         WHERE type='table'
                         AND name='LOGICIEL_CLIENT';"""):
        cursor.execute(
            """
            CREATE TABLE LOGICIEL_CLIENT(
                idLogicielClient INTEGER,
                IdLogiciel INTEGER NOT NULL,
                idClient INTEGER NOT NULL,
                PRIMARY KEY(idLogicielClient),
                FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel),
                FOREIGN KEY(idClient) REFERENCES CLIENT(idClient)
            );""")

    # LOGICIEL_CLIENT_EBP
    if not execute_query("""SELECT name
                         FROM sqlite_master
                         WHERE type='table'
                         AND name='LOGICIEL_CLIENT_EBP';"""):
        cursor.execute(
            """
            CREATE TABLE LOGICIEL_CLIENT_EBP(
                idLogicielClient INTEGER,
                Folder_Id TEXT,
                Client_Id TEXT NOT NULL,
                Client_Secret TEXT NOT NULL,
                Subscription_Key TEXT NOT NULL,
                Token TEXT,
                PRIMARY KEY(idLogicielClient),
                FOREIGN KEY(idLogicielClient) REFERENCES LOGICIEL_CLIENT(idLogicielClient)
            );""")

    # LOGICIEL_CLIENT_ZEENDOC
    if not execute_query("""SELECT name
                         FROM sqlite_master
                         WHERE type='table'
                         AND name='LOGICIEL_CLIENT_ZEENDOC';"""):
        cursor.execute(
            """
            CREATE TABLE LOGICIEL_CLIENT_ZEENDOC(
                idLogicielClient INTEGER,
                Index_Statut_Paiement TEXT,
                Index_Ref_Doc TEXT,
                Classeur TEXT,
                Login TEXT NOT NULL,
                Password TEXT NOT NULL,
                UrlClient TEXT NOT NULL,
                PRIMARY KEY(idLogicielClient),
                FOREIGN KEY(idLogicielClient) REFERENCES LOGICIEL_CLIENT(idLogicielClient)
            );""")

    # Connecte_Logiciel_Source
    if not execute_query("""SELECT name
                         FROM sqlite_master
                         WHERE type='table'
                         AND name='Connecte_Logiciel_Source';"""):
        cursor.execute(
            """
            CREATE TABLE Connecte_Logiciel_Source(
                IdPasserelle INTEGER,
                IdLogiciel INTEGER NOT NULL,
                PRIMARY KEY(IdPasserelle),
                FOREIGN KEY(IdPasserelle) REFERENCES PASSERELLE(IdPasserelle),
                FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel)
            );""")

    # Connecte_Logiciel_Destination
    if not execute_query("""SELECT name
                         FROM sqlite_master
                         WHERE type='table'
                         AND name='Connecte_Logiciel_Destination';"""):
        cursor.execute(
            """
            CREATE TABLE Connecte_Logiciel_Destination(
                IdPasserelle INTEGER,
                IdLogiciel INTEGER NOT NULL,
                PRIMARY KEY(IdPasserelle),
                FOREIGN KEY(IdPasserelle) REFERENCES PASSERELLE(IdPasserelle),
                FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel)
            );""")

    # CLIENT_PASSERELLE
    if not execute_query("""SELECT name
                         FROM sqlite_master
                         WHERE type='table'
                         AND name='CLIENT_PASSERELLE';"""):
        cursor.execute(
            """
            CREATE TABLE CLIENT_PASSERELLE(
                idClient INTEGER,
                IdPasserelle INTEGER,
                PRIMARY KEY(idClient, IdPasserelle),
                FOREIGN KEY(idClient) REFERENCES CLIENT(idClient),
                FOREIGN KEY(IdPasserelle) REFERENCES PASSERELLE(IdPasserelle)
            );""")




def execute_query(query, params=None):
    """Exécute une requête SQL sur la base de données et retourne les résultats
    si la requête est un SELECT."""
    conn = get_db_connexion()



    try:
        cursor = conn.cursor()
        if params:
            # Nettoie les paramètres de la requête
            params = tuple(params)
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if not query.strip().upper().startswith("SELECT"):
            conn.commit()

        # Récupère les résultats seulement pour les requêtes SELECT
        # (pas besoin pour les INSERT, UPDATE, DELETE, etc.)
        if query.strip().upper().startswith("SELECT"):
            # transforme les résultats en json
            result = [dict(row) for row in cursor.fetchall()]
            return result


    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()


def execute_query_single(query, params=None):
    """Exécute une requête SQL sur la base de données et retourne un seul résultat si la
    requête est un SELECT."""
    conn = get_db_connexion()

    try:
        if params:
            result = conn.execute(query, params).fetchone()
        else:
            result = conn.execute(query).fetchone()
        conn.commit()

        # transforme les résultats en json
        if result:
            result = dict(result)



        return result
    except Exception as e:
        return e
    finally:
        conn.close()


def add_record(table_name, columns, values):
    """Ajoute un enregistrement à la table spécifiée avec les colonnes et valeurs spécifiées."""
    query = f"""INSERT INTO {table_name}({', '.join(columns)})
    VALUES ({', '.join(['?'] * len(values))})"""
    return execute_query(query, values)


def delete_record(table_name, condition, params):
    """Supprime un enregistrement de la table spécifiée en fonction de
    la condition et des paramètres spécifiés."""
    query = f"DELETE FROM {table_name} WHERE {condition}"
    return execute_query(query, params)


def get_all_records(table_name):
    """Récupère tous les enregistrements de la table spécifiée."""
    query = f"SELECT * FROM {table_name}"
    return execute_query(query)


def get_record_by_id(table_name, id_column, id_value):
    """Récupère un enregistrement spécifique de la table spécifiée en fonction de
    la colonne et de la valeur d'identifiant."""
    query = f"SELECT * FROM {table_name} WHERE {id_column} = ?"
    return execute_query_single(query, (id_value, ))


def drop_table(table_name):
    """Supprime la table spécifiée de la base de données."""
    query = f"DROP TABLE IF EXISTS {table_name}"
    return execute_query(query)


###################################################################################################
#                                        PASSERELLE                                              #
###################################################################################################


def get_all_passerelles():
    """Récupère toutes les passerelles de la base de données."""

    return get_all_records("PASSERELLE")


def get_passerelle_by_id(id_passerelle):
    """Récupère une passerelle spécifique en fonction de son identifiant."""

    return get_record_by_id("PASSERELLE", "IdPasserelle", id_passerelle)



def delete_passerelle(id_passerelle):
    """Supprime une passerelle spécifique en fonction de son identifiant."""

    return delete_record("PASSERELLE", "IdPasserelle = ?", (id_passerelle, ))

def get_passerelle_by_logiciel(logiciel_id):
    """Récupère toutes les passerelles associées à un logiciel spécifique."""
    query = """
        SELECT DISTINCT p.*
        FROM (
            SELECT IdPasserelle
            FROM Connecte_Logiciel_Source
            WHERE IdLogiciel = ?

            UNION

            SELECT IdPasserelle
            FROM Connecte_Logiciel_Destination
            WHERE IdLogiciel = ?
        ) AS pass_ids
        JOIN PASSERELLE AS p ON pass_ids.IdPasserelle = p.IdPasserelle
    """
    return execute_query(query, (logiciel_id, logiciel_id))


def get_passerelle_by_client(client_id):
    """Récupère toutes les passerelles associées à un client spécifique."""
    query = """
        SELECT DISTINCT p.*
        FROM (
            SELECT IdPasserelle
            FROM CLIENT_PASSERELLE
            WHERE idClient = ?
        ) AS pass_ids
        JOIN PASSERELLE AS p ON pass_ids.IdPasserelle = p.IdPasserelle
    """
    return execute_query(query, (client_id, ))


def add_passerelle_with_connectors(lib_passerelle, source_logiciel_id, destination_logiciel_id):
    """Ajoute une passerelle avec des connecteurs source et destination spécifiés.
    note: requiert des logiciels existants dans la base de données.
    """
    try:
        # Ajouter la passerelle
        passerelle_id = add_passerelle(lib_passerelle)

        # Ajouter les connecteurs source et destination
        if passerelle_id:
            add_connecteur_source(passerelle_id, source_logiciel_id)
            add_connecteur_destination(passerelle_id, destination_logiciel_id)

        return passerelle_id
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def add_passerelle(lib_passerelle):
    """Ajoute une passerelle avec le libellé spécifié."""
    return add_record("PASSERELLE", ["LibPasserelle"], [lib_passerelle])

def add_connecteur_source(passerelle_id, logiciel_id):
    """Ajoute un connecteur source pour une passerelle spécifique et un logiciel spécifique."""
    return add_record("Connecte_Logiciel_Source",
                      ["IdPasserelle",
                       "IdLogiciel"],
                      [passerelle_id,
                       logiciel_id])

def add_connecteur_destination(passerelle_id, logiciel_id):
    """Ajoute un connecteur de destination pour une passerelle spécifique et un
    logiciel spécifique."""
    return add_record("Connecte_Logiciel_Destination",
                      ["IdPasserelle", "IdLogiciel"],
                      [passerelle_id, logiciel_id])

def delete_connecteur_source(passerelle_id):
    """Supprime un connecteur source pour une passerelle spécifique."""
    return delete_record("Connecte_Logiciel_Source", "IdPasserelle = ?", (passerelle_id, ))

def delete_connecteur_destination(passerelle_id):
    """Supprime un connecteur de destination pour une passerelle spécifique."""
    return delete_record("Connecte_Logiciel_Destination", "IdPasserelle = ?", (passerelle_id, ))

def get_all_connecteurs_source():
    """Récupère tous les connecteurs source de la base de données."""
    return get_all_records("Connecte_Logiciel_Source")

def get_all_connecteurs_destination():
    """Récupère tous les connecteurs de destination de la base de données."""
    return get_all_records("Connecte_Logiciel_Destination")

def get_connecteur_source_by_id(passerelle_id):
    """Récupère un connecteur source pour une passerelle spécifique."""
    query = "SELECT * FROM Connecte_Logiciel_Source WHERE IdPasserelle = ?"
    return execute_query_single(query, (passerelle_id, ))

def get_connecteur_destination_by_id(passerelle_id):
    """Récupère un connecteur de destination pour une passerelle spécifique."""
    query = "SELECT * FROM Connecte_Logiciel_Destination WHERE IdPasserelle = ?"
    return execute_query_single(query, (passerelle_id, ))




##########################################################################################
#                                       CLIENT                                          #
##########################################################################################


def get_all_clients():
    """Récupère tous les clients de la base de données."""
    return get_all_records("CLIENT")

def get_client_by_id(id_client):
    """Récupère un client spécifique en fonction de son identifiant."""
    return get_record_by_id("CLIENT", "idClient", id_client)

def add_client(username):
    """Ajoute un client avec le nom d'utilisateur spécifié."""
    return add_record("CLIENT", ["username"], [username])

def delete_client(id_client):
    """Supprime un client spécifique en fonction de son identifiant."""
    return delete_record("CLIENT", "idClient = ?", (id_client, ))

def get_client_by_logiciel(logiciel_id):
    """Récupère tous les clients associés à un logiciel spécifique."""
    query = """
        SELECT DISTINCT c.*
        FROM (
            SELECT idClient
            FROM LOGICIEL_CLIENT
            WHERE IdLogiciel = ?
        ) AS client_ids
        JOIN CLIENT AS c ON client_ids.idClient = c.idClient
    """
    return execute_query(query, (logiciel_id, ))

def get_client_by_passerelle(passerelle_id):
    """Récupère tous les clients associés à une passerelle spécifique."""
    query = """
        SELECT DISTINCT c.*
        FROM (
            SELECT idClient
            FROM CLIENT_PASSERELLE
            WHERE IdPasserelle = ?
        ) AS client_ids
        JOIN CLIENT AS c ON client_ids.idClient = c.idClient
    """
    return execute_query(query, (passerelle_id, ))

def add_client_passerelle(id_client, id_passerelle):
    """Ajoute un client à une passerelle spécifique."""
    return add_record("CLIENT_PASSERELLE", ["idClient", "IdPasserelle"], [id_client, id_passerelle])

def delete_client_passerelle(id_client, id_passerelle):
    """Supprime un client d'une passerelle spécifique."""
    return delete_record("CLIENT_PASSERELLE",
                         "idClient = ? AND IdPasserelle = ?",
                         (id_client, id_passerelle))

def get_client_passerelle_by_id(id_client, id_passerelle):
    """Récupère un client de passerelle spécifique en fonction de l'identifiant du client et de
    l'identifiant de la passerelle."""
    query = "SELECT * FROM CLIENT_PASSERELLE WHERE idClient = ? AND IdPasserelle = ?"
    return execute_query_single(query, (id_client, id_passerelle))


def get_passerelle_client_by_client(client_id):
    """Récupère idClient IdPasserelle et LibPasserelle par idClient"""
    query = """
        SELECT CLIENT_PASSERELLE.idClient, CLIENT_PASSERELLE.IdPasserelle, PASSERELLE.LibPasserelle
        FROM CLIENT_PASSERELLE
        JOIN PASSERELLE ON CLIENT_PASSERELLE.IdPasserelle = PASSERELLE.IdPasserelle
        WHERE CLIENT_PASSERELLE.idClient = ?
    """



    return execute_query(query, (client_id, ))




#############################################################################################
#                                       LOGICIEL                                           #
#############################################################################################


def get_all_logiciels():
    """Récupère tous les logiciels de la base de données."""
    return get_all_records("LOGICIEL")


def get_logiciel_by_id(id_logiciel):
    """Récupère un logiciel spécifique en fonction de son identifiant."""
    return get_record_by_id("LOGICIEL", "IdLogiciel", id_logiciel)


def add_logiciel(lib_logiciel):
    """Ajoute un logiciel avec le libellé spécifié."""
    return add_record("LOGICIEL", ["LibLogiciel"], [lib_logiciel])


def delete_logiciel(id_logiciel):
    """Supprime un logiciel spécifique en fonction de son identifiant."""
    return delete_record("LOGICIEL", "IdLogiciel = ?", (id_logiciel, ))


#############################################################################################
#                                  LOGICIEL CLIENT                                          #
#############################################################################################

def get_all_logiciel_clients():
    """Récupère tous les clients de logiciel de la base de données."""
    return get_all_records("LOGICIEL_CLIENT")


def get_logiciel_client_by_id(id_logiciel_client):
    """Récupère un client de logiciel spécifique en fonction de l'identifiant du client de logiciel."""
    query = "SELECT * FROM LOGICIEL_CLIENT WHERE idLogicielClient = ?"
    return execute_query_single(query, (id_logiciel_client, ))

def add_logiciel_client(id_logiciel, id_client):
    """Ajoute un client de logiciel avec les informations spécifiées."""
    return add_record("LOGICIEL_CLIENT", ["IdLogiciel", "idClient"], [id_logiciel, id_client])

def delete_logiciel_client(id_logiciel_client):
    """Supprime un client de logiciel spécifique en fonction de l'identifiant du client de logiciel."""
    return delete_record("LOGICIEL_CLIENT", "idLogicielClient = ?", (id_logiciel_client, ))

def get_logiciel_client_by_logiciel(logiciel_id):
    """Récupère tous les clients associés à un logiciel spécifique."""
    query = "SELECT * FROM LOGICIEL_CLIENT WHERE IdLogiciel = ?"
    return execute_query(query, (logiciel_id, ))

def get_logiciel_client_by_client(client_id):
    """Récupère tous les clients associés à un client spécifique."""
    query = "SELECT * FROM LOGICIEL_CLIENT WHERE idClient = ?"
    return execute_query(query, (client_id, ))

def get_logiciel_client_by_logiciel_and_client(logiciel_id, client_id):
    """Récupère un client de logiciel spécifique en fonction de l'identifiant du logiciel et de l'identifiant du client."""
    query = "SELECT * FROM LOGICIEL_CLIENT WHERE IdLogiciel = ? AND idClient = ?"
    return execute_query_single(query, (logiciel_id, client_id))



#############################################################################################
#                                  LOGICIEL EBP CLIENT                                      #
#############################################################################################


def get_all_logiciels_ebp_client():
    """Récupère tous les clients de logiciel EBP de la base de données."""
    return get_all_records("LOGICIEL_CLIENT")


def get_logiciel_ebp_client_by_id(id_logiciel_client):
    """Récupère un client de logiciel EBP spécifique en fonction de l'identifiant du
    client de logiciel."""
    query = "SELECT * FROM LOGICIEL_CLIENT WHERE IdLogicielClient = ?"
    return execute_query_single(query, (id_logiciel_client, ))


def add_logiciel_ebp_client(id_logiciel, id_client, id_logiciel_client, subscription_key, client_secret):
    """Ajoute un client de logiciel EBP avec les informations spécifiées."""
    return add_record(
        "LOGICIEL_CLIENT",
        ["IdLogiciel", "idLogicielClient", "idClient"],
        [id_logiciel, id_client, id_logiciel_client],
    )

def delete_logiciel_ebp_client(id_logiciel_client):
    """Supprime un client de logiciel EBP spécifique en fonction de l'identifiant du
    client de logiciel."""
    return delete_record(
        "LOGICIEL_CLIENT",
        "IdLogicielClient = ?",
        (id_logiciel_client, ))



############################################################################################
#                                   LOGICIEL ZEENDOC CLIENT                                #
############################################################################################


def get_all_logiciel_zeendoc_clients():
    """Récupère tous les clients de logiciel Zeendoc de la base de données."""
    return get_all_records("LOGICIEL_CLIENT")


def get_logiciel_zeendoc_client_by_id(id_logiciel_client):
    """Récupère un client de logiciel Zeendoc spécifique en fonction de l'identifiant du
    client de logiciel."""
    query = "SELECT * FROM LOGICIEL_CLIENT JOIN LOGICIEL_CLIENT_ZEENDOC USING (idLogicielClient) WHERE idLogicielClient = ?"
    return execute_query_single(query, (id_logiciel_client, ))


# def add_logiciel_zeendoc_client(id_logiciel_client, login, password, url_client, db_connection):
#     """Ajoute ou met à jour un client de logiciel Zeendoc avec les informations spécifiées."""
#     cursor = db_connection.cursor()
#     cursor.execute("SELECT 1 FROM LOGICIEL_CLIENT_ZEENDOC WHERE idLogicielClient = ?", (id_logiciel_client,))
#     if cursor.fetchone():
#         # Mise à jour de l'enregistrement existant
#         cursor.execute("UPDATE LOGICIEL_CLIENT_ZEENDOC SET Login = ?, Password = ?, UrlClient = ? WHERE idLogicielClient = ?",
#                        (login, password, url_client, id_logiciel_client))
#     else:
#         # Insertion d'un nouvel enregistrement
#         cursor.execute("INSERT INTO LOGICIEL_CLIENT_ZEENDOC (idLogicielClient, Login, Password, UrlClient) VALUES (?, ?, ?, ?)",
#                        (id_logiciel_client, login, password, url_client))
#     db_connection.commit()

def add_logiciel_zeendoc_client(id_logiciel, id_client, login, password, url_client):
    """Ajoute un client de logiciel Zeendoc avec les informations spécifiées."""
    add_logiciel_client(id_logiciel, id_client)


    # on recupere l'id du logiciel client
    id_logiciel_client = get_logiciel_client_by_logiciel_and_client(id_logiciel, id_client)["idLogicielClient"]

    # print("id_logiciel_client", id_logiciel_client)



    add_record("LOGICIEL_CLIENT_ZEENDOC",
                        ["idLogicielClient", "Login", "Password", "UrlClient"],
                        [id_logiciel_client, login, password, url_client])




def delete_logiciel_zeendoc_client(id_logiciel_client):
    """Supprime un client de logiciel Zeendoc spécifique en fonction de l'identifiant du
    client de logiciel."""
    return delete_record("LOGICIEL_CLIENT_ZEENDOC", "IdLogicielClient = ?",
                         (id_logiciel_client, ))



def set_logiciel_zeendoc_client_Index_Statut_Paiement(id_logiciel_client, Index_Statut_Paiement):
    """Met à jour l'index de statut de paiement d'un client de logiciel Zeendoc spécifique."""
    query = "UPDATE LOGICIEL_CLIENT_ZEENDOC SET Index_Statut_Paiement = ? WHERE idLogicielClient = ?"
    return execute_query(query, (Index_Statut_Paiement, id_logiciel_client))

def set_logiciel_zeendoc_client_Index_Ref_Doc(id_logiciel_client, Index_Ref_Doc):
    """Met à jour l'index de référence de document d'un client de logiciel Zeendoc spécifique."""
    query = "UPDATE LOGICIEL_CLIENT_ZEENDOC SET Index_Ref_Doc = ? WHERE idLogicielClient = ?"
    return execute_query(query, (Index_Ref_Doc, id_logiciel_client))

def set_logiciel_zeendoc_client_Classeur(id_logiciel_client, Classeur):
    """Met à jour le classeur d'un client de logiciel Zeendoc spécifique."""
    query = "UPDATE LOGICIEL_CLIENT_ZEENDOC SET Classeur = ? WHERE idLogicielClient = ?"
    return execute_query(query, (Classeur, id_logiciel_client))





#######################################################################################
#                               Requête plus complexe                                 #
#######################################################################################


def get_all_client_passerelles_by_id_client(id_client):
    """
    Retourne toutes les passerelles d'un client spécifique.

    :param id_client: L'identifiant du client pour lequel récupérer les passerelles.
    :return: Une liste de toutes les passerelles associées au client.
    """
    # Définition de la requête SQL
    query = """
    SELECT EBP_CLIENT.*, LOGICIEL_CLIENT.*, LOGICIEL.LibLogiciel
    FROM EBP_CLIENT
    JOIN LOGICIEL_CLIENT ON EBP_CLIENT.IdLogiciel = LOGICIEL_CLIENT.IdLogiciel
                          AND EBP_CLIENT.id = LOGICIEL_CLIENT.id
                          AND EBP_CLIENT.IdLogicielClient = LOGICIEL_CLIENT.IdLogicielClient
    JOIN LOGICIEL ON LOGICIEL_CLIENT.IdLogiciel = LOGICIEL.IdLogiciel
    WHERE EBP_CLIENT.id = ?
    """

    # Exécution de la requête avec le paramètre id_client
    return execute_query(query, (id_client, ))


def drop_all_tables():
    """ Supprime toutes les tables de la base de données."""
    drop_table("CLIENT")
    drop_table("LOGICIEL")
    drop_table("LOGICIEL_CLIENT")
    drop_table("PASSERELLE")
    drop_table("API")
    drop_table("API_EBP")
    drop_table("API_ZEENDOC")
    drop_table("EBP_CLIENT")
    drop_table("ZEENDOC_CLIENT")
    drop_table("Connecte_Logiciel_Source")
    drop_table("Connecte_Logiciel_Destination")
    drop_table("CLIENT_PASSERELLE")
    drop_table("LOGICIEL_CLIENT_EBP")
    drop_table("LOGICIEL_CLIENT_ZEENDOC")