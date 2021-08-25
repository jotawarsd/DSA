#include <iostream>
using namespace std;

class addition
{
    public:
    int a,b,sum;
    void add()
    {
        cin >> a>> b;
        sum = a + b;
        cout << sum;
        printf("\n");
    }
}obj;

int main ()
{
    obj.add();
}