#include<iostream>
using namespace std;

double Combinatoria_R(int n,int k)
{
	if(k==0) return 1;
	if(k==n) return 1;
	
	return   Combinatoria_R(n-1,k)
			+Combinatoria_R(n-1,k-1);
}

int main()
{
	cout<<Combinatoria_R(24,17)<<endl;
	return 0;
}