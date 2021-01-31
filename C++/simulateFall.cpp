#include <iostream>
#include "constants.h"

double calculateDistanceFallen(int seconds)
{
    // approximate distance fallen in the next second
    double distanceFallen = myConstants::gravity * seconds * seconds / 2;

    return distanceFallen;
}

void printStatus(int time, double height)
{
    std::cout << "At " << time
    << " seconds, the ball is at height "
    << height << " meters\n";
}

int main()
{
    using namespace std;
    cout << "Enter the initial height of the tower in meters: ";
    double initialHeight;
    cin >> initialHeight;
    double currentHeight = initialHeight;
    int t = 0;
    
    while(currentHeight >0){
        currentHeight = initialHeight - calculateDistanceFallen(t);
        if(currentHeight < 0){
            currentHeight = 0;
        }
        printStatus(t, currentHeight);
        t++;
    }

    return 0;
}