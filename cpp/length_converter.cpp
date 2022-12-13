#include <iostream>
#include <iomanip>

using namespace std;

struct unit
{
    string name_full;
    string name_short;
    double value;
};
unit units[] = {
    {"Meters", "m", 1},
    {"Millimeters", "mm", 0.001},
    {"Centimeters", "cm", 0.01},
    {"Kilometers", "km", 1000.0},
    {"Yards", "yd", 0.9144},
    {"Inches", "in", 0.0254},
    {"Feet", "ft", 0.3048},
    {"Miles", "mi", 1609.344}};

template <class T>
void print(T x, bool useEndLine = true)
{
    if (useEndLine)
        cout << setprecision(3) << fixed << x << endl;
    else
        cout << setprecision(3) << fixed << x;
}

void clear()
{
    print("\x1B[2J\x1B[H", false); // Clear screen
    print("\e[3J", false);         // Clear scrollback
}

string input(string prompt = "")
{
    // Simple arrow-prompt input system - returns a string of whatever user entered (empty strings are possible)
    string in;
    if (prompt.empty())
        print("\n> ", false);
    else
        print("\n" + prompt + "\n> ", false);
    getline(cin, in);
    return in;
}

int main()
{
    // Init
    string usr;
    unsigned char selected;
    double number;

    // Program loop
    while (true)
    {
        // Select unit
        while (true)
        {
            clear();
            print("Length Converter - Select a unit and put in a value to get the converted values for all the other units.\n");
            for (unsigned char i = 0; i < 4; i++)
            {
                // Column-by-column printing of the available units (column size is 2)
                string s1 = to_string(i) + "). " + units[i].name_full + "\t(" + units[i].name_short + ")" + "\t\t";
                string s2 = to_string(i + 4) + "). " + units[i + 4].name_full + "\t(" + units[i + 4].name_short + ")";
                print(s1, false);
                print(s2);
            }
            usr = input("First, type in the matching number of the unit you wish to convert from, then press 'Enter'...");
            // Validate number entered by user
            try
            {
                if (usr.length() > 1)
                    throw selected;
                selected = usr[0] - 48;
                if (selected >= 0 && selected <= 7)
                    break;
                else
                    throw selected;
            }
            catch (unsigned char e)
            {
                clear();
                print("Invalid entry. Entry must be a whole number between 0 and 7.");
                usr = input("(Press 'Enter' to try again)");
            }
        }
        // Length Value
        while (true)
        {
            clear();
            print("Next, type the length in " + units[selected].name_full + ", then press 'Enter'...");
            usr = input();
            // Validate string as positive number
            bool valid = true;
            if (usr.length() > 0)
            {
                unsigned char decimals = 0;
                if (usr[0] == '.' || usr[usr.length() - 1] == '.')
                    valid = false;
                for (unsigned char i = 0; i < usr.length(); i++)
                {
                    if (usr[i] == '.')
                        decimals++;
                    if (decimals > 1)
                        valid = false;
                    if (isdigit(usr[i]) || usr[i] == '.')
                        continue;
                    valid = false;
                }
            }
            else
                valid = false;
            // Valid
            if (valid)
            {
                number = stod(usr);
                break;
            }
            // Not valid
            clear();
            print("Invalid entry. Please put in a number to calculate the other units.");
            usr = input("(Press 'Enter' to try again)");
        }
        // Calculate lengths
        clear();
        print(number, false);
        print(" " + units[selected].name_short + " is equal to...\n");
        for (int i = 0; i < 8; i++)
        {
            if (i == selected)
                continue;
            print("- ", false);
            print(number * (units[selected].value / units[i].value), false);
            print(" " + units[i].name_short);
        }
        // Does user want to try again?
        string again = input("Would you like to select a different unit? (Y/N)");
        if (again == "Y" || again == "y")
            continue;
        break;
    }
    return 0;
}