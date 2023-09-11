#include <Stepper.h>

const int stepsPerRevolution = 1600;   // Change this according to your motor's specification
const int clkPin = 3;            // Stepper control pin 1 (CLK)
const int dirPin = 2;            // Stepper control pin 2 (DIR)
const int controlPin1 = 7;
const int controlPin2 = 9;

Stepper stepper(stepsPerRevolution, clkPin, dirPin);

void setup() {
  stepper.setSpeed(4000);    // Set the speed of the stepper motor (in steps per minute)
  Serial.begin(115200);  // Set the baud rate to match the value used in the Python script
  pinMode(controlPin1, INPUT_PULLUP);
  pinMode(controlPin2, INPUT_PULLUP);
}

void loop() {
  if (Serial.available()) {
    Serial.println("ping");
    // Read the command from the serial connection
    String command = Serial.readStringUntil('\n');
    long steps = command.toInt();
    
    volatile long i = 0;
    
    if((steps < 0) == 1) {
      steps = abs(steps);
      while(i < steps){
        digitalWrite(dirPin, HIGH);
        stepper.step(1);
        i = i + 1; 
      }
    } else if ((steps > 0) == 1) { 
      while(i < steps){
        digitalWrite(dirPin, LOW);
        stepper.step(1);
        i = i + 1; 
      }
    }
    Serial.println("ping"); 
  }

  
  
  volatile int sensorVal1 = digitalRead(controlPin1);
  volatile int sensorVal2 = digitalRead(controlPin2);  
  while (sensorVal1 == LOW) {
    digitalWrite(dirPin, LOW);
    stepper.step(1);
    sensorVal1 = digitalRead(controlPin1);
  } 
  while (sensorVal2 == LOW) {
    digitalWrite(dirPin, HIGH);
    stepper.step(1);
    sensorVal2 = digitalRead(controlPin2);
    }   
}
