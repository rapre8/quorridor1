import requests



def lister_parties(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.get(url_base+'lister/', params={'idul': f'{idul}'})
    if rep.status_code == 200:
        rep = rep.json()
        try:
            if "message" in rep:
                raise RuntimeError
            else:
                return rep
        except RuntimeError:
            raise RuntimeError(rep['message'])
        

    else:
        print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")


lister_parties('rapre8')
        

