from ftplib import FTP
import os


def envoyer_document_ftp(adresse, port, utilisateur, mot_de_passe, chemin_fichier_local, chemin_fichier_distant):
    try:
        # Se connecter au serveur FTP
        ftp = FTP()
        ftp.connect(adresse, port)
        ftp.login(utilisateur, mot_de_passe)

        # Ouvrir le fichier local en mode binaire
        with open(chemin_fichier_local, 'rb') as fichier_local:
            # Envoyer le fichier vers le serveur FTP
            ftp.storbinary('STOR ' + chemin_fichier_distant, fichier_local)

        # Fermer la connexion FTP
        ftp.quit()
        print("Le document a été envoyé avec succès.")
        # Supprimer le fichier local
        os.remove(chemin_fichier_local)

    except Exception as e:
        print("Une erreur s'est produite lors de l'envoi du document :", str(e))


def envoyer_docs_dossier(adresse, port, utilisateur, mot_de_passe, chemin_dossier_local, chemin_fichier_distant):
    for fichier in os.listdir(chemin_dossier_local):
        envoyer_document_ftp(adresse, port, utilisateur, mot_de_passe,
                             chemin_dossier_local + fichier, chemin_fichier_distant + fichier)


# Utilisation de la fonction
adresse_ftp = "depotftp.zeendoc.com"
port_ftp = 21
utilisateur_ftp = "1axsg5rd6on3e2x2wni0"
mot_de_passe_ftp = "emwf8owgczycnf4wsc9q"
chemin_dossier_local = "C:/Users/Antonin/Desktop/Test_solstyce/"
chemin_fichier_distant = "/"

envoyer_docs_dossier(adresse_ftp, port_ftp, utilisateur_ftp,
                    mot_de_passe_ftp, chemin_dossier_local, chemin_fichier_distant)
