#define num unsigned long int
#define NODE_T num
#include "/home/syed/Programming/c/linked-list/node.h"
#include <stdbool.h>

bool is_factor(num big, num small)
{
	num mod = big % small;
	if (mod == 0)
		return true;
	else
		return false;
}

bool is_prime(struct node *primes, num n)
{
	for (struct node *p = primes; p != NULL; p = p->next) {
		if (is_factor(n, p->val)) {
			return false;
		}
	}
	return true;
}

int main(void)
{
	struct node *primes = make_node(2);
	int i = 3;
	while (true) {
		bool prime = is_prime(primes, i);
		if (prime) {
			push(primes, i);
			printf("%d, ", i);
		}
		i += 2;
	}
	return 0;
}
