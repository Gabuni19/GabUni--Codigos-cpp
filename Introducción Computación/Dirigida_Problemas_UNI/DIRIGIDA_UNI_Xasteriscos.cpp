#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int n,k=1,p;
	cout<<"Ingrese un numero:";
	cin>>n;
	if(n%2!=0)
	{
		p=n-k;
		for(int i=0;i<n;i++)
		{
			if(i<(n/2)+1)
			{
				cout<<setw(k)<<"*";
				if(p!=0)
				{
					cout<<setw(p)<<"*";
					p-=2;
					k++;
				}
			}else{
				k--;
				p+=2;
				cout<<setw(k)<<"*";
				cout<<setw(p)<<"*";
			}
			cout<<endl;
		}
		
	}else{
		
		p=n-k;
		for(int i=0;i<n;i++)
		{
		
			if(i<(n/2))
			{
				cout<<setw(k)<<"*";
				if(p>2)
				{
					cout<<setw(p)<<"*";
					p-=2;
					k++;
				}else if(p==1){
					cout<<setw(1)<<"*";
				}
				
			}else if(i==n/2)
			{
				cout<<setw(k)<<"*";
				cout<<setw(1)<<"*";
			}else{
				k--;
				p+=2;
				cout<<setw(k)<<"*";
				cout<<setw(p)<<"*";
				
			}
			cout<<endl;
		}
		
	}
	
	return 0;
}













