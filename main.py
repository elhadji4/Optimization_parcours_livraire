import heapq

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix # Matrice d'adjacence (représentant le graphe)
        self.rows = len(matrix)  # Nombre de lignes
        self.cols = len(matrix[0]) # On suppose que la matrice est rectangulaire

    def get_neighbors(self, x, y):
        """Retourne les voisins accessibles (sans obstacle) d'une cellule (x, y)."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, Bas, Gauche, Droite
        neighbors = []
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.matrix[nx][ny] != -1:
                neighbors.append((nx, ny))
        
        return neighbors

    def dijkstra(self, start, end):
        """Trouve le chemin le moins coûteux entre start et end en utilisant Dijkstra."""
        x_start, y_start = start
        x_end, y_end = end

        # Initialisation
        distances = { (i, j): float('inf') for i in range(self.rows) for j in range(self.cols) }
        distances[start] = self.matrix[x_start][y_start]
        predecessors = { (i, j): None for i in range(self.rows) for j in range(self.cols) }

        priority_queue = [(self.matrix[x_start][y_start], start)]  # (coût, (x, y))

        while priority_queue:
            current_distance, (x, y) = heapq.heappop(priority_queue)

            if (x, y) == end:  # Arrivé à la destination
                break

            for nx, ny in self.get_neighbors(x, y):
                new_distance = current_distance + self.matrix[nx][ny]

                if new_distance < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_distance
                    predecessors[(nx, ny)] = (x, y)
                    heapq.heappush(priority_queue, (new_distance, (nx, ny)))

        # Reconstruire le chemin
        path = []
        node = end
        while node:
            path.append(node)
            node = predecessors[node]
        path.reverse()

        return distances[end], path

# Exemple de ville
ville = [
    [1, 3, 1, 1, -1],
    [1, -1, 1, -1,  1],
    [4,  1, 1,  3,  1],
    [1, -1, 1,  1,  1],
    [1,  1, 2, -1,  1]
]

graph = Graph(ville)
start, end = (0, 0), (4, 4)
cost, path = graph.dijkstra(start, end)

# Affichage des résultats
print("Coût minimal :", cost)
print("Chemin optimal :", path)
print("Longueur du chemin :", len(path))
