class ProblemClassifier:
    """Conceptual mapping of complexity classes."""
    def __init__(self):
        self.database = {
            "Merge Sort": {"class": "P", "verifier": "O(n log n)", "solver": "O(n log n)"},
            "Dijkstra Shortest Path": {"class": "P", "verifier": "O(E log V)", "solver": "O(E log V)"},
            "0/1 Knapsack Decision": {"class": "NP-Complete", "verifier": "O(n)", "solver": "O(2^n)"},
            "Travelling Salesperson (TSP)": {"class": "NP-Hard", "verifier": "O(n)", "solver": "O(n! / 2^n)"},
            "N-Queens": {"class": "NP", "verifier": "O(n)", "solver": "O(n!)"},
            "Graph 3-Coloring": {"class": "NP-Complete", "verifier": "O(V + E)", "solver": "O(3^V)"}
        }

    def check_complexity(self, problem_name):
        return self.database.get(problem_name, "Problem classification not found")

classifier = ProblemClassifier()
print("TSP Info:", classifier.check_complexity("Travelling Salesperson (TSP)"))
print("Merge Sort Info:", classifier.check_complexity("Merge Sort"))
