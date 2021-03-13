#define NUM long
#define NODE_T NUM
#include "/home/syed/Programming/c/linked-list/node.h"

#include <stdbool.h>

#define DEFAULT_MAX 1000

bool is_factor(NUM big, NUM small)
{
	NUM mod = big % small;
	if (mod == 0)
		return true;
	else
		return false;
}

bool is_prime(struct node *primes, NUM n)
{
	for (struct node *p = primes; p != NULL; p = p->next) {
		if (is_factor(n, p->val)) {
			return false;
		}
	}
	return true;
}

int main(int argc, const char **argv)
{
    int max;
    if (argc >= 2)
        max = atoi(argv[1]);
    else
        max = DEFAULT_MAX;
    printf("MAX: %d\n", max);

    struct node *primes = list_new(2);

    NUM p = 3;
    int i = 1;
	while (i < max) {
	    if (is_prime(primes, p)) {
		list_push(primes, p);
		i++;
	    }
	    p += 2;
	}

    for (struct node *ptr = primes; ptr != NULL; ptr = ptr->next)
        printf("%d, ", ptr->val);

    putchar('\n');

    return 0;
}
