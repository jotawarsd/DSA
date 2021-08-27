#include <iostream> 
using namespace std;

class exponent
{
    public:
    int a,b;
    int k = 1;
    void exp();
}obj;

void exponent::exp()
{
    cout << "enter base: ";
    cin >> a;

    cout << "enter exponent: ";
    cin >> b;

    for(int i = 0; i < b; i++)
    {
        k = k*a;
    }
    printf("%d \n", k);
}

int main()
{
    obj.exp();
}