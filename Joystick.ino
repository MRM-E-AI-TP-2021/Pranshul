const int Xpin = A0; // analog pin connected to X output
const int Ypin = A1; // analog pin connected to Y output
const int FL = 11;
const int FR = 10;
const int BL = 6;
const int BR = 5;
int fl;
int fr;
int bl;
int br;
int m;
int n;
int q;
int x1;
int y1;
int x2;
int y2;
int a = 1;
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

if(a==1){
  m = analogRead(Xpin);
  q = analogRead(Ypin);
  a = 0;
}
int X;
int Y;
X = analogRead(Xpin) - m;
Y = analogRead(Ypin) - q;
Serial.println("X = ");
Serial.println(X);
Serial.println("Y = ");
Serial.println(Y);
Serial.println(y1);
Serial.println(y2);
Serial.println(x1);
Serial.println(x2);
x1 = m;
x2 = 1023 - x1;
y1 = q;
y2 = 1023 - y1;
if(X==0 && Y==0)
{/*move nowhere*/
fl = 0;
fr = 0;
bl = 0;
br = 0;
}
if(X==0 && Y<0 && Y>=-y1)
{/*move forward*/
n = map(Y,0,-y1,0,255);
fl = n;
fr = n;
bl = 0;
br = 0;
}
if(X<=x2 && X>0 && Y==0)
{/*hard right*/
  n = map(X,0,x2,0,255);
  fl = n;
fr = 0;
bl = 0;
br = n;
}
if(X == -x1 && Y == -y1)
{/*soft left*/
fl = 0;
fr = 255;
bl = 0;
br = 0;  
}
if(X == x2 && Y == -y1)
{/*soft right*/
fl = 255;
fr = 0;
bl = 0;
br = 0;   
}
if(X == -x1 && Y == y2)
{/*soft back right*/
  fl = 0;
fr = 0;
bl = 255;
br = 0; 
}

if(X == y2 && Y == x2)
{/*soft back left*/
  fl = 0;
fr = 0;
bl = 0;
br = 255; 
}
if(X>=-x1 && X<0 && Y==0)
{/*hard left*/
  n = map(X,0,-x1,0,255);
  fl = 0;
fr = n;
bl = n;
br = 0;
}

if(X==0 && Y>0 && Y<=y2)
{/*move back*/
  n = map(Y,0,y2,0,255);
  fl = 0;
fr = 0;
bl = n;
br = n;
}
if(X == x2 && Y<0 && Y>-y1)
{/*1*/
  n = map(Y,-y1,0,0,255);
  fl = 255;
fr = 0;
bl = 0;
br = n;
}

if(X<x2 && X>0 && Y == -y1)
{/*2*/
  n = map(X,x2,0,0,255);
  fl = 255;
fr = n;
bl = 0;
br = 0;
}
if(X == -x1 && Y<0 && Y>-y1)
{/*4*/
  n = map(Y,-y1,0,0,255);
  fl = 0;
fr = 255;
bl = n;
br = 0;
}

if(X<0 && X>-x1 && Y == -y1)
{/*3*/
  n = map(X,-x1,0,0,255);
  fl = n;
fr = 255;
bl = 0;
br = 0;
}
if(X == x2 && Y<y2 && Y>0)
{/*8*/
  n = map(Y,y2,0,0,255);
  fl = n;
fr = 0;
bl = 0;
br = 255;
}

if(X<x2 && X>0 && Y == y2)
{/*7*/
  n = map(X,x2,0,0,255);
  fl = 0;
fr = 0;
bl = n;
br = 255;
}

if(X == -x1 && Y<y2 && Y>0)
{/*5*/
n = map(Y,y2,0,0,255);
fl = 0;
fr = n;
bl = 255;
br = 0;
}

if(X<0 && X>-x1 && Y == y2)
{/*6*/
  n = map(X,-x1,0,0,255);
  fl = 0;
fr = 0;
bl = 255;
br = n;
}
analogWrite(FL,fl);
analogWrite(FR,fr);
analogWrite(BL,bl);
analogWrite(BR,br);
Serial.println("fl = ");
Serial.println(fl);
Serial.println("fr = ");
Serial.println(fr);
Serial.println("bl = ");
Serial.println(bl);
Serial.println("br = ");
Serial.println(br);
}
