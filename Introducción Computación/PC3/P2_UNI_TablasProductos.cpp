#include<iostream>
#include<cstdlib>
#include<ctime>
#include<iomanip>
#define N 12
#define M 10
using namespace std;

int main()
{
	srand(time(NULL));
	
	int meses,productos;
	cout<<"Cuantos meses desea (1-12):";
	cin>>meses;
	
	cout<<"Cuantos productos desea (1-10):";
	cin>>productos;
	
	int C_vendida[N][M];
	int P_producto[N][1];
	
	//Rellenamos la tabla 1
	for(int i=0;i<meses;i++)
	{
		for(int j=0;j<productos;j++){
			C_vendida[i][j]=rand()%(51);
		}		
	}
	
	//Rellenamos la tabla 2
	for(int i=0;i<productos;i++)
	{
		for(int j=0;j<1;j++){
			P_producto[i][j]=1+rand()%(10);
		}		
	}
	
	cout<<setw(4)<<"M/P";
	//Imprimimos tabla1	
	for(int i=0;i<productos;i++)
		cout<<setw(4)<<i+1;	
	cout<<endl;
	
	for(int i=0;i<meses;i++)
	{
		cout<<setw(4)<<i+1;
		for(int j=0;j<productos;j++){
			cout<<setw(4)<<C_vendida[i][j];
		}
		cout<<endl;		
	}
	//Imprimimos tabla2
	cout<<endl;
	cout<<setw(9)<<"Producto"
		<<setw(9)<<"Precio"<<endl;	
	
	for(int i=0;i<productos;i++)
	{
		cout<<setw(9)<<i+1;
		for(int j=0;j<1;j++){
			cout<<setw(9)<<P_producto[i][j];
		}
		cout<<endl;		
	}
	cout<<endl;
	//Tabla Monto Vendido
	
	int Monto[N][M];
	for(int i=0;i<meses;i++)
	{
		for(int j=0;j<productos;j++){
			Monto[i][j]=C_vendida[i][j]*P_producto[j][0];
		}		
	}
	
	cout<<setw(4)<<"M/P";
	//Imprimimos tabla MONTO	
	for(int i=0;i<productos;i++)
		cout<<setw(4)<<i+1;	
	cout<<endl;
	
	for(int i=0;i<meses;i++)
	{
		cout<<setw(4)<<i+1;
		for(int j=0;j<productos;j++){
			cout<<setw(4)<<Monto[i][j];
		}
		cout<<endl;		
	}
	
	
	return 0;
}