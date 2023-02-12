#include<iostream>
#include<cstdlib>
#include<ctime>
#define N 20
using namespace std;
int main()
{
	
	srand(time(NULL));
	int n;
	int i,j;
	cout<<"\t Cuantos numeros desea? (1-20): ";
	cin>>n;
	
	int arreglo[N];
	int ordenado[N];
	
	for(i=0;i<n;i++)
		arreglo[i]=1+rand()%(50-1+1);
		
	int mayor=-1;
	
	for(i=0;i<n;i++)
		if(arreglo[i]>mayor) mayor=arreglo[i];
		
	int k=0;
	for(j=1;j<mayor;j++)
	{
		for(i=0;i<n;i++)
		{
			if(arreglo[i]==j)
			{
				ordenado[k++]=j;
				break;
			}
		}
	}
	cout<<"\t mayor: "<<mayor<<endl;
	
	cout<<"\t Arreglo creado:"<<endl;
	cout<<"\t";
	for(i=0;i<n;i++)
		cout<<arreglo[i]<<" ";
		
	cout<<endl;
	cout<<"\t Arreglo ordenado:"<<endl;
	cout<<"\t";
	for(i=0;i<k;i++)
		cout<<ordenado[i]<<" ";
	
	
	return 0;
}