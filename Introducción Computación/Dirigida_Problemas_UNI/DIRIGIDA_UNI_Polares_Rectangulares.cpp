#include<iostream>
#include<iomanip>
#include<cmath>

void P_R(double r,double theta
         ,double& x,double& y)
{
    x = r*cos(theta);
	y = r*sin(theta);   	
}


using namespace std;
int main()
{
	double r,theta,angulo_S;
	double x,y;
	
	cout<<"\tIngresa un angulo (grados):";	
	cin>>theta;
	
	angulo_S=theta*(M_PI/180);
	
	cout<<"\tIngresa el r :";
	cin>>r;
	
	P_R(r,angulo_S,x,y);
	cout<< "\tLas coordenadas rectangulares son: (" 
	<<fixed<<setprecision(4)
	<< x << ", " 
	<<fixed<<setprecision(4)
	<< y << ")" <<endl;
		
	return 0;
}