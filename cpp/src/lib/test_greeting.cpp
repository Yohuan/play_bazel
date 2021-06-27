#include "cpp/src/lib/greeting.h"

#include <gtest/gtest.h>

namespace
{
  TEST(Greeting, GetGreet)
  {
    EXPECT_EQ(get_greet("yohuan"), "Hello yohuan");
  }
}
