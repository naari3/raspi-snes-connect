#include <iostream>
#include <algorithm>
#include <cstring>
#include <wiringPi.h>

using namespace std;

const int P_S = 20;
const int CLK = 21;
const int _DAT = 22;

const int sleep_time = 0;

int main() {
  int r = 0;
  if (wiringPiSetupGpio() < 0) {
    cout << "GPIO ERROR" << endl;
    return 0;
  }

  pinMode(P_S, OUTPUT);
  pinMode(CLK, OUTPUT);
  pinMode(_DAT, INPUT);

  int stack[16];
  int prev_stack[16];

  cout << "B Y s S u d l r A X L R 1 2 3 4" << endl;
  while (true) {
    for (int i = 0; i < 16; i++) {
      digitalWrite(CLK, HIGH);
      delayMicroseconds(sleep_time);
      digitalWrite(CLK, LOW);
      delayMicroseconds(sleep_time);
      if (i == 0) {
        digitalWrite(P_S, HIGH);
        delayMicroseconds(sleep_time);
        digitalWrite(P_S, LOW);
        delayMicroseconds(sleep_time);
      }
      stack[i] = digitalRead(_DAT);
    }
    // if (memcmp(stack, prev_stack, sizeof(prev_stack)) != 0) {
      for (int j = 0; j < 16; j++) {
        cout << (stack[j] == 0 ? "P" : " ") << " ";
      }
      cout << "\r";
    // }
    memcpy(prev_stack, stack, sizeof(stack));
  }

  return 0;
}
