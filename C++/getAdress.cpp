# include <iostream>
# include <cassert>

int main()
{
    int arr[4] = {11, 12, 13, 14};
    std::cout << "array has address ";
    std::cout << &arr;
    std::cout << "\n";
    for(int i = 0; i <= 3; i++){
        std::cout << "index ";
        std::cout << i;
        std::cout << " has value ";
        std::cout << arr[i];
        std::cout << " and adress ";
        std::cout << &arr[i];
        std::cout << "\n";
    };

    return 0;
}