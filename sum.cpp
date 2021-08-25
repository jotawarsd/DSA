#include <iostream>
using namespace std;

class addition
{
    public:
    int a,b,sum;
    void add()
    {
        cout << "a: ";
        cin >> a;
        cout << "b: ";
        cin >> b;
        sum = a + b;
        cout << sum;
        printf("\n");
    }
}obj;

int main ()
{
    obj.add();
}