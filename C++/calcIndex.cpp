# include <iostream>
# include <cassert>

int calcIndex(int n){
    int terms[n+1];
    int last_term = 0;
    terms[0] = 0;
    terms[1] = 1;

    for(int i = 2; i<=n;i++){
        terms[i] = terms[i-1] + terms[i-2];
        if(terms[i] > n){
            last_term = i;
            break;
        }
    };

    return last_term;
}

int main()
{
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}