Projet : Algorithme de Dijkstra pour la recherche de chemin optimal

Description du projet : Le but de ce projet est de concevoir un algorithme permettant de trouver le chemin le moins coûteux entre deux points dans une ville représentée par une matrice d'adjacence. Chaque cellule de cette matrice représente un lieu dans la ville, et les valeurs dans la matrice représentent le coût de passage à travers ce lieu. Les obstacles sont représentés par la valeur -1, empêchant l'accès à ces cellules.

L'algorithme utilisé pour résoudre ce problème est l'algorithme de Dijkstra, une méthode classique de recherche de chemin dans les graphes qui trouve le chemin le plus court entre un point de départ et un point d'arrivée dans un graphe pondéré.

Fonctionnement du code :

    Représentation de la ville : La ville est modélisée par une matrice où chaque élément représente un lieu ou un obstacle :
        Les valeurs positives indiquent le coût pour accéder à cette cellule.
        Les valeurs -1 représentent des obstacles infranchissables.

    Initialisation de l'algorithme de Dijkstra : L'algorithme commence par attribuer une distance infinie à toutes les cellules, sauf celle de départ, qui a la valeur du coût d'accès. Un tableau de prédécesseurs est également initialisé pour retracer le chemin optimal.

    Exploration des voisins : À chaque étape, l'algorithme explore les voisins accessibles de la cellule actuelle (haut, bas, gauche, droite), en ajoutant ceux-ci à une file de priorité (utilisant un tas de type heapq pour garantir que la cellule avec le coût minimal soit explorée en premier).

    Mise à jour des distances : Lorsqu'un voisin est exploré, sa distance est mise à jour si un chemin plus court est trouvé. Cette mise à jour est également reflétée dans la structure des prédécesseurs pour pouvoir reconstruire le chemin une fois l'algorithme terminé.

    Reconstruire le chemin optimal : Une fois que l'algorithme atteint la cellule d'arrivée, le chemin est reconstruit en suivant les prédécesseurs depuis l'arrivée jusqu'au départ.

Exemple d'utilisation : Dans l'exemple de la ville, une matrice représente le réseau de rues avec des coûts associés pour chaque zone. L'algorithme de Dijkstra est appliqué pour trouver le chemin optimal entre le point de départ (0, 0) et le point d'arrivée (4, 4), en prenant en compte les obstacles.

Résultats : L'algorithme retourne le coût minimal pour parcourir ce chemin ainsi que le trajet optimal, qui est la série de cellules à traverser pour atteindre l'objectif.

Caractéristiques :

    La complexité de l'algorithme de Dijkstra est de O((E + V) log V), où E est le nombre d'arêtes et V le nombre de sommets. Dans ce cas, chaque cellule représente un sommet, et chaque connexion entre cellules adjacentes représente une arête.
    Ce projet montre comment résoudre efficacement des problèmes de pathfinding dans un environnement où les obstacles et les coûts sont présents.

Améliorations possibles :

    Ajouter des capacités pour gérer des graphes dynamiques ou plus complexes, où les coûts des cellules peuvent varier dans le temps.
    Optimiser la gestion de la mémoire et du temps d'exécution pour de très grands graphes.
