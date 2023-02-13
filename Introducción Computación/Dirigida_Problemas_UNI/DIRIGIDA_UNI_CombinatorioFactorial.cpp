#include<iostream>
using namespace std;
//Funcion solo llega a 16!
int factorial(int n)
{
	int factorial=1;	
	for(int i=1;i<=n;i++)	
		factorial=factorial*i;	
	
	return factorial;	
}
//Se reduce las posibilidades de lo que pueda calcular
double Combinatoria(int n,int k)
{
	return factorial(n)/(factorial(k)*factorial(n-k));
}
int main()
{
	cout<<Combinatoria(6,0)<<endl;
	return 0;
}