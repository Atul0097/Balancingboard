#include <SoftwareSerial.h>

SoftwareSerial hc06(10,11);

void setup(){
  Serial.begin(115200);
  Serial.println("ENTER AT Commands:");
  hc06.begin(115200);
  }

void loop(){
  // Keep reading from HC-05 and send to Arduino Serial Monitor
  if (hc06.available()){
  Serial.write(hc06.read());
  }
  // Keep reading from Arduino Serial Monitor and send to  HC-05 
  if (Serial.available()){
  hc06.write(Serial.read());
  }  
}

