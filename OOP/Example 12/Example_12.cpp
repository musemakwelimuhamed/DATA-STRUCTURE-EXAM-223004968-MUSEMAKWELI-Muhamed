#include <iostream>  // Include the input-output stream library
using namespace std; // Use the standard namespace to avoid writing std:: before cout and cin

// Function definition to greet a user by name
void greet(string name)
{
    cout << "Hello, " << name << "!" << endl; // Print a greeting message
}

int main()
{
    greet("Alice"); // Calling the function with a name

    return 0; // Return 0 to indicate successful execution
}
