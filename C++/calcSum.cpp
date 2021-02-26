#include <iostream>
#include <cassert>

int calcSum(int m, int n){
    int asc[m][n];
    int desc[n][m];
    int product[m][m];

    for(int j = 0; j <n; j++){
        for(int k =0; k < m; k++ ){
            asc[k][j] = 1+j+k*n;
            desc[j][k] = m*n - k - j*m;
        };
    };

    int sum = 0;

    for(int i=0; i<m; i++){
        for(int j=0; j<m; j++){
        int dotProduct = 0;
        for(int k=0; k<n; k++){
            dotProduct += asc[i][k]*desc[k][j];
        }; 
        product[i][j] = dotProduct;
        sum += product[i][j];
        };

    };

    return sum;
}


int main(){
    std::cout << "Testing...\n";
    std::cout << calcSum(2,3);
    std::cout << "\n";
    assert(calcSum(2,3)==131);
    std::cout << "Success!";
}