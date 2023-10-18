def sjf(processes, n):
    # Sort processes based on their burst time
    processes.sort(key=lambda x: x[1])

    # Initialize waiting time and turnaround time arrays
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time and turnaround time
    waiting_time[0] = 0
    turnaround_time[0] = processes[0][1]

    for i in range(1, n):
        waiting_time[i] = turnaround_time[i - 1]
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    # Calculate the average waiting time and average turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Display the scheduling results
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)

# Input the number of processes
n = int(input("Enter the number of processes: "))

processes = []
for i in range(n):
    burst_time = int(input(f"Enter the burst time for process P{i+1}: "))
    processes.append((i, burst_time))

sjf(processes, n)
