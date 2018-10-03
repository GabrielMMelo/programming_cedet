#include <Wire.h>
#include <NewTone.h>
#include "notas.h"

#define LDR A0
#define LED1 11
#define LED2 10
#define LED3 9

const byte BUT = 2;
void setup() {
  Serial.begin(9600);
  pinMode(LDR,INPUT);
  pinMode(BUT,INPUT_PULLUP);
  pinMode(LED1,OUTPUT);
  pinMode(LED2,OUTPUT);
  pinMode(LED3,OUTPUT);
  pinMode(buzzer,OUTPUT);
  attachInterrupt(digitalPinToInterrupt(BUT), interrupt, FALLING);
}

volatile bool flag = false;

void interrupt() {
  flag = true;
}

float leitura_ldr;
void loop() {
 leitura_ldr = map(analogRead(LDR),0,255,0,100);
 if(leitura_ldr < 10){
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, HIGH);
    digitalWrite(LED3, HIGH);
 }
 else{
    digitalWrite(LED3, LOW);
    digitalWrite(LED2, HIGH);
    digitalWrite(LED1, HIGH);
 }
 if(flag){
  StarWars();
  flag = false;
 }
 delay(1000);

}
