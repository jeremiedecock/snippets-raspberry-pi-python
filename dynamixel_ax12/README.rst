Dynamixel AX-12
===============

This snippet show how to control Robotis Dynamixel AX-12 servos from Raspberry
Pi's GPIO.

A small electronic circuit is needed to convert Raspberry Pi UART signals (on
RX and TX pins) to the half-duplex ones required by Dynamixels (see
https://web.archive.org/web/20100414173935/support.robotis.com/en/product/dynamixel/dxl_ax_main.htm).

The chips that converts full-duplex into half-duplex are either 74HC126/74HC04
or 74LS241.

Dynamixel AX-12 documentation
-----------------------------

`Official documentation <https://web.archive.org/web/20101008170532/http://support.robotis.com/en/product/dynamixel/ax_series/dxl_ax_actuator.htm>`__ (archive).

Control Dynamixel AX-12 with the 74LS241
----------------------------------------

For the 74LS241, it's well explained on the following pages:

- http://www.oppedijk.com/robotics/control-dynamixel-with-raspberrypi
- http://memememememememe.me/post/the-dynamixel-ax-12a-servos/
- http://robottini.altervista.org/dynamixel-ax-12a-and-arduino-how-to-use-the-serial-port
- http://savageelectronics.blogspot.fr/2011/01/arduino-y-dynamixel-ax-12.html

A PCB by Thiago Hersan is freely available here:

- https://circuits.io/circuits/267189-ax-12-driver-for-raspberry-pi/#pcb

For the schematics, check the following pages:

- http://memememememememe.me/assets/posts/the-dynamixel-ax-12a-servos/uart_half-duplex_74LS241.jpg
- https://circuits.io/circuits/267189-ax-12-driver-for-raspberry-pi/#schematic
- http://robottini.altervista.org/wp-content/uploads/2011/12/Dynamixel-Arduino-electric-schema-1024x768.jpg (this one doesn't link pins 3 and 20 by a resistor)

Control Dynamixel AX-12 with the 774HC126/74HC04
------------------------------------------------

For the 74HC126/74HC04, check the following page:

- https://web.archive.org/web/20110202164651/support.robotis.com/en/product/dynamixel/dxl_ax_main.htm

Additional information
----------------------

See also: https://github.com/jeremiedecock/pyax12/issues/2
