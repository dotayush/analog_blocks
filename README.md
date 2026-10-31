### analog blocks.

This project was written to create a mathematical description of
analog electronic blocks used in various applications such that
a designer or an engineer can reference/use the model without
having to rigrously analyse every block from scratch. This is
**a continuously evolving project and will be updated as new blocks
are added and existing block descriptions are improved**.

I intend to minimise the textual description and maximise the
mathematical description. If you can read mathematics, you will be
able to understand the block.


### access.

Look at the [release page](../../releases) to download the latest
compiled version of the project. You can also build this project
from source by compiling `main.tex` using `pdflatex` or `xelatex`.
The project is written in LaTeX and requires a LaTeX distribution
to compile.

### license.

This project is licensed under the CC BY-NC-SA 4.0 license. You can
read the full license [here](./LICENSE.md).

### structure.

```
main.tex, preamble.tex
00_Introduction/   preface, organisation, notation
01_Analysis/       octant system of circuit analysis
02_Devices/        Passives/ (R, C, L, Diode), Actives/ (BJT, MOSFET, Op-Amp)
03_General/        Voltage_Dividers/, Current_Dividers/
04_Filters/        Passive/ (Single_Pole, Double_Pole), Active/
05_Current_Mirrors/ Basic, Widlar, Wilson, Modified Wilson, Cascode
06_Amplifiers/     Common/, Functional/, Differential/
07_Data_Converters/ Characterisation, DAC/, ADC/
08_PLL_VCO/        phase detectors, charge pump, PLL, VCOs
09_RF/             reserved
10_Electromech/    Motors/
AX_Theory/         appendix: General/, Control_Systems/, EM/
```
