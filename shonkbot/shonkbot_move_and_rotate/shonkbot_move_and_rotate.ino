/*++
 * Constants
++*/
// Number of steps for 1 complete rotation of the motor shaft
#define STEPS_PER_REV (4096.0/2.0)

// Maximum motor speed, 800 is a sensible limit on 5v motor supply, 300 is a sensible limit on 3v.        
#define MAX_SPEED 350 

// Maximum rate of speed change 1600 on 5v, 400 on 3v
#define MAX_ACCELERATION 400

// Define constant pi
#define PI 3.14159;

// Diameter of wheel in mm
#define WHEEL_DIAMETER 41.0 

// Distance from one wheel to the other in mm
#define WHEEL_SPACING 150.0


/*++
 * Includes
++*/
#include <AccelStepper.h>


/*++
 * Prototypes
++*/
void move_by_distance(float dist);
void rotate_by_angle(float angle);


/*++
 * Macros
++*/

// Macro used to make switch statement action list have cleaner syntax
#define action(n, f) case n: f; break


/*++
  Define a stepper and the pins it will use. Note middle two pins are
  swapped to work with 28BYJ-48, wire arduino pin D2 to driver
  board IN1, and so on
 
  using 28BYj-48 motors from http://www.ebay.co.uk/itm/131410728499
  these motore come in two different gear rations, 
  see http://42bots.com/tutorials/28byj-48-stepper-motor-with-uln2003-driver-and-arduino-uno/ 
  and http://forum.arduino.cc/index.php?topic=71964.15
++*/
AccelStepper leftStepper(AccelStepper::FULL4WIRE, 2,4,3,5); 
AccelStepper rightStepper(AccelStepper::FULL4WIRE, 6,8,7,9);


/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * Set up the stepper motors
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
void setup()
{  
  leftStepper.setMaxSpeed(MAX_SPEED);
  leftStepper.setAcceleration(MAX_ACCELERATION);
  rightStepper.setMaxSpeed(MAX_SPEED);
  rightStepper.setAcceleration(MAX_ACCELERATION);
}


/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * Main loop
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
void loop()
{
// Static variable for current action state
  static int action_id = 0;

// Run the next action if the steppers have nothing to do
  if (leftStepper.distanceToGo() == 0 && rightStepper.distanceToGo() == 0)
  {
  // List of actions to do, 'action' macro is used to simplify syntax.
    switch(action_id) {
      action(0, move_by_distance(50));
      action(1, rotate_by_angle(90));
    }
    
  // Progress to the next action
    action_id ++;
    
  // Return to first action on completion
    if(action_id > 1)
      action_id = 0;
  }

// Run the steppers
  leftStepper.run();
  rightStepper.run();
}


/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * Move the robot forward by some distance in millimeters
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
void move_by_distance(float dist)
{
// Calculate the circumference of the wheel, this is how far the
// bot will move along the ground in 1 motor rotation
  float wheel_circ = WHEEL_DIAMETER * PI;

// Calculate the number of steps to move by 1mm
  float steps_1mm = STEPS_PER_REV / wheel_circ;

// Calculate how many steps are required to move by the requested distance
  float mov_steps = steps_1mm * dist;

// Move the motors
  leftStepper.move(mov_steps);
  rightStepper.move(mov_steps);
}


/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * Rotate the robot on the spot by an angle in degrees
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
// Rotate on the spot by an angle in degrees
void rotate_by_angle(float angle)
{
// Calculate the circumference of the robots wheel base
  float base_circ = WHEEL_SPACING * PI;

// Calculate the circumference of the wheel, this is how far the
//  bot will move along the ground in 1 motor rotation
  float wheel_circ = WHEEL_DIAMETER * PI;

// How many times does the wheel have to rotate to traverse
// the circumference of the robots wheel base?
  float total_w_rots = base_circ / wheel_circ;

// Calculate the number of motor steps required to rotate the robot by 360 degrees,
// this is the number of steps in a single wheel revolution multiplied by the
// number of wheel rotations needed to rotate the robot 360 degrees.
  float steps_360 = total_w_rots * STEPS_PER_REV;

// Calculate the number of motor steps to rotate the robot by 1 degree
  float steps_per_degree = steps_360 / 360;

// Calculate the number of steps needed to rotate the robot by the desired angle
  float steps_angle = steps_per_degree * angle;

// Move the motors, note that one is inverted to reverse direction
  leftStepper.move(steps_angle);
  rightStepper.move(-steps_angle);
}
