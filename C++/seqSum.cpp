# include <iostream>
# include <cassert>

int kthNumber(int k)
{
    if(k==0){
        return 0;
    }else if(k==1){
        return 1;
    }else{
        return kthNumber(k-1) + (2*kthNumber(k-2));
    };
}

int seqSum(int k)
{
    int sum = 0;
    int kEntries [k+1];
    for(int i = 0; i<=k;i++){
        kEntries[i] = kthNumber(i);
    };
    for(int j = 0; j<= k; j++){
        sum += kEntries[j];
    };
    return sum;
}

int extendedSeqSum(int k)
{
    int sum = kthNumber(k);
    return seqSum(sum);
}

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);
    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(3)==5);

    std::cout << "Success!";

    return 0;
}