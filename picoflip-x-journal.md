
2/14/2026 9 PM - The beginning of my project!!
Time spent: 2.1h
When I finished my last project, I was thinking again about what I could do... I thought I'd try something hard and test my nerves... 💀
So I was looking and came up with this project - DEVBOARD!! I started to gradually make and create a diagram. When I had most of it done, I needed something to make my DevBoard special, to make it unique!
I stopped thinking and went to do something. I opened KiCad and started inserting all the components and connecting them according to the instructions. It went pretty well, but I got stuck on a few things for a while because I had never encountered them before.

![Snímek obrazovky 2026-02-09 183541](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTU5LCJwdXIiOiJibG9iX2lkIn19--d230666c21b6d22bb9a6613d9ccfda594eb417b5/Sn%C3%ADmek%20obrazovky%202026-02-09%20183541.png)

2/14/2026 10:01 PM - Adding custom components
Time spent: 1.8h
I kept adding more and more things and I was slowly getting it done. But then I remembered that I wanted to add something! I decided to go for the ICM-20602 and SHT4x first.

![Snímek obrazovky 2026-02-10 201901](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTcxLCJwdXIiOiJibG9iX2lkIn19--8f91ccb51b20f87e2a1e6f4ece08eb8aaeeeb009/Sn%C3%ADmek%20obrazovky%202026-02-10%20201901.png)

So I put them in the program and started researching how to connect it... I've never worked with them before, so that was probably the hardest part for me so far. I also had to do some research on how these things are connected and I decided to connect the ICM via I2C!! I gradually started adding resistors and other things and after a long time I had it connected with all the things :)

![Snímek obrazovky 2026-02-10 204240](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTY5LCJwdXIiOiJibG9iX2lkIn19--2090bd2ab9034c33a9b24806ddbbf3ff68cea73e/Sn%C3%ADmek%20obrazovky%202026-02-10%20204240.png)

2/14/2026 10:12 PM - Schema editing
Time spent: 1.4h
Right after adding the sensors I thought I would like to add 2 LEDs for indication and 1 neopixel that would be programmable via GPIO25! So I was looking for some components to make them small but powerful.
I decided on WS2818B-2020 and normal SMD LEDs. I immediately prepared them and added them to the work surface. But I thought for a while how I could use the LEDs and what they would indicate. I told myself that it would be best if I chose this:
1st LED - POWER indicator
2nd LED - RESET indicator
So I started looking again how to connect them and it went pretty quickly, so I had time to redo a few things.

![Snímek obrazovky 2026-02-11 172207](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTkzLCJwdXIiOiJibG9iX2lkIn19--e0363d5ddd840c7d305321f8b59cd58e830c0d73/Sn%C3%ADmek%20obrazovky%202026-02-11%20172207.png)

2/14/2026 10:19 PM - Pin assignment
Time spent: 0.6h
I was thinking about how I would make the pins on my DevBoard... So I started experimenting and at first the pins didn't fit at all, so I started redoing it and said to myself that I'd better add another 3v3 on one side for some reason, because as I know myself, it will definitely come in handy in the future :)
So I already arranged the pins well and where there was space left, I put GND.

![Snímek obrazovky 2026-02-11 185952](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTk1LCJwdXIiOiJibG9iX2lkIn19--421f40cbe782fbb7682f9f9bc1977ecf2f7f961c/Sn%C3%ADmek%20obrazovky%202026-02-11%20185952.png)

2/14/2026 10:29 PM - Editing a KiCad project
Time spent: 1.7h
Before I start assigning cases, I made parts of all the things so that I can understand them later and read the schematic better when, for example, I make a PCB.
I didn't know where to do it at all, so I had to look up where to make the border and then I found out that it's normally a rectangle... 🧑‍🦽
So it went pretty quickly, but I had to play around with it to get everything to fit so well.

![Snímek obrazovky 2026-02-11 194257](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjA0LCJwdXIiOiJibG9iX2lkIn19--1e5753ebc6366fc8c2ff2805f6ddb3da1b42fe96/Sn%C3%ADmek%20obrazovky%202026-02-11%20194257.png)

Assigning cases
As I wrote earlier, I started working on the cases. First, I marked all the same capacitors and gradually assigned them. I did the same with other things. It was the kind of thing that I didn't enjoy at all, but I had to do it anyway so that it would work well later.

