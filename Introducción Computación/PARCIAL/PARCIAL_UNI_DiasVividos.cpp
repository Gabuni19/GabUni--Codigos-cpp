#include<iostream>
using namespace std;
int main()
{
	int d,m,a;
	int dc,mc,ac;
	int dt,mt,at;
	int diasT;
	int dias_restantes,dias_centrales,dias_faltantes;
	cout<<"\t[+] Ingrese sus datos de entrada:"<<endl;
	cout<<"\t-> Fecha de Nacimiento "<<endl;
	cout<<"-----------------------------------"<<endl;
	cout<<"\tdia: ";
	cin>>d;
	cout<<"\tmes: ";
	cin>>m;
	cout<<"\tyear: ";
	cin>>a;
	
	cout<<"\n\t-> Fecha de Consulta "<<endl;
	cout<<"-----------------------------------"<<endl;
	cout<<"\tdia: ";
	cin>>dc;
	cout<<"\tmes: ";
	cin>>mc;
	cout<<"\tyear: ";
	cin>>ac;
	
	//Calculamos los dias que pasaron
	//-> considerando año = 12 meses, mes=30 dias;
	
	dias_restantes = (30 - d) + 30*(12 - m);
	dias_centrales = 360 * (ac-a-1);
	dias_faltantes = 30*(mc-1) + dc;
	
	diasT=dias_restantes+dias_centrales+dias_faltantes;
	
	at = diasT/360;
	mt = (diasT%360)/30;
	dt = (diasT%360)%30;
	
	cout<<"-----------------------------------"<<endl;
	cout<<"\n\t[+] Usted ha vivido "<<
	at<<" anios "<<
	mt<<" meses y "<<
	dt<<" dias"<<endl;
	
	
	
	return 0;
}