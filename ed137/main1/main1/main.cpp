#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >>t;
    while(t--){
        int n;
        cin >> n;

        for(int i=0; i<n; ++i){
            int x;
            cin >> x;
        }
        n = 10 - n;
        int r = (n * (n-1)) / 2 * 6;
        cout << r<<endl;
    }
    return 0;
}
