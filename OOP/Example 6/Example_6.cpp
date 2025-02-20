#include <iostream> // Including the input-output stream library for using cout

using namespace std; // Using the standard namespace to avoid writing std:: before cout and cin

int main() // Main function where execution begins
{
    int age = 16; // Declaring an integer variable 'age' and initializing it with the value 16

    // Checking if the age is greater than or equal to 18
    if (age >= 18) // If condition to check if the user is an adult
    {
        cout << "You are an adult." << endl; // If true, print the message
    }
    else // If the condition is false (age < 18)
    {
        cout << "You are a minor." << endl; // Print the message for minors
    }

    return 0; // Returning 0 to indicate successful program execution
}
