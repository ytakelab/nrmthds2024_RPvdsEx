# NiDaqControlPanel
MATLAB GUI for controlling National Instruments data acquisition boards

## Getting Started

### Prerequisites
- [RX8 MULTI-I/O PROCESSOR (Tucker-Davis Technologies)](http://www.ni.com/data-acquisition/)
- [TDT Drivers/RPvdsEx (Tucker-Davis Technologies)](https://www.tdt.com/support/downloads/)
- Recording controller such as [RHD recording controller (Intan Technologies)](RHD 512-channel recording controller) and [Open Ephys Acquisition Board (Open Ephys)](https://open-ephys.org/acq-board) and corresponding software such as [RHX Data Acquisition Software (Intan Technologies)](https://intantech.com/downloads.html?tabSelect=Software) and [Open Ephys GUI (Open Ephys)](https://open-ephys.org/gui)

The code has been tested with a TDT Drivers/RPvdsEx ver 98 (updated at 08/21/2023).

### Installing
* Install TDT Drivers/RPvdsEx.
* Connect your RX8 MULTI-I/O PROCESSOR to your PC.
* Connect the Analog Input Port of RX8 to analog output of the recording controller and Digital Output Port of RX8 to digital input of the recording controller.

### How to use
1. Make sure that the recording controller is outputting an analogue signal to the Analog Input Port of RX8.
2. Turn on the RX8.
3. Launch RPvdsEx.
4. Open Theta_detection.rcx.
5. Run the code by clicking the "Build, Load and Run" in the "Implement" tub in the menu bar.
6. Launch the code by making the trigger of "TrgIn" component in the main tub high using Software trigger 1 command.
![Launching the code](\tdt_launch_code.png){#fig:fg1}

## Help
Refer the documents below for further manuals.
- [RPvdsEx Manual](https://www.tdt.com/files/manuals/RPvdsEx_Manual.pdf)

## Releases
* Ver 1.0.0, 2024/04/01: The first release.

## Authors
### Yuichi Takeuchi
- Department of Biopharmaceutical Sciences and Pharmacy, Faculty of Pharmaceutical Sciences, Hokkaido University, Sapporo 060-0812, Japan
- Tel: +81-11-706-3248
- Fax: +81-11-706-4987
- E-mail: ytake@pharm.hokudai.ac.jp
- [GitHub](https://github.com/yuichi-takeuchi)

# Acknowledgments
We thank Masabumi Minami for fruitful discussion.
This work was supported by KAKENHI (22H04762, 23H02790), AMED (23gm6510015h002, 22zf0127004h002), Takeda Science Foundation, Takahashi Industrial and Economic Research Foundation, The Asahi Glass Foundation, Casio Science Promotion Foundation, Shimadzu Science Foundation, The Japan Epilespy Research Foundation, and Brain Science Foundation to Y.T.
