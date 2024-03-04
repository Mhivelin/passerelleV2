import requests
import json
import sys
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError, InvalidClientError
# from app.models.database import get_db_connection
from flask import jsonify, url_for



class EBP:
    
    def __init__(self, id) -> None:
        
        
        res = self.BdGetClientEBP(id)

        
        self.idDB = id
        self.client_id = res['EBP_CLIENT_ID']
        self.client_secret = res['EBP_CLIENT_SECRET']
        self.ebp_subscription_key = res['EBP_SUBSCRIPTION_KEY']
        self.ebp_folder_id = res['EBP_FOLDER_ID']
        
        if res['TOKEN_DEFINED'] == 1:
            print ('token defined')
            print(res['TOKEN'])
            #{"id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjVDNzI4RTIxOTYwQURBODdCQkQ5M0I5QTgwNjgxRURFRjhFRkI5QTQiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJYSEtPSVpZSzJvZTcyVHVhZ0dnZTN2anZ1YVEifQ.eyJuYmYiOjE3MDkxMTExMjYsImV4cCI6MTcwOTExMTQyNiwiaXNzIjoiaHR0cHM6Ly9hcGktbG9naW4uZWJwLmNvbSIsImF1ZCI6Imp1cGl0ZXJ3aXRob3V0cGtjZSIsImlhdCI6MTcwOTExMTEyNiwiYXRfaGFzaCI6IjVzb2pJTGZWQ3E1SGtyOHJKQlR4aWciLCJzdWIiOiI0Yzk1MWRiNi1jOTE0LTRmMTUtOWZkMC0xOThiY2Q0M2E2ODgiLCJhdXRoX3RpbWUiOjE3MDkwMjY5ODYsImlkcCI6IkVicExvZ2luVjIiLCJhbXIiOlsicHdkIl19.AerAJ5rbLA5I3GSVtUjSq6Qg6rDVyhubc9amyAqn2Abakn_h7bn--hHvpoFSqveCF8l6G1L7k2s1BdqyOgFBRhWYiXfGXlJuM_1CXIMvsayRFYlFrXHCs-7JgLuijkIYRecz2xfD4xAncQW8JFvU8hw0F95_EaAbTzUz7E8cOLs_Y1h4_t3IZcYc3BSeXOaGKiUh4oykiEFSQWLb4iKJHziXa0hBjVfwiboPSAW6iPgZ52_MMu5sDptuB0mTkh3caeVZ5HnX1pbiIMiKr5_xPp5e7f-aOLzEOwnfnP5NJU29mxRPeLpovtmUQqzYkDIt0Rq0woGxO4LWo9Yqiz0VAA", "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjVDNzI4RTIxOTYwQURBODdCQkQ5M0I5QTgwNjgxRURFRjhFRkI5QTQiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJYSEtPSVpZSzJvZTcyVHVhZ0dnZTN2anZ1YVEifQ.eyJuYmYiOjE3MDkxMTExMjYsImV4cCI6MTcwOTExNDcyNiwiaXNzIjoiaHR0cHM6Ly9hcGktbG9naW4uZWJwLmNvbSIsImNsaWVudF9pZCI6Imp1cGl0ZXJ3aXRob3V0cGtjZSIsInN1YiI6IjRjOTUxZGI2LWM5MTQtNGYxNS05ZmQwLTE5OGJjZDQzYTY4OCIsImF1dGhfdGltZSI6MTcwOTAyNjk4NiwiaWRwIjoiRWJwTG9naW5WMiIsImVicC5lbWFpbCI6Im1hcml1cy5oaXZlbGluQGdtYWlsLmNvbSIsIm5hbWUiOiJNYXJpdXMgSGl2ZWxpbiIsInNfaGFzaCI6IkMxd1hyYzZrTzJlTnZoUG1tRVl1QVEiLCJmYW1pbHlfbmFtZSI6IkhpdmVsaW4iLCJnaXZlbl9uYW1lIjoiTWFyaXVzIiwiZW1haWwiOiJtYXJpdXMuaGl2ZWxpbkBnbWFpbC5jb20iLCJodHRwOi8vbG9naW4uc2NoZW1hcy5lYnAuY29tL2lkZW50aXR5L2NsYWltcy9Db2RlVGllcnMiOiIwMDAxNjg0NjI5IiwiaHR0cDovL2xvZ2luLnNjaGVtYXMuZWJwLmNvbS9pZGVudGl0eS9jbGFpbXMvQ29udGFjdElkIjoiNTU5MTI0NyIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicHdkIl19.jNZ-iCO6rOJIhWBm0r6zxs_TmRd9E7sps9wYY7lSbnObOafqEbxcQymvwpczbJ8CgdrwOBQIU16Pu35T1R7EkZr-lUGqYI7fZwt69qoPB0L_2fISyB6i3fvYHy1EiJ5QK4gqTOiiKjE9T9Qe2BM0KN58wz_hPDBvkzqkRgzaa-m_7-Oto5ypK1Jksw5oEGRhCkh-kNduKPvqSP1hu4h2gHjVvOSUxUOGXanvmePu0aSRSNdNYNH39w2RY8tkhw5BgqVCxFOqb1905fRp8sbExAN03Vdmlt6mivx_F-podSB486ecAdP7wAe1kKWFufisFUIi1f4JPCwFm8o--fLKmg", "expires_in": 3600, "token_type": "Bearer", "refresh_token": "VVAe5cFKG9l3Dh3nyQrEH9fsBWPrvTvRhWFBSbE07q8", "scope": ["openid", "profile", "offline_access"], "expires_at": 1709114726.334089}
            self.token = json.loads(res['TOKEN'])
            
        
        
        
        
        # login = self.login()
        # print('login test')
        # print(login)
        
        
        
        
        
    # def getModelBD(self):
    #     conn = get_db_connection()
        
    #     champs = conn.execute("PRAGMA table_info('CLIENT_EBP')").fetchall()
        
    #     return champs
        
                    
    # def BdGetClientEBP(self, id) :
    #     conn = get_db_connection()
        
    #     try:
    #         client = conn.execute("SELECT EBP_CLIENT_ID, EBP_CLIENT_SECRET, EBP_SUBSCRIPTION_KEY, EBP_FOLDER_ID, CASE WHEN TOKEN IS NULL THEN 0 ELSE 1 END AS TOKEN_DEFINED, TOKEN FROM CLIENT_EBP WHERE id = ?", (id,)).fetchone()
    #         return dict(client)
    #     except:
    #         print('erreur lors de la récupération du client EBP')
    #         return jsonify({'error': 'Client EBP non trouvé'}), 404
    #     finally:
    #         conn.close()
    
        
    # def login(self):
    #     ''' Fonction qui permet de se connecter à l'API EBP. '''

    #     authorization_base_url = 'https://api-login.ebp.com/connect/authorize'
    #     token_url = 'https://api-login.ebp.com/connect/token'
    #     redirect_uri = url_for('ebp.SinginRedirect', _external=True)
    #     scope = ["openid", "profile", "offline_access"]

    #     # Essayez de récupérer le token de la base de données
    #     token = None
    #     conn = get_db_connection()
    #     try:
    #         token_row = conn.execute(
    #             "SELECT TOKEN FROM CLIENT_EBP WHERE id = ?", (self.idDB,)).fetchone()
    #         if token_row:
    #             token = json.loads(token_row['TOKEN'])
                
    #     except Exception as e:
    #         print("Erreur lors de la récupération du token de la base de données:", e)
    #     finally:
    #         conn.close()

    #     if not token:
    #         try:
    #             # Créez une session OAuth2
    #             oauth = OAuth2Session(self.client_id, redirect_uri=redirect_uri, scope=scope)

    #             # Récupérez l'URL de redirection
    #             authorization_url, state = oauth.authorization_url(authorization_base_url)
    #             print('Aller à %s et autoriser l\'accès.' % authorization_url)
    #             authorization_response = input('Entrez l\'URL de redirection: ')

    #             # Récupérez le token
    #             token = oauth.fetch_token(token_url, authorization_response=authorization_response,
    #                                     client_secret=self.client_secret)
    #         except InvalidClientError as e:
    #             print("Erreur de client invalide lors de la récupération du token:", e)
    #             return "Erreur de client invalide lors de la récupération du token"
    #         except Exception as e:
    #             print("Erreur lors de la récupération du token:", e)
    #             return "Erreur lors de la récupération du token"

    #     # Créez une session avec le token
    #     oauth = OAuth2Session(self.client_id, token=token, auto_refresh_kwargs={
    #         'client_id': self.client_id, 'client_secret': self.client_secret},
    #         auto_refresh_url=token_url,
    #         token_updater=self.Bdtoken_saver)

    #     # Rafraîchissez le token si nécessaire
    #     try:
    #         token = oauth.refresh_token(token_url)
    #     except TokenExpiredError:
    #         token = oauth.refresh_token(token_url)
    #     except Exception as e:
    #         print("Erreur lors du rafraîchissement du token:", e)
    #         return None

    #     self.token = token
    #     # Enregistrez le nouveau token
    #     self.Bdtoken_saver(token)
        

    #     return token
    

    def callback(self, code):
        ''' Fonction qui gère le callback après l'autorisation de l'utilisateur. '''
        redirect_uri = url_for('ebp.SinginRedirect', _external=True)
        token_url = 'https://api-login.ebp.com/connect/token'
        
        
        
        
        try:
            oauth = OAuth2Session(self.client_id, redirect_uri=redirect_uri)
            token = oauth.fetch_token(token_url, client_secret=self.client_secret, code=code)

            # Enregistrez le nouveau token et créez une session
            self.Bdtoken_saver(token)
            return self.create_oauth_session(token)

        except Exception as e:
            print("Erreur lors de l'échange du code d'autorisation:", e)
            return None


    def create_oauth_session(self, token):
        ''' Crée et renvoie une session OAuth avec le token fourni. '''
        token_url = 'https://api-login.ebp.com/connect/token'
        return OAuth2Session(self.client_id, token=token, auto_refresh_kwargs={
            'client_id': self.client_id, 'client_secret': self.client_secret},
            auto_refresh_url=token_url,
            token_updater=self.Bdtoken_saver)
        

    # def Bdtoken_saver(self, token):
    #     '''
    #     Fonction qui permet de sauvegarder le token dans la base de données.
    #     '''
    #     conn = get_db_connection()
    #     try:
    #         # Conversion du token en chaîne JSON pour le stockage
    #         token_json = json.dumps(token)

    #         # Requête pour mettre à jour le token dans la base de données
    #         sql = """
    #             UPDATE CLIENT_EBP
    #             SET TOKEN = ?
    #             WHERE id = ?
    #         """
    #         conn.execute(sql, (token_json, self.idDB))
    #         conn.commit()
            
    #     except Exception as e:
    #         print("Erreur lors de la sauvegarde du token:", e)
    #     finally:
    #         conn.close()

    
    # def Bdtoken_clear(self):
    #     '''
    #     Fonction qui permet de supprimer le token de la base de données.
    #     '''
    #     conn = get_db_connection()
    #     try:
    #         # Requête pour supprimer le token de la base de données
    #         sql = """
    #             UPDATE CLIENT_EBP
    #             SET TOKEN = NULL
    #             WHERE id = ?
    #         """
    #         conn.execute(sql, (self.idDB,))
    #         conn.commit()
    #     except Exception as e:
    #         print("Erreur lors de la suppression du token:", e)
    #     finally:
    #         conn.close()
    
    
                            
    # def setFolder(self, folder_id):
    #     '''fonction qui permet setter les dossiers dans la base de données
    #     '''
    #     print('folder_id')
    #     print(folder_id)
    #     conn = get_db_connection()
    #     try:
    #         conn.execute("UPDATE CLIENT_EBP SET EBP_FOLDER_ID = ? WHERE id = ?", (folder_id, self.idDB))
    #         conn.commit()
    #     except:
    #         print('erreur lors de la mise à jour du dossier')
    #         # afficher l'erreur rencontrée
    #         print(sys.exc_info()[0])
    #     finally:
    #         conn.close()
            

    def get_folders(self):
        '''
        Fonction qui permet de récupérer les dossiers de l'API EBP.
        '''
        
        self.login()
        
        if self.token is None:
            return "Erreur lors de la récupération du token"
        
        
        
        
        url = "https://api-developpeurs.ebp.com/gescom/api/v1/Folders?Offset=0&Limit=100&Accept-Language=fr-FR"
        
        payload = {}
        headers = {
            'ebp-subscription-key': self.ebp_subscription_key,
            'Authorization': 'Bearer ' + self.token['access_token']
        }
        
        response = requests.request("GET", url, headers=headers, data=payload)
        
        response.json()
        # {'folders': [{'id': '298324', 'name': 'API DELTIC', 'shortName': 'INV40', 'isMariaDb': False}, {'id': '305435', 'name': 'test api', 'shortName': 'INV30', 'isMariaDb': False}, {'id': '306851', 'name': 'APIDELTIC2', 'shortName': 'INV40', 'isMariaDb': False}], 'paging': {'total': 3, 'returned': 3, 'offset': 0, 'limit': 100}}
        
        return response.json()['folders']
        

                    

            
    def getPaidPurchaseDocument(self, folder_id, SysModifiedDate = "1999-01-01"):


        url = "https://api-developpeurs.ebp.com/gescom/api/v1/Folders/" + folder_id + "/Documents/PurchaseDocument?Duration=30&DocumentType=null&ToDate=1999-01-01&SysModifiedDate=" + SysModifiedDate + "&Columns=DocumentNumber, Reference, CommitmentsBalanceDue&WhereCondition=%20%20type%3A%20CustomFilter%0A%20%20column%3A%20CommitmentsBalanceDue%0A%20%20operator%3A%20Equal%0A%20%20valueType%20%3A%20Decimal%0A%20%20value%3A%0A%20%20-%200"

        payload = {}
        headers = {
            'ebp-subscription-key': self.ebp_subscription_key,
            'Authorization': 'Bearer ' + self.token['access_token']
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        
        # print('response : ' + response.json())

        return json.dumps(response.json())
    
    
    
    
    def getSupplier(self):
        url = "https://api-developpeurs.ebp.com/gescom/api/v1/Folders/306851/GenericQuery?TableName=supplier&Columns=name, Id&=2020-11-06"

        payload = {}
        headers = {
        'ebp-subscription-key': self.ebp_subscription_key,
        'Authorization': 'Bearer ' + self.token['access_token']
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
