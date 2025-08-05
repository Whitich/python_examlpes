import sys
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def get_points(n):
    points = []
    for i in range(n):
        while True:
            try:
                x = float(input(f"{i+1}. nokta için X koordinatı: "))
                y = float(input(f"{i+1}. nokta için Y koordinatı: "))
                points.append((x, y))
                break
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")
    return points

def calculate_distances(points):
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):  # Tekrarsız karşılaştırma
            dist = euclidean_distance(points[i], points[j])
            distances.append((dist, points[i], points[j]))
    return distances

def find_min_distance(distances):
    min_distance = min(distances, key=lambda d: d[0])
    return min_distance

def main():
    try:
        n = int(input("Kaç nokta gireceksiniz?: "))
        if n < 2:
            print("En az iki nokta girilmelidir.")
            return
    except ValueError:
        print("Geçerli bir sayı giriniz.")
        return

    points = get_points(n)
    distances = calculate_distances(points)

    print("\nGirilen Noktalar:")
    for i, p in enumerate(points, 1):
        print(f"{i}. Nokta: {p}")

    print("\nTüm Mesafeler:")
    for dist, p1, p2 in distances:
        print(f"{p1} ile {p2} arası mesafe: {dist:.2f}")

    min_dist, p1, p2 = find_min_distance(distances)
    print(f"\nEn kısa mesafe: {min_dist:.2f} ({p1} ile {p2} arasında)")

if __name__ == "__main__":
    main()
