import sqlite3

# CREATE TABLE CLIENT(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    username TEXT NOT NULL
# );

# CREATE TABLE LOGICIEL(
#    IdLogiciel INTEGER PRIMARY KEY AUTOINCREMENT,
#    LibLogiciel TEXT
# );

# CREATE TABLE LOGICIEL_CLIENT(
#    IdLogiciel INTEGER,
#    id INTEGER,
#    IdLogicielClient INTEGER,
#    PRIMARY KEY(IdLogiciel, id, IdLogicielClient),
#    FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel),
#    FOREIGN KEY(id) REFERENCES CLIENT(id)
# );

# CREATE TABLE PASSERELLE(
#    IdPasserelle INTEGER PRIMARY KEY AUTOINCREMENT,
#    LibPasserelle TEXT,
#    IdLogiciel INTEGER NOT NULL,
#    IdLogiciel_1 INTEGER NOT NULL,
#    FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel),
#    FOREIGN KEY(IdLogiciel_1) REFERENCES LOGICIEL(IdLogiciel)
# );

# CREATE TABLE API(
#    IdLogiciel INTEGER,
#    IdApi INTEGER,
#    PRIMARY KEY(IdLogiciel, IdApi),
#    FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel)
# );

# CREATE TABLE API_EBP(
#    IdLogiciel INTEGER,
#    IdApi INTEGER,
#    Client_Id TEXT,
#    Client_Secret TEXT,
#    Subscription_Key TEXT,
#    Token TEXT,
#    PRIMARY KEY(IdLogiciel, IdApi),
#    FOREIGN KEY(IdLogiciel, IdApi) REFERENCES API(IdLogiciel, IdApi)
# );

# CREATE TABLE API_ZEENDOC(
#    IdLogiciel INTEGER,
#    IdApi INTEGER,
#    Login TEXT,
#    Password TEXT,
#    UrlClient TEXT,
#    PRIMARY KEY(IdLogiciel, IdApi),
#    FOREIGN KEY(IdLogiciel, IdApi) REFERENCES API(IdLogiciel, IdApi)
# );

# CREATE TABLE EBP_CLIENT(
#    IdLogiciel INTEGER,
#    id INTEGER,
#    IdLogicielClient INTEGER,
#    Folder_Id TEXT,
#    PRIMARY KEY(IdLogiciel, id, IdLogicielClient),
#    FOREIGN KEY(IdLogiciel, id, IdLogicielClient) REFERENCES LOGICIEL_CLIENT(IdLogiciel, id, IdLogicielClient)
# );

# CREATE TABLE ZEENDOC_CLIENT(
#    IdLogiciel INTEGER,
#    id INTEGER,
#    IdLogicielClient INTEGER,
#    Index_Statut_Paiement TEXT,
#    Index_Ref_Doc TEXT,
#    Classeur TEXT,
#    PRIMARY KEY(IdLogiciel, id, IdLogicielClient),
#    FOREIGN KEY(IdLogiciel, id, IdLogicielClient) REFERENCES LOGICIEL_CLIENT(IdLogiciel, id, IdLogicielClient)
# );

# CREATE TABLE Client_Passerelle(
#    IdLogiciel INTEGER,
#    id INTEGER,
#    IdLogicielClient INTEGER,
#    IdPasserelle INTEGER,
#    PRIMARY KEY(IdLogiciel, id, IdLogicielClient, IdPasserelle),
#    FOREIGN KEY(IdLogiciel, id, IdLogicielClient) REFERENCES LOGICIEL_CLIENT(IdLogiciel, id, IdLogicielClient),
#    FOREIGN KEY(IdPasserelle) REFERENCES PASSERELLE(IdPasserelle)
# );

################################################################################################################################
#                                                     Connexion à la base de données                                           #


def get_db_connexion():
    conn = sqlite3.connect("BDPasserelleV2.db")
    conn.row_factory = sqlite3.Row
    return conn


################################################################################################################################
#                                                     CREATE TABLE CLIENT                                                      #
################################################################################################################################


