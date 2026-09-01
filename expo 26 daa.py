def job_sequencing(jobs):
    """
    jobs format: [(job_id, deadline, profit), ...]
    """
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)
    
    total_profit = 0
    scheduled = []

    for job_id, deadline, profit in jobs:
        for j in range(min(max_deadline, deadline), 0, -1):
            if slots[j] == -1:
                slots[j] = job_id
                total_profit += profit
                scheduled.append(job_id)
                break

    return scheduled, total_profit

jobs = [('J1', 2, 100), ('J2', 1, 19), ('J3', 2, 27), ('J4', 1, 25), ('J5', 3, 15)]
scheduled, max_profit = job_sequencing(jobs)
print(f"Scheduled Jobs: {scheduled}, Total Profit: {max_profit}")