![Snímek obrazovky 2026-02-11 203945](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjEwLCJwdXIiOiJibG9iX2lkIn19--bee80eaf9d68256613dcccaa30359a3e3e14c57d/Sn%C3%ADmek%20obrazovky%202026-02-11%20203945.png)

2/14/2026 10:40 PM - Getting started with PCB design!
Time spent: 3.6h
After checking everything to make sure I wasn't missing anything, I ran the rules check test again and there were no errors that would jeopardize my project. So I could move on to the PCB itself.
I imported all the stuff and started connecting everything. I told myself several times that I would never be able to do it and that it would be terrible (it happened).
But I continued with the connections, which was really difficult for me.
Several times I had to delete several paths so that I could run another important wire and then re-draw the ones I had deleted. Well... it was very difficult, but I don't know how I managed to do it. I think I could do it even better next time, but for my first PCB that is difficult for me, I'm glad I connected everything at all.

![Snímek obrazovky 2026-02-13 151409](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjE4LCJwdXIiOiJibG9iX2lkIn19--610d4386c1f125475d9b18e2422b7452da8e5a97/Sn%C3%ADmek%20obrazovky%202026-02-13%20151409.png)

2/14/2026 10:51 PM - Error correction
Time spent: 1.2h
I didn't think it would be error-free at all, so I immediately opened DRC and started redoing things that were badly connected, somewhere it touched the connections of some components to each other, but I solved that.

![Snímek obrazovky 2026-02-13 151652](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjIzLCJwdXIiOiJibG9iX2lkIn19--37f44e3aaffada6ef9074581d8fd04521597baab/Sn%C3%ADmek%20obrazovky%202026-02-13%20151652.png)

Unfortunately, ICM-20602 was still annoying me and I didn't know why... So I did some research and found out that I had to modify KiCad so that it wouldn't be so strict with this component. So I modified it and then all that was left was to pour the board, with copper.

![Snímek obrazovky 2026-02-13 153254](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MjI0LCJwdXIiOiJibG9iX2lkIn19--de977ca282cfc5c252d8ff65a870d0ca5d6ddcaa/Sn%C3%ADmek%20obrazovky%202026-02-13%20153254.png)

2/15/2026 4:19 PM - Silkscreen creation
Time spent: 0.9h
When I was sure I could continue, I decided to go straight to silkscreen.
I created all the necessary things like:
A QR code that has the URL to my GitHub project
A name I chose "PicoFlip X" or PFX for short
I also added my nickname at the bottom
On the top I put my own images that I created and I wanted some smaller images:

![Snímek obrazovky 2026-02-13 215404](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0ODA3LCJwdXIiOiJibG9iX2lkIn19--2f41a8da229d7b66cdfc9646cfa7261398ff0690/Sn%C3%ADmek%20obrazovky%202026-02-13%20215404.png)

Silkscreen editing
So I continued importing the images and I also had to resize them somehow, so that took me a while. Then I had to put them on the PCB and play around with the layout and here is the bottom:

![Snímek obrazovky 2026-02-13 221942](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0ODA5LCJwdXIiOiJibG9iX2lkIn19--da59126d823ed60189ebf4bb98d7412f81f53815/Sn%C3%ADmek%20obrazovky%202026-02-13%20221942.png)

2/15/2026 4:44 PM - JLCPCB wants a lot of money from me...
Time spent: 0.7h
I started making tables and all the exports for the production of the JLCPCB board and when I was making tables, it was still quite good... Then I compressed all the files into a .ZIP file and uploaded it to the site. What I was afraid of came - they wanted me to choose a PCBA standard, because components like neopixel, ICM were only installed in the standard.
So I came across this huge problem of mine and said to myself that I would redo it rather than submit with about 100 dollars.

![Snímek obrazovky 2026-02-13 233512](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA0ODE5LCJwdXIiOiJibG9iX2lkIn19--09e3341ead9aa7f6313fdeddc2987f9f831f88c6/Sn%C3%ADmek%20obrazovky%202026-02-13%20233512.png)

2/15/2026 10:20 PM - Schema reworking
Time spent: 1.0h
So I had to choose some better components and I decided as follows:
Instead of ICM I will use MPU 6050
Instead of WS2812B I will use SK6812.
So I found the parts in KiCad and started to modify... But I still had to check if JLCPCB really assembles it in economic PCBA - and it does, so I could celebrate!!!

