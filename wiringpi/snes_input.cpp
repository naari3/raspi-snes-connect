#include <iostream>
#include <algorithm>
#include <wiringPi/wiringPi.h>
using namespace std;

const int P_S = 20
const int CLK = 21
const int _DAT = 22

int main() {
  if (wiringPiSetupGpio() < 0) {
    printf("GPIO ERROR\n");
    return 0;
  }

  pinMode(P_S, OUTPUT);
  pinMode(CLK, OUTPUT);
  pinMode(_DAT, INPUT);

  int stack[16];
  int prev_stack[16];
  cout << "B Y s S U D L R A X L R 1 2 3 4" << endl;
  while (true) {
    for (int i = 0; i < 16; i++) {
      if (i == 0) {
        digitalWrite(P_S, HIGH);
        digitalWrite(P_S, LOW);
      }
      digitalWrite(CLK, HIGH);
      digitalWrite(CLK, LOW);
      stack[i] = digitalRead(_DAT);
    }
    if (memcmp(stack, prev_stack, 16) != 0) {
      for (int j = 0; j < 16; j++) {
        cout << stack[j] << " ";
      }
      cout << "\r";
    }
    memcpy(prev_stack, stack, 16);
  }

  return 0;
}
