<div align="center">
  
# PicoFlip X 
![header](https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-14%20212438.png?raw=true)

PicoFlip X is a compact RP2040 development board with a built-in IMU for motion tracking, there's also a humidity and temperature sensor! It has several status LEDs, buttons,...
</div>

## Key Features

- DevBoard powered by RP2040 chip
- Humidity and temperature sensor built right on the PCB
- 2 LEDs for visual feedback (PWR and RST)
- IMU - MPU 6050 to monitor the board's current position, all built-in
- USB-C connectivity
- 2-layer PCB, so it's cost-effective to manufacture!
- Modified GPIO pin layout and added one extra +3V3
- Custom silkscreen with images and descriptions

## Why I made this project?

When I finished my last project, I was thinking again about what I could do... I thought I'd try something hard and test my nerves... 💀
So I was looking and came up with this project - DEVBOARD!!


## Schema and PCB
  <div align="center">
    
Here is the circuit diagram!

<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-15%20212834.png?raw=true" alt="Diagram" width="75%"/>


Next, here is the PCB that is created in KiCad:
<div align="center">
  
<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-16%20182051.png?raw=true" alt="PCB Design" width="75%"/>
  
</div></div>

## The Design :)
  <div align="center">
    
Here is the top side of the PCB:

<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/image.png?raw=true " alt="Diagram" width="75%"/>


Also here is the bottom of the PCB!
<div align="center">
  
<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-16%20195745.png?raw=true" width="75%"/>
  
</div></div>

## JLCPCB Order
<div align="center">
  
<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-14%20201612.png?raw=true" width="75%"/>
<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-14%20182733.png?raw=true" width="75%"/>
  
</div>

## Bill of Materials

**Here is the complete BOM:**  

<details>
<summary>Click to expand!</summary>


