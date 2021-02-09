#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Entry point
 *
 * Return: Print or 0
 */
int main(void)
{
	pid_t ch_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		ch_pid = fork();
		if (ch_pid > 0)
			printf("Zombie process created, PID: %i\n", ch_pid);
		else
			return (0);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - infinite while
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
