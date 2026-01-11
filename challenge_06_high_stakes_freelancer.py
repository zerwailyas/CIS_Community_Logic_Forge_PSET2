def maximize_freelance_profit(deadlines, profits):
    jobs = list(zip(profits, deadlines))
    
    jobs.sort(reverse=True, key=lambda x: x[0])

    max_deadline = max(deadlines)
    parent = list(range(max_deadline + 1))

    def find(slot):
        if parent[slot] != slot:
            parent[slot] = find(parent[slot])
        return parent[slot]

    def union(u, v):
        parent[find(u)] = find(v)

    total_jobs = 0
    total_profit = 0

    for profit, deadline in jobs:
        available_slot = find(deadline)

        if available_slot > 0:
            total_jobs += 1
            total_profit += profit
            # Mark this slot as occupied
            union(available_slot, available_slot - 1)

    return [total_jobs, total_profit]

# Example usage
deadlines = [4, 1, 1, 1]
profits = [20, 10, 40, 30]
print(maximize_freelance_profit(deadlines, profits))