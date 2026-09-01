class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot:
            return False
        if self.rank[xroot] < self.rank[yroot]:
            xroot, yroot = yroot, xroot
        self.parent[yroot] = xroot
        if self.rank[xroot] == self.rank[yroot]:
            self.rank[xroot] += 1
        return True

def kruskal(vertices, edges):
    """
    edges format: [(weight, u, v), ...]
    """
    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0

    # Sort edges by weight
    for w, u, v in sorted(edges):
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight

nodes = ['A', 'B', 'C', 'D', 'E']
edge_list = [
    (1, 'A', 'B'), (3, 'A', 'C'), (3, 'B', 'C'),
    (6, 'B', 'D'), (4, 'C', 'D'), (2, 'C', 'E'), (5, 'D', 'E')
]
mst_edges, weight = kruskal(nodes, edge_list)
print(f"MST Edges: {mst_edges}, Total Weight: {weight}")
