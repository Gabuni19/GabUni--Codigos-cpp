#include<iostream>
using namespace std;
int buscarRima(string* A,int n,int i)
{
	int indice=-1;
	string r="";
	int l = A[i].size();	
	
	for(int j=i+1;j<n;j++)
	{
		r=A[j];		
		int t=r.size();			
		if(    r[t-3] == A[i][l-3] 
			&& r[t-2] == A[i][l-2] 
			&& r[t-1] == A[i][l-1] )
			{
				return j;
			}
	}	
	return indice;
}


int main()
{
	string versos[]={
			"En la plantacion de cania",
			"nacio el triste socabon",
			"en el trapiche de ron",
			"el negro canto la zania",
			"el machete y la guadania",
			"curtio sus manos morenas",
			"y los indios con sus quenas",
			"y el negro con tamborete",
			"cantaron su triste suerte",
		    "al compas de las cadenas"};	
		    
	int n=sizeof(versos)/sizeof(versos[0]);	
	cout<<"\n\t Versos Iniciales "<<endl;
	for(int i=0;i<n;i++)
		cout<<"\t"<<versos[i]<<endl;		
	cout<<endl;
	
	for(int i=0;i<n-1;i++)
	{
		int indice=buscarRima(versos,n,i);		
		if(indice!=-1)
		{
			string aux=versos[i+1];
			versos[i+1]=versos[indice];
			versos[indice]=aux;
		}
	}
	cout<<"\n\t Versos Modificados "<<endl;
	for(int i=0;i<n;i++)
		cout<<"\t"<<versos[i]<<endl;	    
		    
	return 0;
}