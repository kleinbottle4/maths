/* What is the nth triangle number?
 * See also Programming/lisp/triangle-numbers.lisp,
 * Programming/8085/triangle_numbers.asm and
 * Programming/python/triangle_numbers.py*/

#include <stdio.h>

int triangle(int n)
{
	int a;
	for(a = 0; n > 0; n--) {
		a += n;
	}
	return a;
}

int main(void)
{
	printf("%d\n", triangle(255));
	return 0;
}