def create_database():
    """
    Creates the necessary tables in the database if they don't already exist.

    This function executes a series of SQL statements to create the following tables:
    - CLIENT
    - LOGICIEL
    - LOGICIEL_CLIENT
    - PASSERELLE
    - API
    - API_EBP
    - API_ZEENDOC
    - EBP_CLIENT
    - ZEENDOC_CLIENT

    If any of the tables already exist, the corresponding CREATE TABLE statement is skipped.

    Note: This function assumes that the `get_db_connexion` function is defined elsewhere.

    Returns:
        None
    """
    conn = get_db_connexion()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS CLIENT(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL)"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS LOGICIEL(IdLogiciel INTEGER PRIMARY KEY AUTOINCREMENT, LibLogiciel TEXT)"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS LOGICIEL_CLIENT(IdLogiciel INTEGER, id INTEGER, IdLogicielClient INTEGER, PRIMARY KEY(IdLogiciel, id, IdLogicielClient), FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel), FOREIGN KEY(id) REFERENCES CLIENT(id))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS PASSERELLE(IdPasserelle INTEGER PRIMARY KEY AUTOINCREMENT, LibPasserelle TEXT, IdLogiciel INTEGER NOT NULL, IdLogiciel_1 INTEGER NOT NULL, FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel), FOREIGN KEY(IdLogiciel_1) REFERENCES LOGICIEL(IdLogiciel))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS API(IdLogiciel INTEGER, IdApi INTEGER, PRIMARY KEY(IdLogiciel, IdApi), FOREIGN KEY(IdLogiciel) REFERENCES LOGICIEL(IdLogiciel))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS API_EBP(IdLogiciel INTEGER, IdApi INTEGER, Client_Id TEXT, Client_Secret TEXT, Subscription_Key TEXT, Token TEXT, PRIMARY KEY(IdLogiciel, IdApi), FOREIGN KEY(IdLogiciel, IdApi) REFERENCES API(IdLogiciel, IdApi))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS API_ZEENDOC(IdLogiciel INTEGER, IdApi INTEGER, Login TEXT, Password TEXT, UrlClient TEXT, PRIMARY KEY(IdLogiciel, IdApi), FOREIGN KEY(IdLogiciel, IdApi) REFERENCES API(IdLogiciel, IdApi))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS EBP_CLIENT(IdLogiciel INTEGER, id INTEGER, IdLogicielClient INTEGER, Folder_Id TEXT, PRIMARY KEY(IdLogiciel, id, IdLogicielClient), FOREIGN KEY(IdLogiciel, id, IdLogicielClient) REFERENCES LOGICIEL_CLIENT(IdLogiciel, id, IdLogicielClient))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ZEENDOC_CLIENT(IdLogiciel INTEGER, id INTEGER, IdLogicielClient INTEGER, Index_Statut_Paiement TEXT, Index_Ref_Doc TEXT, Classeur TEXT, PRIMARY KEY(IdLogiciel, id, IdLogicielClient), FOREIGN KEY(IdLogiciel, id, IdLogicielClient) REFERENCES LOGICIEL_CLIENT(IdLogiciel, id, IdLogicielClient))"
    )


def execute_query(query, params=None):
    conn = get_db_connexion()

    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # Ne commit que si la requête n'est pas une SELECT
        if not query.strip().upper().startswith("SELECT"):
            conn.commit()

        # Récupère les résultats seulement pour les requêtes SELECT
        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(f"An error occurred: {e}")  # Ou utilisez un mécanisme de logging
        return None
    finally:
        conn.close()


def execute_query_single(query, params=None):
    conn = get_db_connexion()

    try:
        if params:
            result = conn.execute(query, params).fetchone()
        else:
            result = conn.execute(query).fetchone()
        conn.commit()
        return result
    except Exception as e:
        return e
    finally:
        conn.close()


def add_record(table_name, columns, values):
    query = f"INSERT INTO {table_name}({', '.join(columns)}) VALUES ({', '.join(['?'] * len(values))})"
    return execute_query(query, values)


def delete_record(table_name, condition, params):
    query = f"DELETE FROM {table_name} WHERE {condition}"
    return execute_query(query, params)


