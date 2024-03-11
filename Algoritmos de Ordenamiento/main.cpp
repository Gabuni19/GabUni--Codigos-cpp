#include <iostream>
#include <cmath>
using namespace std;
// Ordenamiento Radix

void imprimirMatriz(int** matriz,int m,int n){
    for (int i = 0; i < m; ++i) {
        cout<<"|\t";
        for (int j = 0; j < n; ++j) {
            cout<<matriz[i][j]<<"\t";
        }
        cout<<"|"<<endl;
    }
}

void imprimirArreglo(int* arreglo,int n){
    cout<<"Arreglo: |\t";
    for (int i = 0; i < n; ++i) {
        cout<<arreglo[i]<<"\t";
    }
    cout<<"|"<<endl;
}

int nMax(int* arreglo,int n){
    int max = -99999;
    for (int i = 0; i < n; ++i) {
        if(arreglo[i]>max){
            max = arreglo[i];
        }
    }
    return max;
}

int nDig(int numero){
    int ndig= 0;

    while(numero>0){
        numero = numero / 10;
        ndig++;
    }
    return ndig;
}

void ordenamientoRadix(int* arreglo,int n, int orden){
    int max = nMax(arreglo,n);
    int nDigMax = nDig(max);

    //cout<<"Elemento maximo: "<<max<<endl;
    //cout<<"nDigitos de max : "<<nDigMax<<endl;

    for (int i = 0; i < nDigMax; ++i) {
        int** matriz_aux = new int*[10];
        for (int j = 0; j < 10; ++j) {
            matriz_aux[j] = new int[n];
            for (int k = 0; k < n; ++k) {
                matriz_aux[j][k] = 0;
            }
        }
        int c[10]{0};
        //imprimirArreglo(c,10);

        for (int j = 0; j < n; ++j) {
            int digito = int(arreglo[j]/ pow(10,i)) % 10 ;
            matriz_aux[digito][c[digito]] = arreglo[j];
            c[digito]++;
            //cout<<"j: "<<j<<"\t numero: "<<arreglo[j]<<"\tdigito: "<<digito<<endl;

        }

        //imprimirMatriz(matriz_aux,10,n);
        //imprimirArreglo(arreglo,n);

        int p=0;
        if(orden == 1){
            for (int j = 9; j >= 0 ; --j) {
                for (int k = 0; k < c[j]; ++k) {
                    arreglo[p] = matriz_aux[j][k];
                    p++;
                }
            }
        }else{
            for (int j = 0; j < 10 ; ++j) {
                for (int k = 0; k < c[j]; ++k) {
                    arreglo[p] = matriz_aux[j][k];
                    p++;
                }
            }
        }

        //imprimirArreglo(arreglo,n);
    }

}

int main() {

    int arreglo[] = {1,0,12,55,14,123};
    int n = sizeof(arreglo)/sizeof(arreglo[0]);
    cout<<"Tam : "<<n<<endl;
    imprimirArreglo(arreglo,n);

    ordenamientoRadix(arreglo,n,1);

    imprimirArreglo(arreglo,n);




    return 0;
}
