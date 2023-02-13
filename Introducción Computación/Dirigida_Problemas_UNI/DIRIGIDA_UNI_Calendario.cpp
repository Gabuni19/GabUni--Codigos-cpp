#include<iostream>
#include<iomanip>
using namespace std;

int D_Semana(int a,int m,int d)
{
	int n;
	//Formula de Zeller
	int x = (14 - m)/12;
	int y = a - x;
	int z = m + 12*x-2;
	
	n= d + y + y/4 - y/100
		 +y/400 + (31*z)/12;
	return n%7;
}

void Calendario(int a, int m)
{
	int dMax[] ={31,28,31,30,31
				 ,30,31,31,30,31
				 ,30,31	};
	//Cambiamos si es un year bisiesto
	if ( (a%4==0 && a%100!=0) 
	     || a%400 == 0 )
	{
	   dMax[1]  = 29;	
	}
	
	//Imprimimos calendario
	
	cout<<setw(3)<<"D"
		<<setw(3)<<"L"
		<<setw(3)<<"M"
		<<setw(3)<<"M"
		<<setw(3)<<"J"
		<<setw(3)<<"V"
		<<setw(3)<<"S"<<endl;
	
	//Calculamos el dia de la semana
	// que cae el primer dia del mes
	
	int d_Sem=  D_Semana(a,m,1);
	for(int j=0;j<d_Sem;j++) 
		cout<<setw(3)<<" ";
	
	for(int i=1;i<=dMax[m-1];i++)
	{
		cout<<setw(3)<<i;
		if( (i + d_Sem)%7==0 ) cout<<endl;
	}
	
}

int main()
{
	int year,mes,dia;
	string d[]={"Domingo","Lunes","Martes"
				,"Miercoles","Jueves"
				,"Viernes","Sabado"};
	cout<<"\t Ingresa el year:";
	cin>>year;
	cout<<"\t Ingresa el mes:";
	cin>>mes;
	cout<<"\t Ingresa el dia:";
	cin>>dia;
	
	int f=D_Semana(year,mes,dia);
	cout<<"Fecha: "<<d[f]<<endl;
	cout<<endl;
	cout<<"\t Calendario"<<endl;
	Calendario(year,mes);
	
	return 0;
}








