#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define nat long int
#define rat long double

int main(int argc, const char **argv)
{
	nat n0 = atoi(argv[1]);	
	rat sum0 = atoi(argv[2]);
	nat n1 = atoi(argv[3]);
	rat sum1 = sum0;

	nat i = n0;
	while (i != n1) {
		i += 1;
		sum1 += 1/(i*i);
		printf("%lf\n", sqrt(6*sum1));
	}

	return 0;
}
