#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int n,f=1,k,num=1;
	cout<<"Ingresa el lado del rombo:";
	cin>>n;
	k=n;
	
	for(int i=0;i<2*n-1;i++)
	{
		if(i<n)
		{
			cout<< setw(2*k) << num;
			for(int j=0;j<n-k;j++)
			{
				num++;
				cout<<setw(4)<<num;
			}
			num++;
			k--;
		}else{
			if(i==n)k+=2;
			cout<<setw(2*k)<<num;
			for(int j=0;j<n-k;j++)
			{
				num++;
				cout<<setw(4)<<num;
			}
			num++;
			k++;
		}
		cout<<endl;
	}
	
	
	return 0;
}