def get_all_records(table_name):
    query = f"SELECT * FROM {table_name}"
    return execute_query(query)


def get_record_by_id(table_name, id_column, id_value):
    query = f"SELECT * FROM {table_name} WHERE {id_column} = ?"
    return execute_query_single(query, (id_value, ))


def drop_table(table_name):
    query = f"DROP TABLE IF EXISTS {table_name}"
    return execute_query(query)


################################################################################################################################
#                                                     PASSERELLE                                                              #
################################################################################################################################


def get_all_passerelles():
    return get_all_records("PASSERELLE")


def get_passerelle_by_id(id_passerelle):
    return get_record_by_id("PASSERELLE", "IdPasserelle", id_passerelle)


def add_passerelle(lib_passerelle, id_logiciel, id_logiciel_1):
    return add_record(
        "PASSERELLE",
        ["LibPasserelle", "IdLogiciel", "IdLogiciel_1"],
        [lib_passerelle, id_logiciel, id_logiciel_1],
    )


def delete_passerelle(id_passerelle):
    return delete_record("PASSERELLE", "IdPasserelle = ?", (id_passerelle, ))


################################################################################################################################
#                                                     API EBP                                                                 #
################################################################################################################################


def get_all_api_ebp():
    return get_all_records("API_EBP")


def get_api_ebp_by_id(id_logiciel, id_api):
    query = "SELECT * FROM API_EBP WHERE IdLogiciel = ? AND IdApi = ?"
    return execute_query_single(query, (id_logiciel, id_api))


def add_api_ebp(id_logiciel, id_api, client_id, client_secret,
                subscription_key, token):
    return add_record(
        "API_EBP",
        [
            "IdLogiciel",
            "IdApi",
            "Client_Id",
            "Client_Secret",
            "Subscription_Key",
            "Token",
        ],
        [
            id_logiciel, id_api, client_id, client_secret, subscription_key,
            token
        ],
    )


def api_ebp_add_token(id_logiciel, id_api, token):
    query = "UPDATE API_EBP SET Token = ? WHERE IdLogiciel = ? AND IdApi = ?"
    return execute_query(query, (token, id_logiciel, id_api))


def delete_api_ebp(id_logiciel, id_api):
    return delete_record("API_EBP", "IdLogiciel = ? AND IdApi = ?",
                         (id_logiciel, id_api))


################################################################################################################################
#                                                     API ZEENDOC                                                             #
################################################################################################################################


def get_all_api_zeendoc():
    return get_all_records("API_ZEENDOC")


def get_api_zeendoc_by_id(id_logiciel, id_api):
    query = "SELECT * FROM API_ZEENDOC WHERE IdLogiciel = ? AND IdApi = ?"
    return execute_query_single(query, (id_logiciel, id_api))


def add_api_zeendoc(id_logiciel, id_api, login, password, url_client):
    return add_record(
        "API_ZEENDOC",
        ["IdLogiciel", "IdApi", "Login", "Password", "UrlClient"],
        [id_logiciel, id_api, login, password, url_client],
    )


def delete_api_zeendoc(id_logiciel, id_api):
    return delete_record("API_ZEENDOC", "IdLogiciel = ? AND IdApi = ?",
                         (id_logiciel, id_api))


################################################################################################################################
#                                                     EBP CLIENT                                                              #
################################################################################################################################


def get_all_ebp_clients():
    return get_all_records("EBP_CLIENT")


def get_ebp_client_by_id(id_logiciel, id_client, id_logiciel_client):
    query = "SELECT * FROM EBP_CLIENT WHERE IdLogiciel = ? AND id = ? AND IdLogicielClient = ?"
    return execute_query_single(query,
                                (id_logiciel, id_client, id_logiciel_client))


def add_ebp_client(id_logiciel, id_client, id_logiciel_client, folder_id):
    return add_record(
        "EBP_CLIENT",
        ["IdLogiciel", "id", "IdLogicielClient", "Folder_Id"],
        [id_logiciel, id_client, id_logiciel_client, folder_id],
    )


