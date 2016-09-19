#include <stdint.h>
#include <inttypes.h>

// Chapter 5 of "Cracking the Coding Interview"

// 5.1
uint32_t insert_into(uint32_t M, uint32_t N, uint8_t i, uint8_t j)
{
    uint32_t mask = ~1; // All ones.
    mask >>= 32-(j-i+1); // Kill all but (j-i+1) ones.
    mask <<= i; // Moves the block of ones to the correct position.
    mask = ~mask; // Block of ones is now block of zeros.
    N &= mask; // Leaves a block of zeros in N.
    return N | (M << i); // Inserts M into the block of zeros.
}

// 5.2. Prints the binary representation of a decimal string.
void print_binary(char *string)
{
    if(string == NULL)
        return;

    char sign = 1;
    if(string[0] == '-') // Result is negative.
        sign = -1;

    // Loop through the characters.
    for(int i=0; string[i] != NULL; i++)
    {

    }

}