#include <stdio.h>
#include <stdlib.h>

#define SQUARES             9
#define NUMBERS_IN_SQUARE   9
#define SQUARE              9
#define POSSIBLE            0x1FF

typedef struct square
{
    int number;
    int row;
    int column;

    unsigned short code;

} square_t;

int **create_puzzle(void);

void print_puzzle(int **puzzle);

square_t ***set_up_puzzle(int **puzzle);