def delete_ebp_client(id_logiciel, id_client, id_logiciel_client):
    return delete_record(
        "EBP_CLIENT",
        "IdLogiciel = ? AND id = ? AND IdLogicielClient = ?",
        (id_logiciel, id_client, id_logiciel_client),
    )


################################################################################################################################
#                                                     ZEENDOC CLIENT                                                          #
################################################################################################################################


def get_all_zeendoc_clients():
    return get_all_records("ZEENDOC_CLIENT")


def get_zeendoc_client_by_id(id_logiciel, id_client, id_logiciel_client):
    query = "SELECT * FROM ZEENDOC_CLIENT WHERE IdLogiciel = ? AND id = ? AND IdLogicielClient = ?"
    return execute_query_single(query,
                                (id_logiciel, id_client, id_logiciel_client))


def add_zeendoc_client(
    id_logiciel,
    id_client,
    id_logiciel_client,
    index_statut_paiement,
    index_ref_doc,
    classeur,
):
    return add_record(
        "ZEENDOC_CLIENT",
        [
            "IdLogiciel",
            "id",
            "IdLogicielClient",
            "Index_Statut_Paiement",
            "Index_Ref_Doc",
            "Classeur",
        ],
        [
            id_logiciel,
            id_client,
            id_logiciel_client,
            index_statut_paiement,
            index_ref_doc,
            classeur,
        ],
    )


def delete_zeendoc_client(id_logiciel, id_client, id_logiciel_client):
    return delete_record(
        "ZEENDOC_CLIENT",
        "IdLogiciel = ? AND id = ? AND IdLogicielClient = ?",
        (id_logiciel, id_client, id_logiciel_client),
    )


################################################################################################################################
#                                                     CLIENT PASSERELLE                                                        #
################################################################################################################################


def get_all_client_passerelles():
    return get_all_records("Client_Passerelle")


def get_client_passerelle_by_id(id_logiciel, id_client, id_logiciel_client,
                                id_passerelle):
    query = "SELECT * FROM Client_Passerelle WHERE IdLogiciel = ? AND id = ? AND IdLogicielClient = ? AND IdPasserelle = ?"
    return execute_query_single(
        query, (id_logiciel, id_client, id_logiciel_client, id_passerelle))


def add_client_passerelle(id_logiciel, id_client, id_logiciel_client,
                          id_passerelle):
    return add_record(
        "Client_Passerelle",
        ["IdLogiciel", "id", "IdLogicielClient", "IdPasserelle"],
        [id_logiciel, id_client, id_logiciel_client, id_passerelle],
    )


def delete_client_passerelle(id_logiciel, id_client, id_logiciel_client,
                             id_passerelle):
    return delete_record(
        "Client_Passerelle",
        "IdLogiciel = ? AND id = ? AND IdLogicielClient = ? AND IdPasserelle = ?",
        (id_logiciel, id_client, id_logiciel_client, id_passerelle),
    )


################################################################################################################################
#                                                     LOGICIEL                                                                #
################################################################################################################################


def get_all_logiciels():
    return get_all_records("LOGICIEL")


def get_logiciel_by_id(id_logiciel):
    return get_record_by_id("LOGICIEL", "IdLogiciel", id_logiciel)


def add_logiciel(lib_logiciel):
    return add_record("LOGICIEL", ["LibLogiciel"], [lib_logiciel])


def delete_logiciel(id_logiciel):
    return delete_record("LOGICIEL", "IdLogiciel = ?", (id_logiciel, ))


################################################################################################################################
#                                                LOGICIEL EBP CLIENT                                                           #
################################################################################################################################


def get_all_logiciel_ebp_clients():
    return get_all_records("LOGICIEL_CLIENT")


def get_logiciel_ebp_client_by_id(id_logiciel, id_client, id_logiciel_client):
    query = "SELECT * FROM LOGICIEL_CLIENT WHERE IdLogiciel = ? AND id = ? AND IdLogicielClient = ?"
    return execute_query_single(query,
                                (id_logiciel, id_client, id_logiciel_client))


def add_logiciel_ebp_client(id_logiciel, id_client, id_logiciel_client):
    return add_record(
        "LOGICIEL_CLIENT",
        ["IdLogiciel", "id", "IdLogicielClient"],
        [id_logiciel, id_client, id_logiciel_client],
    )


