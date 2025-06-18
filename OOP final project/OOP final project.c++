#include <iostream>
#include <cstring>
#include <iomanip>

using namespace std;

// Simple Date structure
struct Date {
    int day, month, year;
};

// Attendance Record structure
struct AttendanceRecord {
    char studentID[10];
    Date* date;
    bool present;
};

// Abstract Interface for Reports
class ReportInterface {
public:
    virtual void generate(const AttendanceRecord* recs, int n) = 0;
    virtual ~ReportInterface() {}
};

// Daily Report
class DailyReport : public ReportInterface {
public:
    void generate(const AttendanceRecord* recs, int n) override {
        cout << "\n--- Daily Attendance Report ---\n";
        for (int i = 0; i < n; ++i) {
            cout << "Student ID: " << recs[i].studentID
                 << " | Date: " << recs[i].date->day << "/" << recs[i].date->month << "/" << recs[i].date->year
                 << " | Present: " << (recs[i].present ? "Yes" : "No") << endl;
        }
    }
};

// Trend Report
class TrendReport : public ReportInterface {
public:
    void generate(const AttendanceRecord* recs, int n) override {
        cout << "\n--- Attendance Trend Report ---\n";
        int presentCount = 0;
        for (const AttendanceRecord* ptr = recs; ptr < recs + n; ++ptr) {
            if (ptr->present) ++presentCount;
        }
        cout << "Total Records: " << n << "\n";
        cout << "Present: " << presentCount << ", Absent: " << (n - presentCount) << endl;
    }
};

// Dynamic array manager
class AttendanceManager {
private:
    AttendanceRecord* recs;
    int count;

public:
    AttendanceManager() : recs(nullptr), count(0) {}

    ~AttendanceManager() {
        for (int i = 0; i < count; ++i) {
            delete recs[i].date;
        }
        delete[] recs;
    }

    void addAttendance(const AttendanceRecord& newRec) {
        AttendanceRecord* temp = new AttendanceRecord[count + 1];
        for (int i = 0; i < count; ++i) {
            temp[i] = recs[i];
        }
        temp[count] = newRec;
        recs = temp;
        count++;
    }

    void removeAttendance(int index) {
        if (index < 0 || index >= count) return;
        delete recs[index].date;
        AttendanceRecord* temp = new AttendanceRecord[count - 1];
        for (int i = 0, j = 0; i < count; ++i) {
            if (i != index) {
                temp[j++] = recs[i];
            }
        }
        recs = temp;
        count--;
    }

    void generateReports(ReportInterface** reports, int numReports) {
        for (int i = 0; i < numReports; ++i) {
            reports[i]->generate(recs, count);
        }
    }

    int getCount() const { return count; }
    AttendanceRecord* getRecords() const { return recs; }
};

// User Prompt and Main Function
int main() {
    AttendanceManager manager;
    int choice;

    do {
        cout << "\n--- Attendance Management ---\n";
        cout << "1. Add Attendance\n2. Remove Attendance\n3. Generate Reports\n4. Exit\nChoose an option: ";
        cin >> choice;

        if (choice == 1) {
            AttendanceRecord newRec;
            newRec.date = new Date;
            cout << "Enter student ID: ";
            cin >> newRec.studentID;
            cout << "Enter date (DD MM YYYY): ";
            cin >> newRec.date->day >> newRec.date->month >> newRec.date->year;
            cout << "Is student present? (1 = Yes, 0 = No): ";
            cin >> newRec.present;
            manager.addAttendance(newRec);
        } else if (choice == 2) {
            int index;
            cout << "Enter index to remove (0 to " << manager.getCount() - 1 << "): ";
            cin >> index;
            manager.removeAttendance(index);
        } else if (choice == 3) {
            ReportInterface* reports[2];
            reports[0] = new DailyReport();
            reports[1] = new TrendReport();

            manager.generateReports(reports, 2);

            delete reports[0];
            delete reports[1];
        }

    } while (choice != 4);

    return 0;
}
