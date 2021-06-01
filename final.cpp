# include <iostream>
# include <cassert>

int sumPerfectCubes(int n){
    int cubes[n];
    for(int i = 1; i<= n; i++){
        cubes[i] = i*i*i;
    };


    int sum = 0;
    for(int i = 0; i <= n; i++){
        sum += cubes[i];
    };

    return sum;
}

int main(){
    std::cout << "Testing...\n";
    std::cout << sumPerfectCubes(10);
    std::cout <<"\n";
    std::cout << "Success!";

    return 0;
}
