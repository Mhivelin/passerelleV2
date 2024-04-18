import json
import sys
import xml.etree.ElementTree as ET
import app.models.database

import requests

# from app.models.database import get_db_connection


class Zeendoc:

    def __init__(self, id) -> None:
        
        infos = db.get_api_zeendoc_by_id(id)
        
        
        

        # res = self.BdGetClientZeendoc(id)

        # self.log = res["ZEENDOC_LOGIN"]
        # self.cpassword = res["ZEENDOC_CPASSWORD"]
        # self.urlclient = res["ZEENDOC_URLCLIENT"]
        # self.classeur = res["ZEENDOC_CLASSEUR"]

        # self.id = id

        # self.co = self.login()

        # self.right = self.getright()

    # def BdGetClientZeendoc(self, id):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()

    #         cursor.execute("SELECT ZEENDOC_LOGIN, ZEENDOC_URLCLIENT, ZEENDOC_CPASSWORD, ZEENDOC_CLASSEUR FROM CLIENT_ZEENDOC WHERE id = ?", (id,))
    #         client = cursor.fetchone()

    #         if client:
    #             return dict(client)
    #         else:
    #             return None
    #     except Exception as e:
    #         print(f"Erreur lors de la récupération du client Zeendoc : {e}")
    #         return None
    #     finally:
    #         if conn:
    #             conn.close()

    def login(self):
        """fonction qui permet de se connecter à l'api zeendoc
        log: login de l'utilisateur
        cpassword: mot de passe de l'utilisateur
        urlclient: url du client
        """

        url = "https://armoires.zeendoc.com/" + self.urlclient + "/ws/3_0/Zeendoc.php"

        payload = (
            '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n  <soap:Body>\n    <login>\n      <Login>'
            + self.log +
            "</Login>\n      <Password></Password>\n      <CPassword>" +
            self.cpassword +
            "</CPassword>\n      <Access_token></Access_token>\n    </login>\n  </soap:Body>\n</soap:Envelope>\n"
        )
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "urn:Zeendoc#login",
            "Cookie": "ZeenDoc=c88d73cfd3fd7600bf9a6efb94e01599",
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text

    def getright(self):
        """fonction qui permet de récupérer les droits de l'utilisateur"""

        url = "https://armoires.zeendoc.com/" + self.urlclient + "/ws/3_0/Zeendoc.php"
        payload = '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n  <soap:Body>\n    <getRights>\n      <Get_ConfigSets></Get_ConfigSets>\n      <Access_token></Access_token>\n    </getRights>\n  </soap:Body>\n</soap:Envelope>\n'
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "urn:Zeendoc#getRights",
            "Cookie": "ZeenDoc=c88d73cfd3fd7600bf9a6efb94e01599",
        }

        try:
            response = requests.request("POST",
                                        url,
                                        headers=headers,
                                        data=payload)
            if response.status_code != 200:
                print("Erreur de requête : Code de statut HTTP",
                      response.status_code)
                return None

            response_text = response.text

            try:
                root = ET.fromstring(response_text)
                json_response = root.find(".//jsonResponse").text
                try:
                    cookie_data = json.loads(json_response)
                    return cookie_data
                except json.JSONDecodeError:
                    print(
                        "Erreur lors de la conversion du JSON en dictionnaire")
                    return None
            except ET.ParseError:
                print("Erreur lors de l'analyse du XML")
                return None
        except requests.RequestException as e:
            print("Erreur lors de la requête :", e)
            return None

    def get_classeurs(self):
        """fonction qui permet de récupérer les nom et id des classeurs de l'utilisateur"""

        right = self.right["Collections"]

        collections = []

        for collection in right:

            collections.append({
                "Coll_Id": collection["Coll_Id"],
                "Label": collection["Label"]
            })

        print(collections)

        return collections

    def getIndex(self):
        """fonction qui permet de récupérer les index de l'utilisateur"""

        return self.right["Collections"][0]["Index"]

    def getIDIndex(self, indexLibelle):
        """fonction qui permet de récupérer l'id d'un index dans right en parcourant les collections puis les index
        indexLibelle: nom de l'index
        """

        for collection in self.right["Collections"]:
            try:

                for index in collection["Index"]:
                    if index["Label"] == indexLibelle:
                        return index["Index_Id"]

            except:
                print("pas d'index")

        return None

    # def setClasseur(self, classeur):
    #     '''fonction qui permet de mettre à jour le classeur
    #     classeur: nom du classeur
    #     '''
    #     print('classeur')
    #     print(classeur)

    #     self.classeur = classeur
    #     # enregistrer le classeur dans la base de données
    #     conn = get_db_connection()

    #     try:
    #         conn.execute("UPDATE CLIENT_ZEENDOC SET ZEENDOC_CLASSEUR = ? WHERE id = ?", (classeur, self.id))
    #         conn.commit()
    #         # afficher le résultat de la requête
    #         print('test')
    #     except:
    #         print('erreur lors de la mise à jour du classeur')
    #         # afficher l'erreur rencontrée
    #         print(sys.exc_info()[0])
    #     finally:
    #         conn.close()

    def searchDocBycustom(self,
                          index_id,
                          index_value,
                          save_query_name="",
                          Wanted_Columns=""):

        Wanted_Columns += index_id

        url = "https://armoires.zeendoc.com/" + self.urlclient + "/ws/3_0/Zeendoc.php"

        payload = (
            '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n  <soap:Body>\n    <searchDoc>\n      <Coll_Id>'
            + self.classeur +
            '</Coll_Id>\n      <IndexList xsi:type="ArrayOfIndexDefinition">\n        <Index>\n            <Id>1</Id>\n            <Label>'
            + index_id + "</Label>\n            <Value>" + index_value +
            "</Value>\n            <Operator>EQUALS</Operator>\n        </Index>\n      </IndexList>\n  <Saved_Query_Name>"
            + save_query_name + "</Saved_Query_Name>\n    <Wanted_Columns>" +
            Wanted_Columns +
            "</Wanted_Columns>\n    </searchDoc>\n  </soap:Body>\n</soap:Envelope>\n"
        )
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "urn:Zeendoc#searchDoc",
            "Cookie": "ZeenDoc=c88d73cfd3fd7600bf9a6efb94e01599",
        }

        # ecrire la requete

        response = requests.request("POST", url, headers=headers, data=payload)

        # on transforme la réponse avec la librairie xml.etree.ElementTree
        root = ET.fromstring(response.text)

        # on récupère le contenu de la balise jsonResponse
        json_response = root.find(".//jsonResponse").text

        # on transforme le json en dictionnaire
        cookie_data = json.loads(json_response)

        return cookie_data

    def GetDocBAP(self):
        """fonction qui permet de récupérer les doc BAP à partir de son numéro de pièce comptable"""

        return self.searchDocBycustom(self.indexBAP, "1")

    def GetDocPaiement(self):

        return self.searchDocBycustom(self.indexPaiement, "0")

    def GetDocRef(self, ref):
        """fonction qui permet de récupérer le doc à partir de son numéro de pièce comptable"""

        res = self.searchDocBycustom(self.indexREF, ref)

        print("GetDocRef : ", res)

        return res

    def updateDoc(self, res_id, index):
        """
        fonction qui permet de mettre à jour un document
        res_id: ID de la ressource du document
        index: dictionnaire représentant l'index à mettre à jour et sa nouvelle valeur
        """

        # URL de l'API Zeendoc
        url = "https://armoires.zeendoc.com/" + self.urlclient + "/ws/3_0/Zeendoc.php"

        # Construction du payload XML pour la requête SOAP
        payload = (
            '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n  <soap:Body>\n    <updateDoc>\n      <Coll_Id>'
            + self.classeur + "</Coll_Id>\n      <Res_Id>" + str(res_id) +
            "</Res_Id>\n      <IndexList>\n")

        for key, value in index.items():
            payload += (
                "        <Index>\n            <Id>1</Id>\n            <Label>"
                + key + "</Label>\n            <Value>" + value +
                "</Value>\n        </Index>\n")

        payload += "      </IndexList>\n      <ArrayOfIndexInput/>\n      <Mode>UpdateGiven</Mode>\n      <Access_token></Access_token>\n    </updateDoc>\n  </soap:Body>\n</soap:Envelope>\n"

        # Headers de la requête
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "urn:Zeendoc#updateDoc",
            "Cookie": "ZeenDoc=c88d73cfd3fd7600bf9a6efb94e01599",
        }

        # Envoi de la requête
        response = requests.request("POST", url, headers=headers, data=payload)

        # Traitement de la réponse
        return response.text

    def updateDocPaiement(self, res_id):
        """fonction qui permet de mettre à jour le doc paiement
        res_id: id du doc

        Statut de paiement

        """

        return self.updateDoc(res_id, {self.indexPaiement: "1"})
