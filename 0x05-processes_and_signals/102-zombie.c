#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - ...
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - ...
 *
 * Return: Always 0
 */
int main(void)
{
	int pid;
	int z;

	while (z < 5)
	{
		pid = fork();
		if (pid != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
			return (0);
		z++;
	}
	infinite_while();
	return (0);
}
