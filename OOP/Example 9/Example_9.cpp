#include <iostream>  // Include the input-output stream library
using namespace std; // Use the standard namespace to avoid writing std:: before cout and cin

int main()
{
    int i = 1; // Initialize the variable 'i' with the value 1

    // Loop that runs while 'i' is less than or equal to 5
    while (i <= 5)
    {
        cout << "This is iteration " << i << endl; // Output the current iteration number
        i++;                                       // Increment 'i' by 1 in each iteration to avoid an infinite loop
    }

    return 0; // Return 0 to indicate successful execution
}
