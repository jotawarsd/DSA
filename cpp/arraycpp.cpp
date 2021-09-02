#include <iostream>
using namespace std;

class summation
{
    public:
    int A[50], dim,i,sum;
    void add();
}obj;

void summation::add()
{
    cout << "enter dimension of array: ";
    cin >> dim;
    
    for(i = 0; i < dim; i++)
    {
        cout << "element: ";
        cin >> A[i];
        sum += A[i];
    }
    cout << sum << "\n";

}

int main()
{
    obj.add();
}