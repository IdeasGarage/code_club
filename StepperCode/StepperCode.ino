/* Defines the vales passed to the function vStepMotor()
   to specify which direction you would like the motor to
   turn in. */

#define FORWARD true
#define REVERSE false

/* Defines the digital IO pins used to control each of
   the stepper motors coils. */

#define MOTOR_COIL_1_DIO 6
#define MOTOR_COIL_2_DIO 7
#define MOTOR_COIL_3_DIO 8
#define MOTOR_COIL_4_DIO 9
#define MOTOR2_COIL_1_DIO 2
#define MOTOR2_COIL_2_DIO 3
#define MOTOR2_COIL_3_DIO 4
#define MOTOR2_COIL_4_DIO 5

/* The number of steps for 1 revolution of this stepper
   motor is 360 degrees devided by the motor step angle
   of 5.625 multiplied by the gear ratio 1/64 multiplied
   by the number of coils 4 devided by two.
   Therefore: 360 / (5.625 * (1 / 64)) = 512 */

#define STEPSPER1REV 512
#define STEPSPER1REV2 512


/* Set the 4 DIO pins used to drive the stepper motor to outputs */
void setup()
{
  pinMode(MOTOR_COIL_1_DIO, OUTPUT);
  pinMode(MOTOR_COIL_2_DIO, OUTPUT);
  pinMode(MOTOR_COIL_3_DIO, OUTPUT);
  pinMode(MOTOR_COIL_4_DIO, OUTPUT);
  pinMode(MOTOR2_COIL_1_DIO, OUTPUT);
  pinMode(MOTOR2_COIL_2_DIO, OUTPUT);
  pinMode(MOTOR2_COIL_3_DIO, OUTPUT);
  pinMode(MOTOR2_COIL_4_DIO, OUTPUT);
}

/* MAIN PROGRAM */
void loop()
{
  /* Used for counting the number of steps the motor has made */
  word u16StepCounter;
  word u16StepCounter2;

  /* Rotate the stepper motor one full forward revolution */
  int Action1 = 360 / (5.625 * (1 / 64));
  for (u16StepCounter = 0; u16StepCounter < Action1; u16StepCounter++) {
    vStepMotor2(FORWARD, 3);
  }
  int Action2 = 360 / (5.625 * (1 / 64));
  for(u16StepCounter = 0; u16StepCounter < Action2; u16StepCounter++){
    vStepMotor(REVERSE, 3);
  }
  int Action3 = 360 / (5.625 * (1 / 64));
  for (u16StepCounter2= 0; u16StepCounter2< Action3; u16StepCounter2++) {
    vStepMotor(FORWARD, 3);
  }
  int Action4 = 360 / (5.625 * (1 / 64));
  for(u16StepCounter = 0; u16StepCounter < Action4; u16StepCounter++){
    vStepMotor2(REVERSE, 3);
  }
}

void vStepMotor(boolean bDirection, word u16StepDelay)
{
  /* Holds which DIO pin is currently associated with which motor coil */
  byte bMotorCoil_1;
  byte bMotorCoil_2;
  byte bMotorCoil_3;
  byte bMotorCoil_4;

  /* Set the order of the DIO pins depending on the direction the
     motor is requires to turn in. */
  if (bDirection == true)
  {
    bMotorCoil_1 = MOTOR_COIL_1_DIO;
    bMotorCoil_2 = MOTOR_COIL_2_DIO;
    bMotorCoil_3 = MOTOR_COIL_3_DIO;
    bMotorCoil_4 = MOTOR_COIL_4_DIO;
  }else
  {
    bMotorCoil_1 = MOTOR_COIL_4_DIO;
    bMotorCoil_2 = MOTOR_COIL_3_DIO;
    bMotorCoil_3 = MOTOR_COIL_2_DIO;
    bMotorCoil_4 = MOTOR_COIL_1_DIO;
  }


  /* Pulse each of the stepper motors coils in a sequential order */
  digitalWrite(bMotorCoil_1, HIGH);
  digitalWrite(bMotorCoil_2, LOW);
  digitalWrite(bMotorCoil_3, LOW);
  digitalWrite(bMotorCoil_4, LOW);

  delay(u16StepDelay);

  digitalWrite(bMotorCoil_1, LOW);
  digitalWrite(bMotorCoil_2, HIGH);
  digitalWrite(bMotorCoil_3, LOW);
  digitalWrite(bMotorCoil_4, LOW);

  delay(u16StepDelay);

  digitalWrite(bMotorCoil_1, LOW);
  digitalWrite(bMotorCoil_2, LOW);
  digitalWrite(bMotorCoil_3, HIGH);
  digitalWrite(bMotorCoil_4, LOW);

  delay(u16StepDelay);

  digitalWrite(bMotorCoil_1, LOW);
  digitalWrite(bMotorCoil_2, LOW);
  digitalWrite(bMotorCoil_3, LOW);
  digitalWrite(bMotorCoil_4, HIGH);

  delay(u16StepDelay);

  digitalWrite(bMotorCoil_1, LOW);
  digitalWrite(bMotorCoil_2, LOW);
  digitalWrite(bMotorCoil_3, LOW);
  digitalWrite(bMotorCoil_4, LOW);

}

void vStepMotor2(boolean bDirection, word u16StepDelay)
{
  /* Holds which DIO pin is currently associated with which motor coil */
  byte bMotorCoil_1;
  byte bMotorCoil_2;
  byte bMotorCoil_3;
  byte bMotorCoil_4;

  /* Set the order of the DIO pins depending on the direction the
     motor is requires to turn in. */
  if (bDirection == true)
  {
    bMotorCoil_1 = MOTOR2_COIL_1_DIO;
    bMotorCoil_2 = MOTOR2_COIL_2_DIO;
    bMotorCoil_3 = MOTOR2_COIL_3_DIO;
    bMotorCoil_4 = MOTOR2_COIL_4_DIO;
  }else
  {
    bMotorCoil_1 = MOTOR2_COIL_4_DIO;
    bMotorCoil_2 = MOTOR2_COIL_3_DIO;
    bMotorCoil_3 = MOTOR2_COIL_2_DIO;
    bMotorCoil_4 = MOTOR2_COIL_1_DIO;
  }


  /* Pulse each of the stepper motors coils in a sequential order */
  digitalWrite(bMotorCoil_1, HIGH);
  digitalWrite(bMotorCoil_2, LOW);
  digitalWrite(bMotorCoil_3, LOW);
  digitalWrite(bMotorCoil_4, LOW);

  delay(u16StepDelay);

  digitalWrite(bMotorCoil_1, LOW);
  digitalWrite(bMotorCoil_2, HIGH);
  digitalWrite(bMotorCoil_3, LOW);
  digitalWrite(bMotorCoil_4, LOW);

  delay(u16StepDelay);

  digitalWrite(bMotorCoil_1, LOW);
  digitalWrite(bMotorCoil_2, LOW);
  digitalWrite(bMotorCoil_3, HIGH);
  digitalWrite(bMotorCoil_4, LOW);

  delay(u16StepDelay);

  digitalWrite(bMotorCoil_1, LOW);
  digitalWrite(bMotorCoil_2, LOW);
  digitalWrite(bMotorCoil_3, LOW);
  digitalWrite(bMotorCoil_4, HIGH);


  delay(u16StepDelay);

  digitalWrite(bMotorCoil_1, LOW);
  digitalWrite(bMotorCoil_2, LOW);
  digitalWrite(bMotorCoil_3, LOW);
  digitalWrite(bMotorCoil_4, LOW);
}
