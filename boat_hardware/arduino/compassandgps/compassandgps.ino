#include <TinyGPSPlus.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <SoftwareSerial.h>

static const int RXPin = 7, TXPin = 4;
static const uint32_t GPSBaud = 9600;

// The TinyGPS++ object
TinyGPSPlus gps;

// The serial connection to the GPS device
SoftwareSerial ss(RXPin, TXPin);


uint16_t BNO055_SAMPLERATE_DELAY_MS = 100;

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                   id, address
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28, &Wire);



void setup() {
  // put your setup code here, to run once:

//claude wrote this:
  Serial.begin(115200);
  Serial.println("debug: booted");
  delay(1000);
  ss.begin(GPSBaud);

  // ADD THIS
  if (!bno.begin()) {
    Serial.println("ERROR: BNO055 not detected. Check wiring/address.");
    while (1);  // halt so you can see the message
  }
  Serial.println("debug: BNO055 initialized");
//end of what claude wrote


  Serial.begin(115200);
  Serial.println("debug: booted");
//  while (!Serial) delay(10);  // wait for serial port to open!

//  Serial.println("Orientation Sensor Test"); Serial.println("");

  /* Initialise the sensor */
//  Serial.println("I'm stupid");
  delay(1000);
  ss.begin(GPSBaud);
}

int latlon = "";

void gpsjson(){
  Serial.println("debug: Gpsjson running");
  Serial.println("debug: Gpsjson running");
  //retry getting a gps lock
  for(int i = 0; i >= 5; i++){
    Serial.print("debug: Try ");
    Serial.print(i);
    Serial.println(" of 5 of getting the GPS lock");
    Serial.println(ss.read());
    if (ss.available() > 0){
        gps.encode(ss.read());
        Serial.println("debug: got gps lock");
    //  if (gps.location.isUpdated()){
        // Latitude in degrees (double)
        Serial.print("{'latitude': ");
        Serial.print(gps.location.lat(), 6);      
        Serial.println(",");
        
        Serial.print("'longitude': ");
        Serial.print(gps.location.lng(), 6); 
        Serial.println(",");
  
  //      Serial.print(gps.location.rawLat().negative ? "-" : "+");
  //      Serial.println(gps.location.rawLat().deg); 
  //      // ... and billionths (u16/u32)
  //      Serial.println(gps.location.rawLat().billionths);
        
        // Raw longitude in whole degrees
  //      Serial.print("Raw longitude = "); 
  //      Serial.print(gps.location.rawLng().negative ? "-" : "+");
  //      Serial.println(gps.location.rawLng().deg); 
  //      // ... and billionths (u16/u32)
  //      Serial.println(gps.location.rawLng().billionths);
  
        // Raw date in DDMMYY format (u32)
        Serial.print("'date': ");
        Serial.print(gps.date.value()); 
        Serial.println(",");
  
  //      // Year (2000+) (u16)
  //      Serial.print("Year = "); 
  //      Serial.println(gps.date.year()); 
  //      // Month (1-12) (u8)
  ///      Serial.print("Month = "); 
  //      Serial.println(gps.date.month()); 
  //      // Day (1-31) (u8)
  //      Serial.print("Day = "); 
  //      Serial.println(gps.date.day()); 
  
        // Raw time in HHMMSSCC format (u32)
        Serial.print("'time': "); 
        Serial.print(gps.time.value()); 
        Serial.println(",");
  
        // Hour (0-23) (u8)
  //      Serial.print("Hour = "); 
  //      Serial.println(gps.time.hour()); 
  //      // Minute (0-59) (u8)
  ///      Serial.print("Minute = "); 
  //      Serial.println(gps.time.minute()); 
        // Second (0-59) (u8)
  //      Serial.print("Second = "); 
  //      Serial.println(gps.time.second()); 
        // 100ths of a second (0-99) (u8)
  //      Serial.print("Centisecond = "); 
  //      Serial.println(gps.time.centisecond()); 
  
        // Raw speed in 100ths of a knot (i32)
  //      Serial.print("Raw speed in 100ths/knot = ");
  //      Serial.println(gps.speed.value()); 
        // Speed in knots (double)
        Serial.print("'speed': ");
        Serial.print(gps.speed.knots()); 
        Serial.println(',');
        
        
        // Speed in miles per hour (double)
        Serial.print("'mph': ");
        Serial.print(gps.speed.mph()); 
        Serial.println(",");
        // Speed in meters per second (double)
  //      Serial.print("Speed in m/s = ");
  //      Serial.println(gps.speed.mps()); 
        // Speed in kilometers per hour (double)
  //      Serial.print("Speed in km/h = "); 
  //      Serial.println(gps.speed.kmph()); 
  
        // Raw course in 100ths of a degree (i32)
  //      Serial.print("Raw course in degrees = "); 
  //      Serial.println(gps.course.value()); 
        // Course in degrees (double)
        Serial.print("'course': "); 
        Serial.print(gps.course.deg()); 
        Serial.println(",");
  
        // Raw altitude in centimeters (i32)
  //      Serial.print("Raw altitude in centimeters = "); 
  //      Serial.println(gps.altitude.value()); 
        // Altitude in meters (double)
  //      Serial.print("Altitude in meters = "); 
  //      Serial.println(gps.altitude.meters()); 
        // Altitude in miles (double)
  //      Serial.print("Altitude in miles = "); 
  //      Serial.println(gps.altitude.miles()); 
        // Altitude in kilometers (double)
  //      Serial.print("Altitude in kilometers = "); 
  //      Serial.println(gps.altitude.kilometers()); 
        // Altitude in feet (double)
        Serial.print("'altitude': "); 
        Serial.print(gps.altitude.feet()); 
        Serial.println(",");
  
        // Number of satellites in use (u32)
  //      Serial.print("Number os satellites in use = "); 
  //      Serial.println(gps.satellites.value()); 
  
        // Horizontal Dim. of Precision (100ths-i32)
  //      Serial.print("HDOP = "); 
  //      Serial.println(gps.hdop.value()); 
    ///  }
    } else{
      Serial.println("debug: no gps lock. trying again");
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  gpsjson();
  sensors_event_t orientationData , angVelocityData , linearAccelData, magnetometerData, accelerometerData, gravityData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);
  bno.getEvent(&magnetometerData, Adafruit_BNO055::VECTOR_MAGNETOMETER);
  bno.getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);
  bno.getEvent(&gravityData, Adafruit_BNO055::VECTOR_GRAVITY);

  printEvent(&orientationData);
  printEvent(&angVelocityData);
  printEvent(&linearAccelData);
  printEvent(&magnetometerData);
  printEvent(&accelerometerData);
  printEvent(&gravityData);

  int8_t boardTemp = bno.getTemp();
  Serial.println();
  Serial.print(F("temperature: "));
  Serial.println(boardTemp);

  uint8_t system, gyro, accel, mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);
  Serial.println();
  Serial.print("Calibration: Sys=");
  Serial.print(system);
  Serial.print(" Gyro=");
  Serial.print(gyro);
  Serial.print(" Accel=");
  Serial.print(accel);
  Serial.print(" Mag=");
  Serial.println(mag);

  Serial.println("--");
  delay(BNO055_SAMPLERATE_DELAY_MS);
}

