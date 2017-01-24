#include <AccelStepper.h>

// Number of steps for 1 complete rotation of the motor shaft
#define STEPS_PER_REV (4096.0/2.0)

// Maximum motor speed, 800 is a sensible limit on 5v motor supply, 300 is a sensible limit on 3v.        
#define MAX_SPEED 350 

// Maximum rate of speed change 1600 on 5v, 400 on 3v
#define MAX_ACCELERATION 400


/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  Define a stepper and the pins it will use. Note middle two pins are
  swapped to work with 28BYJ-48, wire arduino pin D2 to driver
  board IN1, and so on
 
  using 28BYj-48 motors from http://www.ebay.co.uk/itm/131410728499
  these motore come in two different gear rations, 
  see http://42bots.com/tutorials/28byj-48-stepper-motor-with-uln2003-driver-and-arduino-uno/ 
  and http://forum.arduino.cc/index.php?topic=71964.15
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
AccelStepper leftStepper(AccelStepper::FULL4WIRE, 2,4,3,5); 
AccelStepper rightStepper(AccelStepper::FULL4WIRE, 6,8,7,9);

/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
void setup()
{  
  leftStepper.setMaxSpeed(MAX_SPEED);
  leftStepper.setAcceleration(MAX_ACCELERATION);
  rightStepper.setMaxSpeed(MAX_SPEED);
  rightStepper.setAcceleration(MAX_ACCELERATION);

// Run both motors 1 full rotation
  leftStepper.move(STEPS_PER_REV);
  rightStepper.move(STEPS_PER_REV);
}

/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
void loop()
{
   leftStepper.run();
   rightStepper.run();
}
