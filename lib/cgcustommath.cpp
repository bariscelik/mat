#include <iostream>
#include "cgcustommath.h"

Eigen::Array22f matrix(int a, int b)
{
    // initialize identity matrix
    Eigen::Array22f result;
    result << 1, 0,
         0, 1;
    result *= a;
    result += b;
    
    return result;
}