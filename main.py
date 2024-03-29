import argparse
from api import lister_parties, débuter_partie, jouer_coup


# on pose la vairable gamestate, avec laquelle ma fonction a été programée
gamestate = 'état'

# première fonction, sert à récupérer les commanees tapées dans le terminal
def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', action='store_true',
     help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    analyser_commande.idul = args.idul
    if args.lister:
        return lister_parties(args.idul)
    return args

# sert à activer la fonction analyser commande
if __name__ == '__main__':
    analyser_commande()

# deuxieme fonction, sert à afficher le damier à partir d'un état fourni
def afficher_damier_ascii(gamestate):
    # sert à créer les parties du damier qui ne changeront jamais,
    # soit les deux lignes du haut et du bas
    haut = f'Légende: 1={analyser_commande.idul}, 2=automate\n'
    haut += '   -----------------------------------\n'
    bas = '--|-----------------------------------\n'
    bas += '  | 1   2   3   4   5   6   7   8   9'
    # On initialise une liste vide, dans laquelle on définit
    # deux types de rangées, les rangées contenant
    # les chiffres (style 1) et les rangées vides (style 2).
    # On finit par ajouter ces fonctions dans la liste vide,
    # une apres l'autre.
    # Cela permet de faire une liste contenant chaque lignes.
    # Chaque ligne est elle-même une liste contenant chaque caractère.
    liste_vide = []
    for i in range(18, 1, -1):
        style_damier_1 = list(f"{i // 2} | .   .   .   .   .   .   .   .   . |")
        style_damier_2 = list("  |                                   |")
        if i%2 == 0:
            liste_vide.append(style_damier_1)
        else:
            liste_vide.append(style_damier_2)
    # La position de chaque joueur est placée dans le damier,
    # à l'aide de sa position en 'y' et en 'x'.
    # On utilise la position en 'y' en premier
    # afin d'aller chercher la ligne,
    # puis la position en 'x',
    # pour aller chercher la position précise.
    # Puisque les indices des colonnes diminuent
    # à mesure que l'on monte dans le damier,
    # la valeur de 'y' fournie est soustraite de 18
    # (le nombre de lignes totales)
    # et est multipliée par 2
    # afin de toujours rester sur les lignes avec des chiffres.
    # On utilise un raisonnemnt similaire pour la coordonnée 'x' des joueurs.
    for i in range(2):
        y = 18 - 2 * gamestate["joueurs"][i]["pos"][1]
        x = 4 * gamestate["joueurs"][i]["pos"][0]
        liste_vide[y][x] = f'{i+1}'
    # On utilise une méthode presqu'identique à celle pour placer les joueurs,
    # à la différence près que l'on rajoute
    # une 2e boucle afin de placer chacun des caractères supplémentaires
    # à ceux donnés pour les "origines" des murs.
    # (dans le cas des murs horizontaux, les '-' subséquents
    # à celui désigné par la position de la commande)
    for i in range(len(gamestate["murs"]["horizontaux"])):
        for j in range(7):
            x = 4 * gamestate["murs"]["horizontaux"][i][0] + j - 1
            y = 19 - 2 * gamestate["murs"]["horizontaux"][i][1]
            liste_vide[y][x] = '-'
    
    for i in range(len(gamestate["murs"]["verticaux"])):
        for j in range(3):
            y = 18 - 2 * gamestate["murs"]["verticaux"][i][1]-j
            x = 4 * gamestate["murs"]["verticaux"][i][0] - 2
            liste_vide[y][x] = '|'
    
    # On crée ensuite une liste vide
    damier = []

    # Dans cette liste vide, on ajoute chaque élément,
    # (ici chaque ligne du damier modifiée)
    # un par un, séparés par des sauts de ligne.
    # On peut finalement les joindre et les faire
    # s'afficher à la console avec la fonction print.
    for ligne in liste_vide:
        damier += ligne + ['\n']
    a = ''.join(damier)
    print(haut + a + bas)

# cette section du code sert à faire fonctionner le jeu.
# Tout d'abord on débute une partie.
# Si le serveur peut être contacté, on utilise l'état
# pour afficher le damier, sinon on affiche le message d'erreur.
# On commence ensuite la boucle, qui continue tant que
# l'on ne recoit pas de message d'erreur, auquel cas elle l'affiche.
tuple_id_état = débuter_partie(analyser_commande.idul)
if len(tuple_id_état) > 1:
    afficher_damier_ascii(tuple_id_état[1])
    while True:
        a = input('type de coup (D, MH, MV): ')
        b = input('''position de l'action (x,y): ''')
        yolo = jouer_coup(tuple_id_état[0], a, b)
        if type(yolo) == str:
            print(yolo)
            break
        afficher_damier_ascii(yolo)
else:
    print(tuple_id_état)