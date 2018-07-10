#include "../Si4703_Breakout.h"
#include <stdio.h>

int main() {
	//Variabeln
	int selectStation =0;
	int volume =7;
	int resetPin = 23; //GPIO2_3
	int sdaPin =0; //GPIO0_0
	Si4703_Breakout radio (resetPin, sdaPin);
	
	//radio init
	radio.powerOn();
	radio.setVolume(volume);
	radio.setChannel(1036);	//Radio Hamburg, nicht Studio
	
	char rdsBuffer[10] = {0};
	radio.readRDS(rdsBuffer, 15000); // timeout
	
	
	//Daten aus geben für Konsole 
	printf (Listening to station: %s %.lf\n", rdsBuffer, radio.getChannel()/10.0);
	radio.printRegisters();
	
	//quittiere
	return 0;
	



}