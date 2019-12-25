const int Xpin = A0; // analog pin connected to X output
const int Ypin = A1; // analog pin connected to Y output
const int FL = 11;
const int FR = 10;
const int BL = 6;
const int BR = 5;
int m;
int n;
void setup() {
  pinMode(Xpin, INPUT);
  pinMode(Ypin, INPUT);
  pinMode(FL,OUTPUT);
  pinMode(FR,OUTPUT);
  pinMode(BL,OUTPUT);
  pinMode(BR,OUTPUT);
  Serial.begin(9600);
}

void loop() {
int  X = analogRead(Xpin) - 493;
int  Y = analogRead(Ypin) - 500;
n = 0;
Serial.println("X = ");
Serial.println(X);
Serial.println("Y = ");
Serial.println(Y);
if(X==0 && Y==0)
{/*move nowhere*/
analogWrite(FL,0);
analogWrite(FR,0);
analogWrite(BL,0);
analogWrite(BR,0);
}
if(X==0 && Y==-500)
{/*move forward*/
analogWrite(FL,1023);
analogWrite(FR,1023);
analogWrite(BL,0);
analogWrite(BR,0);
}
if(X==529 && Y==0)
{/*hard right*/
analogWrite(FL,1023);
analogWrite(FR,0);
analogWrite(BL,0);
analogWrite(BR,1023);
}
if(X==-493 && Y==0)
{/*hard left*/
analogWrite(FL,0);
analogWrite(FR,1023);
analogWrite(BL,1023);
analogWrite(BR,0);
}

if(X==0 && Y==523)
{/*move back*/
analogWrite(FL,0);
analogWrite(FR,0);
analogWrite(BL,1023);
analogWrite(BR,1023);
}
if(X == 529 && Y<0 && Y>-500)
{/*1*/
  n = map(Y,-500,0,0,255);
analogWrite(FL,255);
analogWrite(FR,0);
analogWrite(BL,0);
analogWrite(BR,n);
}

if(X<529 && X>0 && Y == -500)
{/*2*/
  n = map(X,529,0,0,255);
analogWrite(FL,255);
analogWrite(FR,n);
analogWrite(BL,0);
analogWrite(BR,0);
}
if(X == -493 && Y<0 && Y>-500)
{/*4*/
  n = map(Y,-500,0,0,255);
analogWrite(FL,0);
analogWrite(FR,255);
analogWrite(BL,n);
analogWrite(BR,0);
}

if(X<0 && X>-493 && Y == -500)
{/*3*/
  n = map(X,-493,0,0,255);
analogWrite(FL,n);
analogWrite(FR,255);
analogWrite(BL,0);
analogWrite(BR,0);
}
if(X == 529 && Y<523 && Y>0)
{/*8*/
  n = map(Y,523,0,0,255);
analogWrite(FL,0);
analogWrite(FR,n);
analogWrite(BL,255);
analogWrite(BR,0);
}

if(X<529 && X>0 && Y == 523)
{/*7*/
  n = map(X,529,0,0,255);
analogWrite(FL,0);
analogWrite(FR,0);
analogWrite(BL,255);
analogWrite(BR,n);
}

if(X == -493 && Y<523 && Y>0)
{/*5*/
n = map(Y,523,0,0,255);
analogWrite(FL,n);
analogWrite(FR,0);
analogWrite(BL,0);
analogWrite(BR,255);
}

if(X<0 && X>-493 && Y == 523)
{/*6*/
  n = map(X,-493,0,0,255);
analogWrite(FL,0);
analogWrite(FR,0);
analogWrite(BL,n);
analogWrite(BR,255);
}
}
