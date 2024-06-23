# Noktaların tanımlanması
points = [(1, 2), (3, 4)] 

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

print("Noktalar arasındaki minimum Öklid mesafesi:", min_distance)
