#include<stdio.h>
#include<stdlib.h>
#include <graphics.h>

int main()
{
int gd = DETECT, gm;
//init graphics
initgraph(&gd, &gm,NULL);
//draw a line
/*
line() function description
parameter left to right
x1: 100
y1: 100
x2: 200
y2: 100
*/
line(100,100,200,100);
//will draw a horizontal line
line(10,10,200,10); //will draw another horizonatl line

delay(500000);
closegraph();
return 0;
}