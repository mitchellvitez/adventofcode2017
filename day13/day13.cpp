#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

unordered_map<int, int> d;

bool caught(int delay) {
  for (int x = 0; x < 91; ++x) {
    auto it = d.find(x);
    if (it != d.end()) {
      if ((x + delay - 1) % (d[x] * 2 - 2) == 0) {
        return true;
      }
    }
  }
  return false;
}

int main() {
  ifstream infile("input.txt");
  int depth, range;
  string garbage;
  while (infile >> depth >> garbage >> range) {
    d[depth] = range;
  }
  for (int delay = 0; delay < 10000000; ++delay) {
    /* if (delay % 10000 == 0) { */
      /* cout << delay << endl; */
    /* } */
    if (!caught(delay)) {
      cout << delay - 1 << endl;
      return 0;
    }
  }
}
