#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() {

	pid_t pid, mypid, myppid;
	pid = getpid();

	printf("Before fork the process id is %d\n-------------\n", pid);
	pid = fork();

	if(pid < 0 ) {
	perror("fork() fail\n");
	return 1;
	}
	if(pid == 0){

	printf("The is the child process \n");
	mypid = getpid();
	myppid = getppid();
	printf("PID : %d and PPID: %d\n-------------------\n", mypid, myppid);
	}
	else {
		sleep(2);
		printf("This is parent process \n");
		mypid = getpid();
		myppid = getppid();
		printf("PID: %d and PPID: %d\n", mypid, myppid);
		printf("Newly created child PID is %d\n", pid);
	}
	return 0;
}


