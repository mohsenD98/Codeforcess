#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >>t;
    while(t--){
        int n, q;
        cin >> n >> q;
        vector<long long> a(n);

        long long sumEven = 0;
        int evenCount = 0;
        long long sumOdd = 0;
        int oddCount = 0;

        for(int i=0; i<n; ++i){
            cin >> a[i];

            if(a[i] % 2 == 0){
                sumEven += a[i];
                evenCount += 1;
            }
            else{
                sumOdd += a[i];
                oddCount += 1;
            }
        }

        for(int i=0; i<q; ++i){
            int type, xj;
            cin >> type >> xj;

            long long newAdd=0;
            if(type == 0){
                newAdd = (evenCount * xj);

            }else{
                newAdd = (oddCount * xj);
            }

            cout <<sumEven+sumOdd+newAdd << endl;

            if(xj %2 == 0 && type == 0){
                sumEven += newAdd;
            }
            if(xj %2 == 0 && type == 1){
                sumOdd += newAdd;
            }
            if(xj %2 == 1 && type == 0){
                oddCount = n;
                sumOdd = sumEven+sumOdd+newAdd;

                sumEven = 0;
                evenCount = 0;
            }
            if(xj %2 == 1 && type == 1){
                evenCount = n;
                sumEven = sumEven+sumOdd+newAdd;

                sumOdd = 0;
                oddCount = 0;
            }
        }
    }
    return 0;
}
