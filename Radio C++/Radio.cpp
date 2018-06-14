#include "../Si4703_Breakout.h"
#include <stdio.h>

int main()
{
        int resetPin = 23; //GPIO_23
        int sdaPin = 0; //GPIO_0 (SDA)

        Si4703_Breakout radio(resetPin, sdaPin);
        radio.powerOn();
        radio.setVolume(5);
        radio.setChannel(1036); //FM 103.6Mhz Radio Hamburg
        
        char rdsBuffer[10] = {0};
        radio.readRDS(rdsBuffer, 15000); //timeout 15sec
        printf("Listening to station: %s %.1f\n", rdsBuffer, radio.getChannel()/10.0);

        radio.printRegisters();

        return 0;
}