def vertex_cover_approx(edges):
    """
    Greedy 2-approximation algorithm for Minimum Vertex Cover.
    edges: set of tuples representing undirected edges.
    """
    uncovered = set(edges)
    cover = set()

    while uncovered:
        u, v = uncovered.pop()
        cover.add(u)
        cover.add(v)
        
        # Remove all edges covered by u or v
        uncovered = {e for e in uncovered if e[0] != u and e[1] != u and e[0] != v and e[1] != v}

    return cover

edge_list = {(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)}
print("Approximate Vertex Cover:", vertex_cover_approx(edge_list))
