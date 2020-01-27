#include <stdbool.h>
#include <math.h>

bool is_prime(int num)
{
  for(int i = 2; i <= sqrt(num); i++)
    if (!(num % i))
      return false;
  return num >= 2;
}
