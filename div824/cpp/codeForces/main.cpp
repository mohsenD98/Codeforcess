#include <iostream>

int main()
{
    int numberOfTestCases = 0;
    std::cin >> numberOfTestCases;

    for(int i=0; i< numberOfTestCases; ++i){
        int n;
        std::cin >> n;
        std::cout << ((n-3) / 3 ) - 1 << std::endl;
    }

    return 0;
}
