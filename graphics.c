#include<graphics.h>

int main()
{   
int gd=DETECT,gm;
initgraph(&gd,&gm,(char*)"");

circle(200,200,100);
line(200,500,45,485);
getch();
closegraph();
return 0;
}