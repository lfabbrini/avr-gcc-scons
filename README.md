# avr-gcc-scons
## Bare Metal Arduino Building with Scons


This repository aims to create a very clear and easy way to build your Arduino projects (and flash it - see the ```task.json``` command examples), with the possibility to control up to the very last building flag.

If you - as me - have got yourself lost from the plug and play philosophy which hides all the building details (the verbose flag is not even the default one) and you need a way to get the control back, well, this repository could be the answer.

## Installation

```sh
$ cd avr-gcc-scons
$ pip install -r requirements.txt
```

## Building the project

```sh
$ cd avr-gcc-scons
$ scons -j4
```

## Flashing a program
the examples reported are in Windows, but the steps to adjust them to other OS should be easy

### with Command Line

Arduino UNO
```sh
$ <path_to_avrdude>bin/avrdude -C<path_to_avrdude>etc/avrdude.conf -v -patmega328p -carduino -P<your_COM> -b115200 -D -Uflash:w:<path_to_avr_gcc_scons>\\build\\appl\\uno\\helloworld\\helloworld.hex:i
```

Arduino NANO Every
```sh
$ mode <your_COM> baud=12 dtr=on > nul && mode <your_COM> baud=12 dtr=off > nul && <path_to_avrdude>bin/avrdude -C<path_to_avrdude>etc/avrdude.conf -v -patmega4809 -cjtag2updi -P<your_COM> -b115200 -e -D -Uflash:w:<path_to_avr_gcc_scons>\\build\\appl\\nanoevery\\blink\\blink.hex:i -Ufuse2:w:0x01:m -Ufuse5:w:0xC9:m -Ufuse8:w:0x00:m {upload.extra_files}
```
> *NOTE*: mode ```<your_COM>``` baud=12 dtr=on > nul && mode ```<your_COM>``` baud=12 dtr=off > nul is used to reset the COM port in order to make Arduino Nano Every to stay in the Bootloader so to receive the commands from ```avrdude```

### with VSCODE
Under the hood we call ```avrdude``` with the poper parametrs (be free to experiment with that), see the full command inside ```task.json```
```sh
1. Open avr-gcc-scon folder whit VSCODE
2. Type CTRL + SHIFT + B to open the building tasks defined in 'task.json'
3. Select one of 'flash (nano every)' or 'flash (uno)'
```

## avr-gcc-scons

This generation tool uses [Scons](https://www.scons.org) to generates all the steps useful to build from a simple Arduino sketch to an extended professional project.  Scons is  a very powerful, yet easy, construction tool, fully relaying on Python as configuration language. This means: what Scons does along the building just comes up easily to you from the code (a Python line).

I provide a Scons tool for the ```avr-gcc``` toolchain, and example of project compilation for Arduino Uno, and Arduino Nano Every. For each board there is a bare metal example ```helloworld``` where Arduino core library is not used, next to the classical sketch ```blink``` used by Arduino IDE.

So there are mainly two ways to use this repository:
1) ***Curiosity level***: clone the repository, modify, add or adjust the code in one of the folder, lunch ```scons``` command, and you have the executable ready to be flashed in the MCU memory, same smooth and peaceful experience of a plug and play tool

2) ***Expert level***: experiment with the flag (have you ever wonder how much size code LTO can save? And the -Os flag? Why don't compile for speed with -Of?), read the .map file (a photo of you executable in human readable format), optimize in deep your code.

## Philosophy
> I chosen to copy the code from the Arduino core library and provide it in the lib/ folder for one main reason: when the code of the core is update by ```Arduino IDE```, you want your well tested and long used executable not to be affected by this. If one want to try the last core release can always delete the content lib/arduino and replace the existing files with the last ones (a cleaner way should be add another folder lib/arduino<put_version_number_here>, copy ```Sconscript``` from lib/arduino, adjust it and use that on your program)

## New Boards

Well, until the board uses the avr core in lib/arduino or the avrmega core in lib/arduinomega there is nothing to worry about. The only thing to do is pass to the project the correct variants/<foldername> folder
```sh
def build_program(env):
    env.IncludeLibrary('arduinomega',arduino_variants_dir='nona4809')
```
To find out what variants/<foldername> folder is used, we can see how is compiled `variant.c` by ```Arduino IDE``` (with verbose option enabled) or by Vscode with Arduino extension (arduino.loglevel="verbose" on settings.json)
![Arduino IDE verbose output](/ArduinoIDE.jpg "Arduino IDE Building")

## Contributing

Eventually, whoever wants to improve and contribute to the extension of this tool is welcome.

>That's all folks, happy building!

## Dependencies

Python 3 (or 2) is required (Scons works even with Python 2, but who we are to not use Python 3 in a 2022 Project), installed by one of the following
* [Anaconda] - Anaconda Individual Edition is the world’s most popular Python distribution platform
* [Python3.x] - Python 3.x (a.k.a. "Python 3000" or "Py3k") is a new version of the language that is incompatible with the 2.x line of releases. The language is mostly the same, but many details, especially how built-in objects like dictionaries and strings work, have changed considerably, and a lot of deprecated features have finally been removed. Also, the standard library has been reorganized in a few prominent places

See `INSTALL.TXT` inside repository to have further informations

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Anaconda]: <https://www.anaconda.com/products/individual>
   [Python3.x]: <https://www.python.org/download/releases/3.0/>
