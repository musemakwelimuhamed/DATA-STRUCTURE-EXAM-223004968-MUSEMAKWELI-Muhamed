#include <iostream>  // Include the input-output stream library
using namespace std; // Use the standard namespace to avoid writing std:: before cout and cin

int main()
{
    int age = 25; // Declare and initialize the variable 'age' with the value 25

    // Check if the person is an adult (age between 18 and 59)
    if (age >= 18 && age < 60)
    {
        cout << "You are an adult." << endl; // Output message for adults
    }
    // Check if the person is a senior citizen (age 60 or above)
    else if (age >= 60)
    {
        cout << "You are a senior citizen." << endl; // Output message for senior citizens
    }
    // If the person is below 18, they are considered a minor
    else
    {
        cout << "You are a minor." << endl; // Output message for minors
    }

    return 0; // Return 0 to indicate successful execution
}