![sn__mek_obrazovky_2026-02-14_133024](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA1MDY0LCJwdXIiOiJibG9iX2lkIn19--a921d2478ecc93ef447bfc1f20a381cdaa91832d/sn__mek_obrazovky_2026-02-14_133024.png)

2/15/2026 10:28 PM - PCB editing
Time spent: 1.6h
So I started connecting all the components together and it went pretty well, except for a few things where I had to think a little more.
Next I poured copper all over the board, but in some places the copper didn't pour properly, so I had to connect the components manually. This was more difficult for me, but I managed it.
So I continued with silkscreen, because in some places the components were placed differently and would interfere with it. I also rewrote the LEDs so that in the future I would know what each of them indicates.

![image-1](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA1MDY2LCJwdXIiOiJibG9iX2lkIn19--d4c22be2f7b8f0bd04abc36acb4824fca1d1723f/image-1.png)

2/15/2026 10:51 PM - JLCPCB
Time spent: 1.9h
Right after everything I decided to export and create a spreadsheet for JLCPCB. First I had to remember where everything was and save it all in one folder. Then I continued with the production files, which I compressed into a .ZIP folder and I had this ready.
I put everything on the website and had to edit everything manually, because unfortunately I had a stupid table. I also had to look for what parts to use for my components and that took me a lot of time.
So I chose a black PCB and then I dealt with installing 2 minimal PCBs!

![sn__mek_obrazovky_2026-02-14_182733](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTA1MDY4LCJwdXIiOiJibG9iX2lkIn19--e699be1968b1433ad34b56723be97a79972963e0/sn__mek_obrazovky_2026-02-14_182733.png)

So everything comes out to about 71 dollars, even with shipping. Which is very good, considering the previous price!
2/16/2026 - PicoFlip X
Time spent: 2.5h

![header](https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-14%20212438.png?raw=true)

PicoFlip X is a compact RP2040 development board with a built-in IMU for motion tracking, there's also a humidity and temperature sensor! It has several status LEDs, buttons,...

Key Features
DevBoard powered by RP2040 chip
Humidity and temperature sensor built right on the PCB
2 LEDs for visual feedback (PWR and RST)
IMU - MPU 6050 to monitor the board's current position, all built-in
USB-C connectivity
2-layer PCB, so it's cost-effective to manufacture!
Modified GPIO pin layout and added one extra +3V3
Custom silkscreen with images and descriptions
Why I made this project?
When I finished my last project, I was thinking again about what I could do... I thought I'd try something hard and test my nerves... 💀
So I was looking and came up with this project - DEVBOARD!!

Schema and PCB
Here is the circuit diagram!

<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-15%20212834.png?raw=true" alt="Diagram" width="75%"/>

Next, here is the PCB that is created in KiCad:

<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-16%20182051.png?raw=true" alt="PCB Design" width="75%"/>

The Design :)
Here is the top side of the PCB:

<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/image.png?raw=true " alt="Diagram" width="75%"/>

Also here is the bottom of the PCB!

<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-16%20195745.png?raw=true" width="75%"/>

JLCPCB Order

<img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-14%20201612.png?raw=true" width="75%"/> <img src="https://github.com/mavory/PicoFlip-X/blob/main/Photos/Sn%C3%ADmek%20obrazovky%202026-02-14%20182733.png?raw=true" width="75%"/>

