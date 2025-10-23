#include "sudoku.h"

int main() 
{
    int **puzzle = create_puzzle();
    //square_t ***sudoku = set_up_puzzle(puzzle);

    print_puzzle(puzzle);

    free(puzzle);
    return 0;

}
