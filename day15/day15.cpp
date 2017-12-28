#include <iostream>
using namespace std;

int main() {
  long long a = 703;
  long long b = 516;
  int total = 0;

  for (int i = 0; i < 5000000; ++i) {
    do {
      a = (a * 16807) % 2147483647;
    } while ((a % 4) !=0);

    do {
      b = (b * 48271) % 2147483647;
    } while (b % 8 != 0);
    if ((a & 0xFFFF) == (b & 0xFFFF)) {
      ++total;
    }

  }
  cout << total << endl;
}
