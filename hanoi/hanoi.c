#include <stdio.h>
#include <stdlib.h>

void move(char, char);
void hanoi(int, char, char, char);

int main(int argc, const char **argv)
{
    if (argc < 2) {
        return 1;
    } else {
        hanoi(atoi(argv[1]), 'A', 'C', 'B');
        return 0;
    }
}

void move(char from, char to)
{
   printf("Move a disc from %c to %c.\n", from, to);
} 


void hanoi(int n, char from, char to, char via)
{
    if (n == 0) {
        return;
    } else {
        hanoi(n - 1, from, via, to);
        move(from, to);
        hanoi(n - 1, via, to, from);
    }
}
