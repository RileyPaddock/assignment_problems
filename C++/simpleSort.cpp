# include <iostream>
# include <cassert>



int main()
{
    std::cout << "Testing...\n";
    int array[5]{ 30, 50, 20, 10, 40 };

    bool incomplete = true;
    int least = array[0];
    int least_index = 0;
    int swap_index = 0;

    while(incomplete){
        int count = 0;

        for(int i = swap_index; i<=4; i++){
            if(array[i] < least){
                least = array[i];
                least_index = i;               
            }else{
                count++;
            };
        };

        if(count >= 5){
            incomplete = false;
        }else{

            array[least_index] = array[swap_index];
            array[swap_index] = least;
            

            if(swap_index < 4){
                swap_index++;
            }else{
                swap_index = 0;
            };
            least = array[swap_index];
        };

        
    };


    assert(array[0]==10);
    assert(array[1]==20);
    assert(array[2]==30);
    assert(array[3]==40);
    assert(array[4]==50);

    std::cout << "Succeeded";

    return 0;
}