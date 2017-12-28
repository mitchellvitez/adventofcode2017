#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
  string l = "abcdefghijklmnop";
  for (int i = 0; i < 1000000000; ++i) {
    if (i % 1000 == 0) {
      cout << i << endl;
    }
    ifstream f;
    f.open("input.txt");
    char instr;
    while (true) {
      cin >> instr;
      if (instr == 's') {
        int num;
        cin >> num;

      }
      else if (instr == 'x') {
        int a, b;
        char slash;
        cin >> a >> slash >> b;
        swap(l[a], l[b]);
      }
      else if (instr == 'p') {
        char a, b;
        char slash;
        cin >> a >> slash >> b;
        swap(l[l.find(a)], l[l.find(b)]);
      }
      else {
        break;
      }
    }
  }
}

