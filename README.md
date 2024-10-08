# PiExp
Expansion board for Raspberry Pi ZERO

More info TK

Testing board design:
![alt text](https://github.com/Sd4Projects/PiExp/blob/main/PiExpTestSetup.png?raw=true "finishedboard")

Top view of board:
![alt text](https://github.com/Sd4Projects/PiExp/blob/main/PiExpTop.png?raw=true "TopView")

Bottom view of board:
![alt text](https://github.com/Sd4Projects/PiExp/blob/main/PiExpBot.png?raw=true "BottomView")

Schematic PDF file: PiExp_v1b.Schematic.pdf

Board PDF file: PiExp_v1b.Board.pdf

BOM PDF file: PiExp_v1b.BOM.pdf

Designed with KiCad Version 8.0.4

PiExp source files included.

Licensed under CERN OHL v.1.2

See CERN OHL v.1.2 for applicable conditions

http://ohwr.org/cernohl

PiExp board features:
1. Four 16bit AtoD lines using an ADS1115 chip via I2C interface
2. Two GPIO pins driving 2N7002 Mosfets for output.
3. I2C lines to a JST_SH Connector
4. SPI lines to a JST_SH Connector
5. UART (Serial) lines to a JST_SH Connector
6. 1-Wire line to a JST_SH Connector (optional 4.7K pull up)
7. 24CS256 EEPROM with solder pads to link I2C of choice
8. Terminal to supply external 5 volts to PI

All data lines use 4-pin Qwiic/JST_SH connectores.

This board started out because I needed to add AtoD for my Raspberry Pi Zero W2 for a project I was working on and then I just keep adding features to the board till it was full.
