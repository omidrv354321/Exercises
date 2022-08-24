#include <stdio.h>
#include <cs50.h>
int main(void)
{
    //get the user name
    string name = get_string("What is your name?\n");
    //now say my name
    printf("hello, %s\n", name);
}