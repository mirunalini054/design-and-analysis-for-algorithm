def max_cut_greedy(nodes, edges):
    set_A, set_B = set(), set()
    
    for u in nodes:
        # Assign u to partition maximizing cross edges
        edges_to_A = sum(1 for v in set_A if (u, v) in edges or (v, u) in edges)
        edges_to_B = sum(1 for v in set_B if (u, v) in edges or (v, u) in edges)
        
        if edges_to_A < edges_to_B:
            set_A.add(u)
        else:
            set_B.add(u)
            
    cut_edges = [(u, v) for u, v in edges if (u in set_A and v in set_B) or (u in set_B and v in set_A)]
    return set_A, set_B, len(cut_edges)

nodes = [0, 1, 2, 3]
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
A, B, cut_size = max_cut_greedy(nodes, edges)
print(f"Partition A: {A}, Partition B: {B}, Cut Size: {cut_size}")
