#include <iostream> // Including the input-output stream library for using cout

using namespace std; // Using the standard namespace to avoid writing std:: before cout and cin

int main() // Main function where execution begins
{
    int age = 18; // Declaring an integer variable 'age' and initializing it with the value 18

    // Checking if the age is greater than or equal to 18
    if (age >= 18)
    {                                        // If condition to check if the user is an adult
        cout << "You are an adult." << endl; // If true, print the message
    }

    return 0; // Returning 0 to indicate successful program execution
}
