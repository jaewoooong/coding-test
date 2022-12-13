#include <stdio.h>

int arr[1000002] = { 0 };

int main()
{
	int a, b, i, k, s = 0, j = 0;

	scanf("%d %d", &a, &b);
	for (i = 1; i <= 1000; i++)
	{
		for (k = 1; k <= i; k++)
		{
			arr[j] = i;
			j++;
		}
	}
	for (i = a; i <= b; i++)
	{
		s += arr[i - 1];
	}
	printf("%d\n", s);
	return 0;
}