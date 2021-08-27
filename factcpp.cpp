#include <iostream>
using namespace std;

class factorial
{
    public:
    int a, k=1;
    void fact();
}obj;

void factorial::fact()
{
    cout << "number: ";
    cin >> a;

    for(int i = 0; i < a; i++)
    {
        k = k * (a - i);
    }
    
    cout << "factorial = " << k;
    printf("\n");
}

int main()
{
    obj.fact();
}