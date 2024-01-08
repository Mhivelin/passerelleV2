import requests

# import PyPDF2


def connexion(email, cpassword, Url_client):

    password = ""

    # Construire l'URL en utilisant la variable Url_client
    url = f'https://armoires.zeendoc.com/{Url_client}/ws/3_0/Zeendoc.php'
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',  # Spécifiez le type de contenu SOAP
    }

    # Remplacez le contenu de la requête avec le corps SOAP
    data = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="urn:Zeendoc">
       <soapenv:Header/>
       <soapenv:Body>
          <ns1:login>
             <Login>{email}</Login>
             <Password>{password}</Password>
             <CPassword>{cpassword}</CPassword>
          </ns1:login>
       </soapenv:Body>
    </soapenv:Envelope>
    """

    # Envoyez la requête POST
    response = requests.post(url, data=data, headers=headers)

    # Vérifiez la réponse
    if response.status_code == 200:
        return response.content
    else:
        return f'Erreur lors de la requête. Code de statut : {response.status_code}'


def getSavedQueries(Coll_Id, Get_Nb_Results, session_id):
    url = f'https://armoires.zeendoc.com/{Url_client}/ws/3_0/Zeendoc.php'
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
    }

    # Remplacez le contenu de la requête avec le corps SOAP pour getSavedQueries
    data = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="urn:Zeendoc">
       <soapenv:Header>
          <SessionId>{session_id}</SessionId>
       </soapenv:Header>
       <soapenv:Body>
          <ns1:getSavedQueries>
             <Coll_Id>{Coll_Id}</Coll_Id>
             <Get_Nb_Results>{Get_Nb_Results}</Get_Nb_Results>
          </ns1:getSavedQueries>
       </soapenv:Body>
    </soapenv:Envelope>
    """

    # Envoyez la requête POST
    response = requests.post(url, data=data, headers=headers)

    # Vérifiez la réponse
    if response.status_code == 200:
        return response.content
    else:
        return f'Erreur lors de la requête. Code de statut : {response.status_code}'


# Exemple d'utilisation de la fonction de connexion
email = 'marius.hivelin@gmail.com'
cpassword = 'X?BSh:R92EmyDKi'
Url_client = 'deltic_demo'

response_content = connexion(email, cpassword, Url_client)
print('Réponse du serveur :', response_content)


# Exemple d'appel de la fonction getSavedQueries
Coll_Id = 'coll_1'
Get_Nb_Results = 1
# Vous devez obtenir ce session_id après avoir effectué la connexion
session_id = response_content.decode(
    'utf-8').split('<SessionId>')[1].split('</SessionId>')[0]

result = getSavedQueries(Coll_Id, Get_Nb_Results, session_id)
print(result)


def fusionDocs(listeDesBulletins, listeDesSyntheses, listeDesNotes, listeDesCourriers):
    # Créez un objet PDF de sortie vide
    pdf_final = PyPDF2.PdfFileWriter()

    # Fusionnez les bulletins de paie, synthèses, notes et courriers dans un ordre spécifique
    for documents in [listeDesBulletins, listeDesSyntheses, listeDesNotes, listeDesCourriers]:
        # Compteur de pages pour vérifier si nous devons ajouter une page blanche
        page_count = 0
        for document in documents:
            pdf = PyPDF2.PdfFileReader(document)
            for page_num in range(pdf.getNumPages()):
                page = pdf.getPage(page_num)
                pdf_final.addPage(page)
                page_count += 1

        # Si le nombre de pages est impair, ajoutez une page blanche
        if page_count % 2 != 0:
            blank_page = PyPDF2.PdfFileReader("blank_page.pdf").getPage(0)
            pdf_final.addPage(blank_page)

    # Créez un fichier PDF de sortie
    with open("pdf_final.pdf", "wb") as output_file:
        pdf_final.write(output_file)

    return "pdf_final.pdf"
