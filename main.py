import heapq

def prim_mst(graph, start):
    """
    Build a minimum spanning tree (MST) using a Prim-style algorithm.

    graph: dict mapping node -> list of (neighbor, weight) pairs.
           The graph is undirected (neighbors listed in both directions).
    start: starting node for Prim's algorithm.

    Return:
        (mst_edges, total_cost)
        - mst_edges: list of (u, v, w) edges in the MST.
        - total_cost: sum of weights w in all MST edges.
    """

    # Step 1: MST meaning (short summary)
    # An MST is a set of edges connecting all nodes with the minimum total weight and no cycles.

    # Step 2: Simple re-phrasing
    # "Grow a cheapest possible tree that connects every node."

    # Step 3: Data structures
    visited = set()
    mst_edges = []
    total_cost = 0
    pq = []  # min-heap storing (weight, u, v)

    # Step 4: Start by marking the start node and pushing its edges
    visited.add(start)
    for (nbr, w) in graph[start]:
        heapq.heappush(pq, (w, start, nbr))

    # Step 5: Prim's loop
    # Repeatedly pick the smallest edge that connects to an unvisited node.
    while pq and len(visited) < len(graph):
        w, u, v = heapq.heappop(pq)

        if v in visited:
            continue  # skip edges leading to visited nodes

        # Accept this edge into the MST
        visited.add(v)
        mst_edges.append((u, v, w))
        total_cost += w

        # Push all edges out of v
        for (nbr, wt) in graph[v]:
            if nbr not in visited:
                heapq.heappush(pq, (wt, v, nbr))

    return mst_edges, total_cost


if __name__ == "__main__":
    # Optional manual test
    sample_graph = {
        "G1": [("G2", 4), ("G3", 2)],
        "G2": [("G1", 4), ("G3", 3)],
        "G3": [("G1", 2), ("G2", 3)],
    }
    edges, cost = prim_mst(sample_graph, "G1")
    print("Sample MST edges:", edges)
    print("Total cost:", cost)
