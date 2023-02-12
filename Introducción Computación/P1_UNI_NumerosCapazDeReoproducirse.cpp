#include<iostream>
using namespace std;
int main()
{
	int num,t1,t2,t3=0;
	cout<<"Ingrese un numero:";
	cin>>num;
	
	int decena,unidad;
	unidad = num%10;
	decena = num/10;
	t1 = decena;
	t2 = unidad;
	
	cout<<" [+] Sucesion de "<<num<<": "<<endl;
	cout<<" "<<t1<<" "<<t2;
	
	while(t3<=num)
	{
		t3 = t1 + t2;
		cout<<" "<<t3;
		t1=t2;
		t2=t3;
		if(t3==num)
		{
			cout<<"\n El numero "<<num<<
			" es capaz de reproducirse."<<endl;
			break;
		}
	}
	
	// Numeros de dos digitos capaz de reproducirse
	cout<<"\n\n\t Numeros de 2 Digitos Capaz de Reproducirse"<<endl;
	cout<<"\t ------------------------------------------"<<endl;
	for(int i=10;i<=99;i++)
	{
		unidad = i%10;
		decena = i/10;
		
		t1=decena;
		t2=unidad;
		t3=t1+t2;
		cout<<"\n\t[ ] Sucesion:";
		cout<<" "<<t1<<" "<<t2;
		while(t3<=i)
		{
			t3=t1+t2;
			cout<<" "<<t3;
			t1=t2;
			t2=t3;
			if(t3==i)
			{
				cout<<"\n\n [+] El numero "<<i<<
				" es capaz de reproducirse."<<endl;
				break;
			}
		}
	}
 	
	
	return 0;
}