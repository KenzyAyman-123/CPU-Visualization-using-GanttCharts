import matplotlib.pyplot as plt

processes = [
    {"name": "P1", "arrival": 0, "burst": 3},
    {"name": "P2", "arrival": 1, "burst": 4},
    {"name": "P3", "arrival": 2, "burst": 2}
]

current_time = 0

print("FCFS Scheduling:\n")

for p in processes:
    start = max(current_time, p["arrival"])
    finish = start + p["burst"]
    
    
    print(f"{p['name']} runs from {start} to {finish}")
    
    current_time = finish

    gantt = []
current_time = 0

for p in processes:
    start = max(current_time, p["arrival"])
    finish = start + p["burst"]
    
    gantt.append((p["name"], start, finish))
    
    current_time = finish


fig, ax = plt.subplots()

for i, (name, start, finish) in enumerate(gantt):
    ax.barh(0, finish - start, left=start, align='center' , color='red')
    ax.text(start + (finish - start)/2, 0, name, ha='center', va='center', color='white')

ax.set_xlabel("Time")
ax.set_yticks([])
ax.set_title("FCFS Gantt Chart")

plt.show()

print("\nSJF Scheduling:\n")


sjf_processes = sorted(processes, key=lambda x: x["burst"])

current_time = 0
gantt = []

for p in sjf_processes:
    start = max(current_time, p["arrival"])
    finish = start + p["burst"]
    
    print(f"{p['name']} runs from {start} to {finish}")
    
    gantt.append((p["name"], start, finish))
    current_time = finish


fig, ax = plt.subplots()

for i, (name, start, finish) in enumerate(gantt):
    ax.barh(0, finish - start, left=start)
    ax.text(start + (finish - start)/2, 0, name, ha='center', va='center', color='white')

ax.set_xlabel("Time")
ax.set_yticks([])
ax.set_title("SJF Gantt Chart")

plt.show()

print("\nRound Robin Scheduling:\n")

quantum = 2
queue = processes.copy()
current_time = 0
gantt = []

remaining = {p["name"]: p["burst"] for p in processes}

while queue:
    p = queue.pop(0)
    
    if remaining[p["name"]] > 0:
        start = current_time
        run_time = min(quantum, remaining[p["name"]])
        finish = start + run_time
        
        print(f"{p['name']} runs from {start} to {finish}")
        
        gantt.append((p["name"], start, finish))
        
        current_time = finish
        remaining[p["name"]] -= run_time
        
        if remaining[p["name"]] > 0:
            queue.append(p)


fig, ax = plt.subplots()

for (name, start, finish) in gantt:
    ax.barh(0, finish - start, left=start)
    ax.text(start + (finish - start)/2, 0, name, ha='center', va='center', color='white')

ax.set_xlabel("Time")
ax.set_yticks([])
ax.set_title("Round Robin Gantt Chart")

plt.show()