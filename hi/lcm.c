#include <stdio.h>

int main()
{
    int a;
    scanf("Entre the first no%d", &a);
    int b;
    scanf("Entre the second n%d", &b);

    int max = b;
    int min = a;

    if (a >= b)
    {
        max = a;
        min = b;
    }

    int ans;
    for (int i = max; i <= a*b; i++)
    {
        if(i%min ==0 && i%max ==0)
        {
            ans = i;
            break;
        }
    }
    printf("%d",ans);

    return 0;

}