#include <iostream>
using namespace std;

class comparison
{
    public:
    int a,b,c;
    void cmp()
    {
        cin >> a>> b>> c;
        if(a > b && a > c)
            printf("%d is greatest", a);
        else if(b > c)
            printf("%d is greatest", b);
        else 
            printf("%d is greatest", c);
    }     
}obj;

int main()
{
    obj.cmp();
}