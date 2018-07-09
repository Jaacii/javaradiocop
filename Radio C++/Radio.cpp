#include "../Si4703_Breakout.h"
#include <stdio.h>

int main()
{
		int selectStation = 0;
		int volume = 5;
        int resetPin = 23; //GPIO_23
        int sdaPin = 0; //GPIO_0 (SDA)

        Si4703_Breakout radio(resetPin, sdaPin);
        radio.powerOn();
        volumeChange(0);
		
		channelSelect(true);
        //radio.setChannel(1036); //FM 103.6Mhz Radio Hamburg
        
        char rdsBuffer[10] = {0};
        radio.readRDS(rdsBuffer, 15000); //timeout 15sec
       // printf("Listening to station: %s %.1f\n", rdsBuffer, radio.getChannel()/10.0);

        radio.printRegisters();

        return 0;
}

void channelSelect(boolean radioON) {
	
	
	if (radioON == true){
		
	
		if (selectStation == 0) {	//radio HH
		radio.setChannel(1036);
	
		printf("Listening to station: Radio Hamburg");
		selectStation++;
		}
		else if  (selectStation == 1) {	//Nrd?
		radio.setChannel(876);
	
		printf("Listening to station: Ndr2");
		selectStation++;
		}
	
		else {
		radio.setChannel(942);		//N joy
		
		printf("Listening to station: NJoy");
		selectStation = 0;
		}
	
	} else {				//Damit das Radio den selben Sender beim An- wie vor dem Ausschalten hat wird, hier Stationselect-1 ausgeführt.
		selectStation--;
	}
	return 0;
	
}

void volumeChange(int changer) {
	int changer = this.changer;
	
	if (changer == 0) {						// simple setVolume
		radio.setVolume(volume);
	}
	else if (changer == 1) {
		volume = volume + 5;
		radio.setVolume(volume);			//+ Volume
	}
	else (changer == 2) {					//- Volume
		volume = volume - 5;
		radio.setVolume(volume);
	}
	return 0;
}