import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('idul', type=str, help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', metavar='', help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    return args



print(analyser_commande())


if __name__ =='__main__':
    analyser_commande()


def afficher_damier_ascii(gamestate):
    version_1 = f'Légende: 1={idul}, 2=automate \n'
    version_1 += '   ' + 35 * '-' + '\n'
    version_1 += '9 | .   .   .   .   .   .   .   .   . |\n  |                                   |\n8 | .   .   .   .   .   .   .   .   . |  \n|                                   |\n7 | .   .   .   .   .   .   .   .   . |  \n|                                   |\n6 | .   .   .   .   .   .   .   .   . |\n
  |                                   |\n
5 | .   .   .   .   .   .   .   .   . |\n
  |                                   |\n
4 | .   .   .   .   .   .   .   .   . |\n
  |                                   |\n
3 | .   .   .   .   .   .   .   .   . |\n   |                                   |\n2 | .   .   .   .   .   .   .   .   . |\n    |                                   |\n1 | .   .   .   .   .   .   .   .   . |\n    --|-----------------------------------\n| 1   2   3   4   5   6   7   8   9'
    print(version_1)

print(afficher_damier)
