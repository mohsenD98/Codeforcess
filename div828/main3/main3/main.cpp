#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >>t;
    while(t--){
        int n;
        char cur;
        string inS;
        cin >> n >> cur;
        cin >> inS;

        if (cur == 'g') {
            cout << 0 << endl;
            continue;
        }

        vector<int> possibles;
        vector<int> greens;
        for(int i=0; i < inS.size(); ++i){
            if(inS[i] == cur){
                possibles.push_back(i);
            }
            if(inS[i] == 'g'){
                greens.push_back(i);
            }
        }

        int maxSteps = 0;
        for(int p: possibles){

            int minsteps = 10000000;
            for(int g: greens){
                if (p < g){
                    if(minsteps > g-p){
                        minsteps = g-p;
                    }
                }
                if (p > g){
                    int x = (n-p-1) + g + 1;
                    if(minsteps > x){
                        minsteps = x;
                    }
                }
            }

            if(minsteps>maxSteps){
                maxSteps = minsteps;
            }

        }
        cout<<maxSteps << endl;

    }
    return 0;
}
