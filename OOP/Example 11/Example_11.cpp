#include <iostream>  // Include the input-output stream library
using namespace std; // Use the standard namespace to avoid writing std:: before cout and cin

// Function definition to add two integers
int add(int a, int b)
{
    return a + b; // Return the sum of 'a' and 'b'
}

int main()
{
    int sum = add(5, 10);                  // Calling the 'add' function with arguments 5 and 10
    cout << "The sum is: " << sum << endl; // Output the result

    return 0; // Return 0 to indicate successful execution
}
