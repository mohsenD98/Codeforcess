#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >>t;
    while(t--){
        int n;
        string s;
        cin >> n;
        vector<int> a(n);

        for(int i=0; i<n; ++i){
            cin >> a[i];
        }

        cin >> s;

        bool flag = false;
        for(int i=0; i<n; ++i){

            flag = true;
            for(int j=i; j<n; ++j){
                if(a[j] == a[i] && s[i]!=s[j]){
                    flag = false;
                    break;
                }
            }

            if(!flag){
                break;
            }
        }
        if(flag){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }
    return 0;
}
