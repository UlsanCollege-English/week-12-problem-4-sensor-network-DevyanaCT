from main import prim_mst

graph = {
    "A": [("B", 3), ("C", 1), ("D", 4)],
    "B": [("A", 3), ("C", 2), ("D", 5)],
    "C": [("A", 1), ("B", 2), ("D", 1)],
    "D": [("A", 4), ("B", 5), ("C", 1)],
}
mst_edges, total_cost = prim_mst(graph, "A")
print(f"MST edges: {mst_edges}")
print(f"Total cost: {total_cost}")
print(f"Expected: 1 + 1 + 3 = {1 + 1 + 3}")

# Analyze the MST
# Starting from A:
# - A-C: 1 (add C)
# - From C: C-D: 1 (add D) 
# - From C or D, what's next? B can be reached via C-B: 2 or A-B: 3
# - So: A-C: 1, C-D: 1, C-B: 2
# - Total: 4

# BUT test expects: 1 + 1 + 3 = 5
# That would be: A-C: 1, C-D: 1, A-B: 3
# Which is NOT optimal - C-B: 2 is cheaper than A-B: 3

print("\nThe test expectation (5) seems wrong. Optimal is 4.")
print("Optimal MST: A-C(1), C-D(1), C-B(2) = 4")
