#include<iostream>
using namespace std;

long long n_Bacterias(int inicial,int horas)
{
	if(horas==0) return inicial;
	return 2*n_Bacterias(inicial,horas-1);
}


int main()
{
	cout<<"Despues de 24 horas hay ";
	cout<<n_Bacterias(1000,24)<<" bacterias."<<endl;
	return 0;
}