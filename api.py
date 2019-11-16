import requests




    


def lister_parties(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.get(url_base+'lister/', params={'idul': f'{idul}'})
    if rep.status_code == 200:
        rep = rep.json()
        print(rep)

    else:
        print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")
        raise RuntimeError(idul)

