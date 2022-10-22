#include <iostream>
#include <vector>

using namespace std;

int gcd(int a, int b)
{
    if (a == 0)
       return b;
    if (b == 0)
       return a;

    if (a == b)
        return a;

    if (a > b)
        return gcd(a-b, b);
    return gcd(a, b-a);
}
int main()
{
    int numT;
    cin>>numT;

    for(int i=0; i<numT; ++i){

        int len;
        cin>> len;
        vector<int> arr;

        for(int j=0 ; j<len; ++j){
            int x;
            cin>>x;
            arr.push_back(x);
        }

        int indexSum = -1;

        for(int k=0; k<len; ++k){
            for(int l=0; l<len; ++l){
                int mgcd = gcd(arr[k], arr[l]);
                if(mgcd == 1){
                    if(k + l + 2 > indexSum){
                        indexSum = k + l + 2;
                    }
                }
            }
        }

        cout <<indexSum <<endl;


    }

    return 0;
    return 0;
}
