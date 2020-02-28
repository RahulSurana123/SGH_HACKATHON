//template<class T> inline Print &operator <<(Print &obj, T arg) { obj.print(arg); return obj; }
bool val[29];
bool out[29];
void setup() {
  pinMode(2,INPUT);
  pinMode(3,INPUT);
  pinMode(4,INPUT);
  Serial.begin(9600); 
  
}
int k=0;

void loop() {
  
 for(int i=0,j=0;i<=29;i++)
          { 
                      
            val[i]=digitalRead(k+2);
            if(val[i]==0)
            {
              
                out[j]=i;
                Serial.print(i);
                Serial.print(" ");
                j++;
              
            }
//             Serial.print(val[i]);
//             if(i==0||i==1)
//             Serial.print(",");
             k++;
             if(k>2)
                k=0;
             if(i==29)
                Serial.print("\n");
          }

     
//          Serial.print("{%c,%c,%c}",val[0]?"1":"0",val[1]?"1":"0",val[2]?"1":"0");
//  for(int i=0;i<=2;i++)
//          {
// 
//          Serial.println(val[i]);
//          
//  }

////  
//  for(int i=0;i<=2;i++)
//          {       
//            if(i==2)
//                Serial.println(val[i]);
//                delay(250);
//          }
//   Serial.println("val");
//   delay(500);
//  int f1 = val[0];
//  int f2 = val[1];
//  int f3 = val[2];
//  int arr[3] = { f1, f2, f3 };
//  Serial<< "{" << f1 << "," << f2 << "," << f3<< "}";
//  Serial.println();
//  for(int i=0;i<=2;i++)
//          {
//            if(val[i] == 0)
//                out[i]=1;
//             else
//                out[i]=0;
//           }
// Serial.println("out");
// delay(500);
//  int g1 = out[0];
//  int g2 = out[1];
//  int g3 = out[2];
//  int ar[3] = { g1, g2, g3 };
//  Serial << "{"<< g1 << "," << g2 << "," << g3 << "}";
//  Serial.println();
}