Bill of Materials
Here is the complete BOM:
Top Designator	Comment	JLCPCB Part #	Product link	Lib Type	Qty	Source	Total Price ($)
C1,C10	1uF	C52923	Link	Basic	4	4 JLCPCB	0,0132
C2,C3,C4,C5,C6,C7,C8,C9,C11,C12,C17,C23	0.1uF	C1525	Link	Basic	32	32 JLCPCB	0,0416
C19,C21,C22,C24	100nF	↑	↑	↑	↑	↑	↑
C13,C14	10uF	C19702	Link	Basic	4	4 JLCPCB	0,026
C15,C16	33pF	C1562	Link	Basic	4	4 JLCPCB	0,0048
C18,C25	10nF	C60133	Link	Extended	20	20 JLCPCB	0,022
C20	2.2uF	C12530	Link	Basic	2	2 JLCPCB	0,0052
D3	SK6812MINI	C7423117	Link	Extended	5	5 JLCPCB	0,428
J1	USB_C_Receptacle_USB2.0_14P	C165948	Link	Extended	2	2 JLCPCB	0,3624
J2,J3	Conn_01x20	C50981	Link	Extended	4	4 JLCPCB	0,4812
J4	Conn_01x03	C49257	Link	Extended	4	4 JLCPCB	0,0692
PWR	POWER	C2286	Link	Basic	2	2 JLCPCB	0,0128
R1,R2	5.1K	C25905	Link	Basic	4	4 JLCPCB	0,0032
R3,R4	27	C25100	Link	Extended	20	20 JLCPCB	0,014
R5,R6,R7	1K	C11702	Link	Basic	6	6 JLCPCB	0,0042
R8,R9	4.7K	C25900	Link	Basic	4	4 JLCPCB	0,0032
R10	10K	C25744	Link	Basic	2	2 JLCPCB	0,0016
R11,R12	680	C25130	Link	Extended	20	20 JLCPCB	0,016
RST	RUN	C2288	Link	Extended	20	20 JLCPCB	0,198
SW1,SW2	SW_Push	C720477	Link	Basic	4	4 JLCPCB	0,1904
U1	RP2040	C2040	Link	Extended	2	2 JLCPCB	1,9318
U2	MCP1700x-330xxTT	C39051	Link	Extended	5	5 JLCPCB	1,807
U4	SHT4x	C2848306	Link	Extended	2	2 JLCPCB	3,427
U5	W25Q16JVZPIQTR	C2843335	Link	Extended	2	2 JLCPCB	2,3964
U6	MPU-6050	C24112	Link	Extended	2	2 JLCPCB	15,7754
Y1	12MHz	C9002	Link	Basic	2	2 JLCPCB	0,1452
PCBA (Parts + Assembly)							65,32
PCB (Black)							4
Shipping (GSDL)							1,5
TOTAL							70,82
The bill of material is also available here: BOM.csv
</details>
<hr>
> Made with ❤️ - by [@mavory](https://github.com/mavory) | Also thank you for providing the guide [@Kai Pereira](https://github.com/kaipereira)! 

3/28/2026 10:22 AM - The package has arrived!!!
Time spent: 0.5h
After a long time I can say that I was not so excited! After about 2 weeks I have the package from JLCPCB with me. I opened everything that day and everything looks very good!

![1000027293](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MDY5LCJwdXIiOiJibG9iX2lkIn19--c31c59ec652bb120abe6d6405cfe2b8e64e494ee/1000027293.jpg)

I couldn't wait and went to try the DevBoard right away. I connected it and everything worked very well. I just had to change the USB driver to CDC via the Zadig application so that it would be recognized properly in the Thonny program/Arduino IDE.

![Snímek obrazovky 2026-03-28 101224](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MDcxLCJwdXIiOiJibG9iX2lkIn19--4eddcb4a178d8cd70c3bca402c764df8a334668c/Sn%C3%ADmek%20obrazovky%202026-03-28%20101224.png)

Then it was a breeze and I was able to prepare my Board for soldering.
3/28/2026 10:48 AM - Soldering :)
Time spent: 0.7h
I decided to use colored DuPont headers and I think it looks pretty good!
So I started slowly soldering each part and after soldering the side headers I jumped on the debug header and chose yellow for it.

![20260328_102939(0)](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MDczLCJwdXIiOiJibG9iX2lkIn19--401969fd13d1d3e4cedecbcefbef5375a35fef76/20260328_102939(0).jpg)

I should have finished it in less than half an hour and then I just cleaned the board and prepared it for testing with components.

![20260328_102952](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MDc0LCJwdXIiOiJibG9iX2lkIn19--8cc0152a150be97b25c93cbf83a430ea27dd0d96/20260328_102952.jpg)

3/28/2026 1 PM - Project completion
Time spent: 1.2h
Then I started working on the code, where I wanted to test the main things:
If the neopixel works at all
If the sensors send the correct data
If the GPIO works and if the text on the OLED display is displayed correctly
So I had the preparation ready and started writing the code. After a while I had it ready and decided that I would do it in Thonny. It was a completely new program for me, but I easily got used to it, so I appreciated that. I also added a print to the Serial monitor so I could watch it and also test if it works.

![image](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MTQwLCJwdXIiOiJibG9iX2lkIn19--4b447e855a217c8021045d2cfdf5ed6a3ca195a8/image.png)

After a while I decided to run it and I must say that everything works PERFECTLY!

![20260328_125100](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MTQxLCJwdXIiOiJibG9iX2lkIn19--00eaec1e6190379d6f65966331ea0e978b61badc/20260328_125100.jpg)