def delete_logiciel_ebp_client(id_logiciel, id_client, id_logiciel_client):
    return delete_record(
        "LOGICIEL_CLIENT",
        "IdLogiciel = ? AND id = ? AND IdLogicielClient = ?",
        (id_logiciel, id_client, id_logiciel_client),
    )


################################################################################################################################
#                                             LOGICIEL ZEENDOC CLIENT                                                          #
################################################################################################################################


def get_all_logiciel_zeendoc_clients():
    return get_all_records("LOGICIEL_CLIENT")


def get_logiciel_zeendoc_client_by_id(id_logiciel, id_client,
                                      id_logiciel_client):
    query = "SELECT * FROM LOGICIEL_CLIENT WHERE IdLogiciel = ? AND id = ? AND IdLogicielClient = ?"
    return execute_query_single(query,
                                (id_logiciel, id_client, id_logiciel_client))


def add_logiciel_zeendoc_client(id_logiciel, id_client, id_logiciel_client):
    return add_record(
        "LOGICIEL_CLIENT",
        ["IdLogiciel", "id", "IdLogicielClient"],
        [id_logiciel, id_client, id_logiciel_client],
    )


def delete_logiciel_zeendoc_client(id_logiciel, id_client, id_logiciel_client):
    return delete_record(
        "LOGICIEL_CLIENT",
        "IdLogiciel = ? AND id = ? AND IdLogicielClient = ?",
        (id_logiciel, id_client, id_logiciel_client),
    )


################################################################################################################################
#                                                     API EBP                                                                 #
################################################################################################################################


def get_all_api_ebp():
    return get_all_records("API_EBP")


def get_api_ebp_by_id(id_logiciel, id_api):
    query = "SELECT * FROM API_EBP WHERE IdLogiciel = ? AND IdApi = ?"
    return execute_query_single(query, (id_logiciel, id_api))


def add_api_ebp(id_logiciel,
                id_api,
                client_id,
                client_secret,
                subscription_key,
                token=None):
    return add_record(
        "API_EBP",
        [
            "IdLogiciel",
            "IdApi",
            "Client_Id",
            "Client_Secret",
            "Subscription_Key",
            "Token",
        ],
        [
            id_logiciel, id_api, client_id, client_secret, subscription_key,
            token
        ],
    )


def delete_api_ebp(id_logiciel, id_api):
    return delete_record("API_EBP", "IdLogiciel = ? AND IdApi = ?",
                         (id_logiciel, id_api))


################################################################################################################################
#                                                     API ZEENDOC                                                             #
################################################################################################################################


def get_all_api_zeendoc():
    return get_all_records("API_ZEENDOC")


def get_api_zeendoc_by_id(id_logiciel, id_api):
    query = "SELECT * FROM API_ZEENDOC WHERE IdLogiciel = ? AND IdApi = ?"
    return execute_query_single(query, (id_logiciel, id_api))


def add_api_zeendoc(id_logiciel, id_api, login, password, url_client):
    return add_record(
        "API_ZEENDOC",
        ["IdLogiciel", "IdApi", "Login", "Password", "UrlClient"],
        [id_logiciel, id_api, login, password, url_client],
    )


def delete_api_zeendoc(id_logiciel, id_api):
    return delete_record("API_ZEENDOC", "IdLogiciel = ? AND IdApi = ?",
                         (id_logiciel, id_api))


################################################################################################################################
#                                                     Requête plus complexe                                                    #
################################################################################################################################


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
    drop_table("CLIENT")
    drop_table("LOGICIEL")
    drop_table("LOGICIEL_CLIENT")
    drop_table("PASSERELLE")
    drop_table("API")
    drop_table("API_EBP")
    drop_table("API_ZEENDOC")
    drop_table("EBP_CLIENT")
    drop_table("ZEENDOC_CLIENT")


def select_all_from_all_tables():

    query = "SELECT * FROM CLIENT"

    result = execute_query(query)
    print("result CLIENT", result)

    return result
