class Proceso:
    def _init_(self, id, arrival_time, burst_time):
        self.id=id
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.completion_time=0
        self.turnaround_time=0
        self.waiting_time=0

def calcular_promedios(processes):
    n=len(processes)
    total_turnaround_time=0
    total_waiting_time=0
    current_time=0

    for process in processes:
        if current_time<process.arrival_time:
            current_time=process.arrival_time
        current_time+=process.burst_time
        process.completion_time=current_time
        process.turnaround_time=process.completion_time-process.arrival_time
        process.waiting_time=process.turnaround_time-process.burst_time
        total_turnaround_time+=process.turnaround_time
        total_waiting_time+=process.waiting_time

    average_turnaround_time=total_turnaround_time/n
    average_waiting_time=total_waiting_time/n

    return average_turnaround_time, average_waiting_time

if __name__=="__main_":
    processes = [
        Proceso(1, 4, 5),
        Proceso(2, 6, 4),
        Proceso(3, 0, 3),
        Proceso(4, 6, 2),
        Proceso(5, 5, 4)]
    
    processes.sort(key=lambda x: x.arrival_time)
    avg_turnaround_time, avg_waiting_time=calcular_promedios(processes)

    print(f"Average Turnaround Time: {avg_turnaround_time:.1f}")
    print(f"Average Waiting Time: {avg_waiting_time:.1f}")