#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}

void dscreen()
{
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Meter Status");
  lcd.setCursor(2, 1);
  lcd.print("DEACTIVATED");
}

void ascreen()
{
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Meter Status");
  lcd.setCursor(2, 1);
  lcd.print("ACTIVATED");
  delay(2000);
  lcd.clear();
}

void loop() {
  
  if (Serial.available() > 0) { // Check if there is any data available
    String receivedData = Serial.readString();
    int value = receivedData.toInt();

    if (value > 0) {
      if(value == 1)
      {
        Serial.print("Received value: ");
        Serial.println(receivedData);
        digitalWrite(12, LOW);
        digitalWrite(13, HIGH);
        ascreen();
      }else{
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Units");
        lcd.setCursor(2, 1);
        lcd.print(receivedData);
      }
    } else{
      Serial.print("Received value: ");
      Serial.println(receivedData);
      digitalWrite(13, LOW);
      digitalWrite(12, HIGH);
      dscreen();
    }
  }
  delay(1000);
}