import numpy as np
import math
from collections import deque

class Node:
    def __init__(self, lat, long, alt, name):
        self.coord = cartesian_coordinates(lat, long, alt)
        self.name = name
    def get_coord(self):
        return self.coord
    def get_name(self):
        return self.name

earth_radius = 6371

# transforms the given latitude, longitude and altitude of satellite into Cartesian coordinates
# so that earth's center is origo
def cartesian_coordinates(lat, long, alt):
    psi = math.radians(lat)
    theta = math.radians(long)
    r = alt + earth_radius
    x = r*math.cos(psi)*math.cos(theta)
    y = r*math.cos(psi)*math.sin(theta)
    z = r*math.sin(psi)
    return [x, y, z]

def euclidean_norm(vector):
    return math.sqrt(sum([math.pow(elem,2) for elem in vector]))

# tests if two coordinates [x, y, z] have a line of sight (not cutting the globe)
def can_see(u, v):
    u = np.array(u)
    v= np.array(v)
    ratio = -np.dot((u-v), v)/np.dot(u-v, u-v)
    if ratio > 1 or ratio < 0:
        return True
    point = v + (u-v)*ratio
    return euclidean_norm(point) >= earth_radius

# Breadth first search (BFS) algorithm to find the shortest route
def bfs_satellites(file):
    table = [row.strip().split(',') for row in file]

    satellites = []
    start = Node(float(table[21][1]),float(table[21][2]), 0, "START")
    satellites.append(start)
    for i in range(1, 21):
        row = table[i]
        lat = float(row[1])
        long =float(row[2])
        alt = float(row[3])
        sat = Node(lat, long, alt, row[0])
        satellites.append(sat)

    end = Node(float(table[21][3]),float(table[21][4]), 0, "END")
    satellites.append(end)

    route ={"END" : "-1"}
    queue = deque([end])

    while(queue):
        node = queue.popleft()
        for sat in satellites:
            if route.has_key(sat.get_name()) == False and can_see(node.get_coord(), sat.get_coord()):
                queue.append(sat)
                route[sat.get_name()] = node.get_name()

    s = route["START"]
    while(s != "END"):
        print s+ ",",
        s = route[s]

if __name__ == '__main__':
    bfs_satellites(open("generate.txt", "rb"))