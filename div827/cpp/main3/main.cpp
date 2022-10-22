#include <iostream>
#include <vector>
using namespace std;

int countString(string s, char x){
    int r = 0;
    for (char ss : s)
    {
        if(ss == x) r++;
    }
    return r;
}
int countString(vector<char> s, char x){
    int r = 0;
    for (char ss : s)
    {
        if(ss == x) r++;
    }
    return r;
}

int main()
{
    int numT;
    cin>>numT;

    for(int i=0; i<numT; ++i){
        vector<string> rows;
        for(int j=0; j<8; ++j){
            string row = "";
            cin >> row;
            rows.push_back(row);
        }

        bool RFound = false;
        for(string row: rows){
            if (countString(row, 'R') == 8){
                RFound = true;
                cout << "R" << endl;
                break;
            }
        }
        if(!RFound){
            cout << "B" << endl;
        }

    }

    return 0;
}
