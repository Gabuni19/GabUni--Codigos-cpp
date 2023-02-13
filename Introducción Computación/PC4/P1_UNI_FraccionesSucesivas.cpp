#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

float CalculandoX(int m,int i,int ultimo)
{
	if(i==(m+1)/2)
	{
		float t1 = (2*i-1);
		float t2 = pow(i,2);
		float t3 = ultimo;
		cout<<"Expresion de la ultima fraccion es:"<<endl;
		cout<<setw(6)<<t1<<" + "
			<<setw(6)<<t2<<" / "
			<<setw(8)<<t3<<" = "
			<<setw(8)<< t1+((t2)/(t3))<<endl;
		return t1+((t2)/(t3));	
	} 
	if(i<(m+1)/2)
	{
		float t1 = (2*i-1);
		float t2 = pow(i,2);
		float t3 = CalculandoX(m,i+1,ultimo);
		
		cout<<setw(6)<<t1<<" + "
			<<setw(6)<<t2<<" / "
			<<setw(8)<<t3<<" = "
			<<setw(8)<< t1+((t2)/(t3))<<endl;
		
		return t1+((t2)/(t3));
	} 
}



int main()
{
	float x = 4/CalculandoX(201,1,203);
	
	cout<<"El resultado es x = "<<x<<endl;
	
	return 0;
}
