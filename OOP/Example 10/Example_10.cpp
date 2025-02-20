#include <iostream>  // Include the input-output stream library
using namespace std; // Use the standard namespace to avoid writing std:: before cout and cin

int main()
{
    int i = 1; // Initialize the variable 'i' with the value 1

    // 'do-while' loop ensures the code runs at least once before checking the condition
    do
    {
        cout << "This is iteration " << i << endl; // Output the current iteration number
        i++;                                       // Increment 'i' by 1 in each iteration
    } while (i <= 5); // Loop continues while 'i' is less than or equal to 5

    return 0; // Return 0 to indicate successful execution
}
