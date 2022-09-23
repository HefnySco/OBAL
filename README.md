This work is licensed under Creative Commons Attribution-ShareAlike 4.0 International License.

[![Creative Commons Attribution-ShareAlike 4.0 International License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png "Creative Commons Attribution-ShareAlike 4.0 International License")](http://creativecommons.org/licenses/by-sa/4.0/ "Creative Commons Attribution-ShareAlike 4.0 International License")

# Open Board Architecture for Linux - OBAL

OBAL is a new Linux-based board for Ardupilot called Open-Board Architecture for Linux  (OBAL). It is designed to be simple to build by professionals as well as hobbyists.

OBAL acts as a simple board with necessary sensors that can be upgraded easily. The board is built over Raspberry Pi. It can use Raspberry Pi 2,3,4 & zero.

Current Linux-based Ardupilot flight controllers that run on Raspberry Pi usually consist of a shield with built-in sensors on it. That cannot be removed or replaced easily. However OBAL is more like a test or development board, where you can remove sensors and replace sensors easily. Also sensors on the board are breakouts that you can solder easily.

OBAL does not use any closed source code, or specialized drivers. It is all open and can be compiled from scratch. Also schematic and board are all published and available to access.

OBAL can be the start step for understanding Ardupilot Linux-based boards and for building more complex boards.a

## Technical Specification

[![Obal Board 3D](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/Obal3D.png "Obal Board 3D")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/Obal3D.png "Obal Board 3D")

The board is simple and contains only necessary sensors with no redundant components. However extra SPI & I2C sockets are available to extend board capability and connect more sensors. 

The board also has a safety switch that prevents the motors from turning on. The switch is connected directly to output and is not connected logically to Ardupilot so it is an external safety mechanism.


The board enabled users to make it at home with simple soldering techniques. It uses breakouts that are famous and available worldwide. Only two SMD resistors are required and it is not that hard to solder.



Please refer to WIKI for full details.
## [Hardware Specification](https://github.com/HefnySco/OBAL/wiki "WIKI")


feel free to email me: [Hardware Specification](email:mohammad.hefny@gmail.com "mohammad.hefny@gmail.com") for any extra support.

THE DESIGN IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS DESIGN INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS DESIGN.