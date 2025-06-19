Attendance Report Generator - C++ Project

Overview

This C++ project is designed to simulate an Attendance Report Generator system. It demonstrates:

*Dynamic memory management
*Inheritance and polymorphism using abstract classes
*Pointer arithmetic for analyzing trends
*User interactivity through a menu-based interface

Core Functionalities

1. Add Attendance Record: Users input a student ID, date, and presence status.
2. Remove Attendance Record: Users can delete a specific attendance entry.
3. Generate Reports:

   *DailyReport: Lists all student attendance entries with their dates.
   *TrendReport: Calculates and displays the number of present and absent records.

Code Explanation (Line by Line)

1. Include Directives and Namespace


#include <iostream>
#include <cstring>
#include <iomanip>
using namespace std;


* Includes necessary libraries: input/output, string manipulation, and formatting.
* using namespace std; simplifies use of standard objects like cout, cin, etc.

2. Date Struct


struct Date {
    int day, month, year;
};


Defines a Date structure to hold day, month, and year.

3. AttendanceRecord Struct


struct AttendanceRecord {
    char studentID[10];
    Date* date;
    bool present;
};


*Stores each attendance record.
*Uses char[] for student ID and a pointer to a dynamically allocated Date.

4. Abstract Base Class


class ReportInterface {
public:
    virtual void generate(const AttendanceRecord* recs, int n) = 0;
    virtual ~ReportInterface() {}
};


*Defines an interface for report generation with a pure virtual method.
*Ensures polymorphic behavior for derived classes.

5. DailyReport Class


class DailyReport : public ReportInterface {
public:
    void generate(const AttendanceRecord* recs, int n) override { ... }
};


*Inherits from ReportInterface.
*Loops through records and prints each student's data.

6. TrendReport Class


class TrendReport : public ReportInterface {
public:
    void generate(const AttendanceRecord* recs, int n) override { ... }
};


*Also inherits from ReportInterface.
*Uses pointer arithmetic to count how many students were present vs. absent.

7. AttendanceManager Class

Handles:

*Dynamic allocation and resizing of the record array
*Adding and removing records
*Report generation

Constructor & Destructor


AttendanceManager() : recs(nullptr), count(0) {}
~AttendanceManager() { ... }


*Initializes empty record array.
*Destructor releases allocated memory.

addAttendance Method


void addAttendance(const AttendanceRecord& newRec) { ... }


*Dynamically resizes the array.
*Copies old data and appends new record.

removeAttendance Method


void removeAttendance(int index) { ... }


*Deletes a record by index and resizes the array.

generateReports Method


void generateReports(ReportInterface reports, int numReports) { ... }


* Loops through each report and calls its generate() method.

8.Main Function (User Interface)


int main() { ... }


*Menu with options:

  *Add Attendance
  *Remove Attendance
  *Generate Reports
  *Exit
*Uses a loop to continuously prompt user until exit.
*Inputs for student ID, date, and presence collected via cin.
*Calls appropriate methods from AttendanceManager.

Summary

This project is ideal for understanding how:

*Dynamic arrays are handled in C++
*Inheritance allows for flexible and extendable report systems
*Polymorphism enables runtime decision of report behavior
*Real-world applications (like student attendance) can be modeled programmatically

Optional Enhancements

*Add file input/output
*Sort records by date or ID
*GUI using a C++ graphics library or Qt
*More report types (e.g., monthly, student-wise trends)