void printEvent(sensors_event_t* event) {
  double x = -1000000, y = -1000000 , z = -1000000; //dumb values, easy to spot problem
  if (event->type == SENSOR_TYPE_ACCELEROMETER) {
    Serial.print("Accl:");
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
  }
  else if (event->type == SENSOR_TYPE_ORIENTATION) {
    Serial.print("Orient:");
    x = event->orientation.x;
    y = event->orientation.y;
    z = event->orientation.z;
  }
  else if (event->type == SENSOR_TYPE_MAGNETIC_FIELD) {
    Serial.print("Mag:");
    x = event->magnetic.x;
    y = event->magnetic.y;
    z = event->magnetic.z;
  }
  else if (event->type == SENSOR_TYPE_GYROSCOPE) {
    Serial.print("Gyro:");
    x = event->gyro.x;
    y = event->gyro.y;
    z = event->gyro.z;
  }
  else if (event->type == SENSOR_TYPE_ROTATION_VECTOR) {
    Serial.print("Rot:");
    x = event->gyro.x;
    y = event->gyro.y;
    z = event->gyro.z;
  }
  else if (event->type == SENSOR_TYPE_LINEAR_ACCELERATION) {
    Serial.print("Linear:");
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
  }
  else if (event->type == SENSOR_TYPE_GRAVITY) {
    Serial.print("Gravity:");
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
  }
  else {
    Serial.print("Unk:");
  }

  Serial.print("\tx= ");
  Serial.print(x);
  Serial.print(" |\ty= ");
  Serial.print(y);
  Serial.print(" |\tz= ");
  Serial.println(z);
}
