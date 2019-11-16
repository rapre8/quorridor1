import argparse
from api import lister_parties


état = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [5, 5]}, 
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ], 
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], 
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
}


gamestate = état

def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', metavar='', help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    return args

if __name__ =='__main__':
    analyser_commande()


def afficher_damier_ascii(gamestate):
    
    haut = f'Légende: 1={gamestate["joueurs"][0]["nom"]}, 2=automate\n'
    haut += '   -----------------------------------\n'
    bas = '--|-----------------------------------\n'
    bas += '  | 1   2   3   4   5   6   7   8   9'
    liste_vide = []
    for i in range(18,1,-1):
        style_damier_1 = list(f"{i//2} | .   .   .   .   .   .   .   .   . |")
        style_damier_2 = list("  |                                   |")
        if i%2 == 0:
            liste_vide.append(style_damier_1)
        else:
            liste_vide.append(style_damier_2)
            
            
    for i in range(2):
        liste_vide[18-2*gamestate["joueurs"][i]["pos"][1]][4*gamestate["joueurs"][i]["pos"][0]] = f'{i+1}'
    
    
    for i in range(len(gamestate["murs"]["horizontaux"])):
        for j in range(7):
            liste_vide[19-2*gamestate["murs"]["horizontaux"][i][1]][4*gamestate["murs"]["horizontaux"][i][0]+j-1] = '-'
    
    for i in range(len(gamestate["murs"]["verticaux"])):
        for j in range(3):
            liste_vide[18-2*gamestate["murs"]["verticaux"][i][1]-j][4*gamestate["murs"]["verticaux"][i][0]-2] = '|'


    
    damier = []
    for ligne in liste_vide:
        damier += ligne + ['\n']
    a = ''.join(damier)
    
    
    
    print(haut + a + bas)

afficher_damier_ascii(gamestate)