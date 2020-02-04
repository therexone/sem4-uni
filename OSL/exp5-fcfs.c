// FCFS Scheduling 
#include <stdio.h>

void main() 
{
    int number_of_processes, burst_time[10], wait_time[10],
    turn_around_time[10], total_wt = 0, total_tat = 0, average_wt = 0, average_tat = 0;
    
    printf("\nEnter the number of Processes: ");
    scanf("%d", &number_of_processes);
    wait_time[0] = 0;
    printf("\nEnter Burst times for the processes-\n");
    for(int i = 0; i < number_of_processes; i++)
    {
        printf("Process[%d]: ", i+1);
        scanf("%d", &burst_time[i]);
    }
    
    for(int i = 1; i < number_of_processes; i++)
    {
        wait_time[i] = wait_time[i-1] + burst_time[i-1];
        total_wt += wait_time[i];
    }
    for(int i = 0; i < number_of_processes; i++)
    {
        turn_around_time[i] = burst_time[i] + wait_time[i];
        total_tat += turn_around_time[i];
    }

    average_wt = total_wt/number_of_processes;
    average_tat = total_tat/number_of_processes;
    printf("\nProcess Number\t Burst Time\t Waiting Time\t Turn Around Time\n");
    for(int i = 0; i < number_of_processes; i++)
    {
        printf("\n%d\t\t%d\t\t%d\t\t%d", i, burst_time[i], wait_time[i], turn_around_time[i]);
    }
    
    printf("\nAverge Waiting time: %d", average_wt);
    printf("\nAverage Turn Around Time: %d", average_tat );


}

// --------OUTPUT-------
// therexone@therexone-X556UQK:~/Desktop/workspace/sem4-uni/OSL$ ./"exp5-sjf" 

// Enter the number of Processes: 5

// Enter Burst times for the processes-
// Process[1]: 4
// Process[2]: 5
// Process[3]: 6
// Process[4]: 3
// Process[5]: 5

// Process Number   Burst Time      Waiting Time    Turn Around Time

// 0               3               0               3
// 1               4               3               7
// 2               5               7               12
// 3               5               12              17
// 4               6               17              23
// Averge Waiting time: 7
// Average Turn Around Time: 12