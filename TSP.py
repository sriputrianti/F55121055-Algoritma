import itertools


def tsp_brute_force(graph, start):
    # Mendapatkan semua kemungkinan permutasi node
    nodes = list(graph.keys())
    nodes.remove(start)
    permutations = list(itertools.permutations(nodes))

    # Menghitung jarak total untuk setiap permutasi
    min_distance = float('inf')
    best_path = None

    for perm in permutations:
        current_path = [start] + list(perm) + [start]
        current_distance = 0

        for i in range(len(current_path) - 1):
            current_distance += graph[current_path[i]][current_path[i + 1]]

        if current_distance < min_distance:
            min_distance = current_distance
            best_path = current_path

    return best_path, min_distance


# Contoh penggunaan
graph = {
    'A': {'B': 5, 'C': 3, 'D': 5},
    'B': {'A': 5, 'C': 6, 'D': 4},
    'C': {'A': 3, 'B': 6, 'D': 2},
    'D': {'A': 5, 'B': 6, 'C': 2}
}
start_node = 'A'

best_path, min_distance = tsp_brute_force(graph, start_node)
print("Jalur terbaik:", best_path)
print("Jarak terpendek:", min_distance)
