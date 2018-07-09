#include "../Si4703_Breakout.h"
#include <stdio.h>
#include "Radio.cpp"
 
int main()
{
        int resetPin = 23; //GPIO_23
        int sdaPin = 0; //GPIO_0 (SDA)

		channelSelect(false);
        Si4703_Breakout radio(resetPin, sdaPin);
        radio.powerOff();
        //radio.setVolume(5);
        //radio.setChannel(1036); //FM 103.6Mhz Radio Hamburg
        
        //char rdsBuffer[10] = {0};
        //radio.readRDS(rdsBuffer, 15000); //timeout 15sec
        printf("Radio aus");

        //radio.printRegisters();
		
        return 0;
}