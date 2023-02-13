#include<iostream>
using namespace std;
imprimirOrden(int a,int b,int c)
{
	cout<<"\n\ta - b - c: "
	<<a<<" "<<b<<" "<<c<<endl;
}

int main()
{ 
	int a,b,c;
	int central;
	
	cout<<"\tIngresa 3 numeros:"<<endl;
	cout<<"\tnumero 1:";
	cin>>a;
	cout<<"\tnumero 2:";
	cin>>b;
	cout<<"\tnumero 3:";
	cin>>c;
	cout<<"\ta - b - c: "
	<<a<<" "<<b<<" "<<c<<endl;
	
	cout<<"\tOrdenando : ";
	
	
	if(a<b)
	{
		if(c>b)
		{
			imprimirOrden(a,b,c);
			central=b;	
		}else{
			if(c>a)
			{
				imprimirOrden(a,c,b);
				central=c;
			}else{
				imprimirOrden(c,a,b);
				central=a;
			}			
		}				
	}else{
		if(c>a)
		{
			imprimirOrden(b,a,c);
			central=a;
		}else{
			if(c>b)
			{
				imprimirOrden(b,c,a);
				central=c;
			}else{
				imprimirOrden(c,b,a);
				central=b;
			}
		}		
	}
	
	
	cout<<"\tCentral: "<<central<<endl;
	
	return 0;
}