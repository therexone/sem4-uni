// FCFS Scheduling
#include <stdio.h>

void main()
{
    int number_of_processes, processes[10], burst_time[10], wait_time[10], 
        turn_around_time[10], total_wt = 0, total_tat = 0, average_wt = 0, average_tat = 0;

    printf("\nEnter the number of Processes: ");
    scanf("%d", &number_of_processes);
    wait_time[0] = 0;
    printf("\nEnter Burst times for the processes-\n");
    for (int i = 0; i < number_of_processes; i++)
    {
        printf("Process[%d]: ", i + 1);
        scanf("%d", &burst_time[i]);
        processes[i] = i + 1;
    }

    for (int i = 0; i < number_of_processes; i++)
    {
        int pos = i;
        for (int j = i + 1; j < number_of_processes; j++)
        {
            if (burst_time[j] < burst_time[pos])
                pos = j;
        }

        int temp = burst_time[i];
        burst_time[i] = burst_time[pos];
        burst_time[pos] = temp;

        temp = processes[i];
        processes[i] = processes[pos];
        processes[pos] = temp;
    }

    for (int i = 1; i < number_of_processes; i++)
    {
        wait_time[i] = wait_time[i - 1] + burst_time[i - 1];
        total_wt += wait_time[i];
    }

    for(int i = 0; i < number_of_processes; i++)
    {
        turn_around_time[i] = burst_time[i] + wait_time[i];
        total_tat += turn_around_time[i];
    }

    printf("\nProcess Number\t Burst Time\t Waiting Time\t Turn Around Time\n");
    for(int i = 0; i < number_of_processes; i++)
    {
        printf("\n%d\t\t%d\t\t%d\t\t%d", i, burst_time[i], wait_time[i], turn_around_time[i]);
    }

    average_wt = total_wt / number_of_processes;
    average_tat = total_tat / number_of_processes;
    printf("\nAverge Waiting time: %d", average_wt);
    printf("\nAverage Turn Around Time: %d", average_tat);
}


// ------OUTPUT-------
/*
therexone@therexone-X556UQK:~/Desktop/workspace/sem4-uni/OSL$ ./"exp5-sjf" 

Enter the number of Processes: 5

Enter Burst times for the processes-
Process[1]: 2
Process[2]: 3
Process[3]: 4
Process[4]: 7
Process[5]: 9

Process Number   Burst Time      Waiting Time    Turn Around Time

0               2               0               2
1               3               2               5
2               4               5               9
3               7               9               16
4               9               16              25
Averge Waiting time: 6
Average Turn Around Time: 11
