# include <iostream>
# include <cassert>

int seqSum(int n)
{
    int terms[n+1];
    terms[0] = 0;
    terms[1] = 1;

    for(int i = 2; i<=n;i++){
        terms[i] = terms[i-1] + 2*terms[i-2];
    };

    int sum = 0;
    for(int i = 0; i <= n; i++){
        sum += terms[i];
    };

    return sum;
}


int extendedSeqSum(int n)
{
    int terms[n+1];
    terms[0] = 0;
    terms[1] = 1;

    for(int i = 2; i<=n;i++){
        terms[i] = terms[i-1] + 2*terms[i-2];
    };

    int val_of_n_term = terms[n];

    int extendedTerms[val_of_n_term+1];

    for(int i = 0; i<=val_of_n_term;i++){
        if(i < n){
            extendedTerms[i] = terms[i];
        }else{
            extendedTerms[i] = extendedTerms[i-1] + 2*extendedTerms[i-2];
        };
        
    };

    int sum = 0;
    for(int i = 0; i <= val_of_n_term; i++){
        sum += extendedTerms[i];
    };

    return sum;
}

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);
    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(3)==5);
    std::cout << extendedSeqSum(4);
    std::cout << "Success!";

    return 0;
}