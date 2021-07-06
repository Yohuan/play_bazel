#include <iostream>
#include <string>

#include "cpp/lib/greeting.h"

int main(int argc, char **argv)
{
  std::string who = "world";
  if (argc > 1)
  {
    who = argv[1];
  }

  std::cout << Greet(who) << std::endl;
  return 0;
}
