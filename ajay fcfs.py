def fcfs(processes):
    n=len(processes)
    waiting_time=0
    turnaround_time=processes[0][1]
    wt_list=[waiting_time]
    tat_list=[turnaround_time]
    for i in range(1,n):
        waiting_time += processes[i-1][1]
        turnaround_time +=processes[i][1]
        wt_list.append(waiting_time)
        tat_list.append(turnaround_time)
    avg_waiting_time=sum(wt_list)/n
    avg_turnaround_time=sum(tat_list)/n
    print("Process\tBurst time \t waiting time \t turnaround time")
    for i in range(n):
        print(f"{processes[i][0]}\t {processes[i][1]}\t\t {wt_list[i]}\t\t{tat_list[i]}")
    print(f"Average waiting time:{avg_waiting_time}")
    print(f"Average turnaround time:{avg_turnaround_time}")