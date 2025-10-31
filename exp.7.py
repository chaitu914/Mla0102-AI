from collections import deque

def water_jug():
    cap4, cap3, goal = 4, 3, 2
    visited, q = set(), deque([(0, 0)])

    while q:
        x, y = q.popleft()
        print((x, y))
        if x == goal:
            print("✅ Goal reached!")
            return
        if (x, y) in visited:
            continue
        visited.add((x, y))

        q += [
            (cap4, y), (x, cap3), (0, y), (x, 0),
            (x - min(x, cap3 - y), y + min(x, cap3 - y)),
            (x + min(y, cap4 - x), y - min(y, cap4 - x))
        ]

water_jug()
