import math

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def closest_pair(pts):
    pts = sorted(pts, key=lambda x: x[0])
    
    def _closest(px):
        n = len(px)
        if n <= 3:
            return min((distance(px[i], px[j]), (px[i], px[j])) 
                       for i in range(n) for j in range(i + 1, n))

        mid = n // 2
        mid_x = px[mid][0]
        
        d_left, pair_left = _closest(px[:mid])
        d_right, pair_right = _closest(px[mid:])
        
        d, min_pair = (d_left, pair_left) if d_left < d_right else (d_right, pair_right)

        strip = [p for p in px if abs(p[0] - mid_x) < d]
        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1]) >= d:
                    break
                dist = distance(strip[i], strip[j])
                if dist < d:
                    d, min_pair = dist, (strip[i], strip[j])

        return d, min_pair

    return _closest(pts)

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
min_dist, pair = closest_pair(points)
print(f"Closest Distance: {min_dist:.2f} between {pair}")