| Top Designator | Comment | JLCPCB Part # | Product link | Lib Type | Qty | Source | Total Price ($) |
|---|---|---|---|---|---|---|---|
| C1,C10 | 1uF | C52923 | [Link](https://jlcpcb.com/partdetail/53938-CL05A105KA5NQNC/C52923) | Basic | 4 | 4 JLCPCB | 0,0132 |
| C2,C3,C4,C5,C6,C7,C8,C9,C11,C12,C17,C23 | 0.1uF | C1525 | [Link](https://jlcpcb.com/partdetail/1877-CL05B104KO5NNNC/C1525) | Basic | 32 | 32 JLCPCB | 0,0416 |
| C19,C21,C22,C24 | 100nF | ↑ | ↑ | ↑ | ↑ | ↑ | ↑ |
| C13,C14 | 10uF | C19702 | [Link](https://jlcpcb.com/partdetail/20411-CL10A106KP8NNNC/C19702) | Basic | 4 | 4 JLCPCB | 0,026 |
| C15,C16 | 33pF | C1562 | [Link](https://jlcpcb.com/partdetail/1914-0402CG330J500NT/C1562) | Basic | 4 | 4 JLCPCB | 0,0048 |
| C18,C25 | 10nF | C60133 | [Link](https://jlcpcb.com/partdetail/YAGEO-CC0402KRX7R9BB103/C60133) | Extended | 20 | 20 JLCPCB | 0,022 |
| C20 | 2.2uF | C12530 | [Link](https://jlcpcb.com/partdetail/13164-CL05A225MQ5NSNC/C12530) | Basic | 2 | 2 JLCPCB | 0,0052 |
| D3 | SK6812MINI | C7423117 | [Link](https://jlcpcb.com/partdetail/OPSCOOptoelectronics-SK6812MINIC/C7423117) | Extended | 5 | 5 JLCPCB | 0,428 |
| J1 | USB_C_Receptacle_USB2.0_14P | C165948 | [Link](https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M12/C165948) | Extended | 2 | 2 JLCPCB | 0,3624 |
| J2,J3 | Conn_01x20 | C50981 | [Link](https://jlcpcb.com/partdetail/51993-2_54_1_20P/C50981) | Extended | 4 | 4 JLCPCB | 0,4812 |
| J4 | Conn_01x03 | C49257 | [Link](https://jlcpcb.com/partdetail/50265-2_54_1_3P/C49257) | Extended | 4 | 4 JLCPCB | 0,0692 |
| PWR | POWER | C2286 | [Link](https://jlcpcb.com/partdetail/Hubei_KENTOElec-KT0603R/C2286) | Basic | 2 | 2 JLCPCB | 0,0128 |
| R1,R2 | 5.1K | C25905 | [Link](https://jlcpcb.com/partdetail/26648-0402WGF5101TCE/C25905) | Basic | 4 | 4 JLCPCB | 0,0032 |
| R3,R4 | 27 | C25100 | [Link](https://jlcpcb.com/partdetail/25843-0402WGF270JTCE/C25100) | Extended | 20 | 20 JLCPCB | 0,014 |
| R5,R6,R7 | 1K | C11702 | [Link](https://jlcpcb.com/partdetail/12256-0402WGF1001TCE/C11702) | Basic | 6 | 6 JLCPCB | 0,0042 |
| R8,R9 | 4.7K | C25900 | [Link](https://jlcpcb.com/partdetail/26643-0402WGF4701TCE/C25900) | Basic | 4 | 4 JLCPCB | 0,0032 |
| R10 | 10K | C25744 | [Link](https://jlcpcb.com/partdetail/26487-0402WGF1002TCE/C25744) | Basic | 2 | 2 JLCPCB | 0,0016 |
| R11,R12 | 680 | C25130 | [Link](https://jlcpcb.com/partdetail/25873-0402WGF6800TCE/C25130) | Extended | 20 | 20 JLCPCB | 0,016 |
| RST | RUN | C2288 | [Link](https://jlcpcb.com/partdetail/Hubei_KENTOElec-KT0603B/C2288) | Extended | 20 | 20 JLCPCB | 0,198 |
| SW1,SW2 | SW_Push | C720477 | [Link](https://jlcpcb.com/partdetail/XUNPU-TS_1088AR02016/C720477) | Basic | 4 | 4 JLCPCB | 0,1904 |
| U1 | RP2040 | C2040 | [Link](https://jlcpcb.com/partdetail/RaspberryPi-RP2040/C2040) | Extended | 2 | 2 JLCPCB | 1,9318 |
| U2 | MCP1700x-330xxTT | C39051 | [Link](https://jlcpcb.com/partdetail/MicrochipTech-MCP1700T_3302ETT/C39051) | Extended | 5 | 5 JLCPCB | 1,807 |
| U4 | SHT4x | C2848306 | [Link](https://jlcpcb.com/partdetail/Sensirion-SHT40_AD1BR3/C2848306) | Extended | 2 | 2 JLCPCB | 3,427 |
| U5 | W25Q16JVZPIQTR | C2843335 | [Link](https://jlcpcb.com/partdetail/WinbondElec-W25Q16JVUXIQ/C2843335) | Extended | 2 | 2 JLCPCB | 2,3964 |
| U6 | MPU-6050 | C24112 | [Link](https://jlcpcb.com/partdetail/TDKInvenSense-MPU6050/C24112) | Extended | 2 | 2 JLCPCB | 15,7754 |
| Y1 | 12MHz | C9002 | [Link](https://jlcpcb.com/partdetail/YXC_CrystalOscillators-X322512MSB4SI/C9002) | Basic | 2 | 2 JLCPCB | 0,1452 |
| PCBA (Parts + Assembly) |  |  |  |  |  |  | 65,32 |
| PCB (Black) |  |  |  |  |  |  | 4 |
| Shipping (GSDL) |  |  |  |  |  |  | 1,5 |
| TOTAL |  |  |  |  |  |  | 70,82 |

The bill of material is also available here: [BOM.csv](https://github.com/mavory/PicoFlip-X/blob/bba36edf56afa61a020f22f13432fc22c765aea1/BOM.csv)

</details>

<hr>

> Made with ❤️ - by [@mavory](https://github.com/mavory) | Also thank you for providing the guide [@Kai Pereira](https://github.com/kaipereira)! 
