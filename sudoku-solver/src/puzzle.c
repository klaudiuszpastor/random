#include "sudoku.h"

square_t ***set_up_puzzle(int **puzzle)
{
    square_t ***sudoku;
    int i,j;

    sudoku = (square_t***) malloc((sizeof(square_t) * SQUARES));

    for (i = 0; i < 9; i++)
    {
        sudoku[i] = (square_t**) malloc((sizeof(square_t*) * SQUARES));

        for (j = 0; j < 9; j++)
        {
            sudoku[i][j] = (square_t*) malloc(sizeof(square_t));

            sudoku[i][j] -> number = puzzle[i][j];
            sudoku[i][j] -> row    = i;
            sudoku[i][j] -> column = j;

            if (sudoku[i][j] -> number != 0)
            {
                sudoku[i][j] -> code = 0x0;
            }
            else
            {
                sudoku[i][j] -> code = POSSIBLE;
            }
         }
    }
    //TODO check

    return sudoku;
}

int **create_puzzle()
{
    int **puzzle;
    int i,j;

    int array[SQUARE][NUMBERS_IN_SQUARE] =
    {
        {0, 1, 9, 0, 0, 2, 0, 0, 0},
        {4, 7, 0, 6, 9, 0, 0, 0, 1},
        {0, 0, 0, 4, 0, 0, 9, 0, 0},
        {8, 9, 4, 5, 0, 7, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 2, 0, 1, 9, 5},
        {0, 5, 0, 0, 0, 0, 6, 0, 0},
        {0, 0, 0, 2, 8, 0, 7, 7, 9},
        {0, 0, 0, 1, 0, 0, 8, 6, 0}
    };

    puzzle = (int**) malloc(sizeof(int*) * SQUARES);

    if (!puzzle)
    {
      fprintf(stderr, "Memory allocation for puzzle failed\n");
      exit(1);
    }

    for (i = 0; i < 9; i++)
    {
        puzzle[i] = (int*)malloc(sizeof(int)*9);

        if (!puzzle[i]) 
        {
            fprintf(stderr, "Memory allocation failed for puzzle[%d]\n", i);
            exit(1);
        }

        for (j = 0; j <9; j++) 
        {
            puzzle[i][j] = array[i][j];
        }
    }

    return puzzle;
}

void print_puzzle(int **puzzle)
{
    int i, j;

    printf("-------------------------------\n");

    for (i = 0; i < 9; i++)
    {
        printf("|");
        // Print each row
        for (j = 0; j < 9; j++)
        {
            printf(" %d ", puzzle[i][j]);

            if ((j + 1) % 3 == 0) 
            {
                printf("|");
            }
        }
        printf("\n");
        if ((i + 1) % 3 ==0)
        {
            printf("-------------------------------\n");
        }
    }
}
