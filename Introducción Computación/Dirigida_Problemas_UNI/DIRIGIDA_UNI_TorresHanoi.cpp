#include<iostream>
using namespace std;

//o= origen , d = destino a = auxiliar
void Hanoi(int n,string o,string d,string a)
{
	if(n==1)
	{
		cout<<"\tPasar el disco "
		<< n << " del "<<o<<" a "
		<<d<<endl;
		return;
	}
	
	Hanoi(n-1,o,a,d);
	cout<<"\tPasar el disco "
	<< n << " del "<<o<<" a "
	<<d<<endl;
	Hanoi(n-1,a,d,o);
}


int main()
{
	Hanoi(3,"A","B","C");
	return 0;
}