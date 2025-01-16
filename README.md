# **MAX5144-SPI-C-Driver**

This repository contains a robust and reusable C++ driver for the MAX5144 DAC IC, designed to interface with SPI-enabled TEC controllers such as the MAX1978 on Raspberry Pi. The driver ensures precise control over the DAC's 14-bit resolution, enabling accurate temperature regulation.

---

## **Features**
- **Full SPI Implementation:** Supports SPI Mode 0 with configurable bus, channel, and clock speed.
- **Error Handling:** Ensures valid DAC output range and robust exception handling.
- **GPIO Control:** Manages the chip-select (CS) line via WiringPi.
- **Clean Architecture:** C++ object-oriented design for maintainability and extensibility.
- **Integration Ready:** Compatible with Raspberry Pi setups and WiringPi library.

---

## **Getting Started**

### **Clone the Repository**

```bash
git clone https://github.com/dcl920108/MAX5144-SPI-C-Driver.git
cd MAX5144-SPI-C-Driver
```

### **File Structure**
```
MAX5144-SPI-C-Driver/
├── include/
│   └── MAX5144.h     # Header file for MAX5144 class
├── src/
│   ├── MAX5144.cpp   # Implementation of MAX5144 class
│   └── main.cpp      # Example usage of MAX5144 driver
├── CMakeLists.txt    # CMake configuration file
└── README.md         # Project documentation
```

---

## **Build and Run**

1. **Install Dependencies**
   Ensure WiringPi is installed on your Raspberry Pi:
   ```bash
   sudo apt-get install wiringpi
   ```

2. **Configure CMake**
   Navigate to the project directory and create a build directory:
   ```bash
   mkdir build
   cd build
   cmake ..
   ```

3. **Compile**
   Compile the project using `make`:
   ```bash
   make
   ```

4. **Run the Example**
   Execute the generated binary:
   ```bash
   ./TemperatureControlProject
   ```

---

## **Code Example**

### **MAX5144 Class**
Here’s an example of how to initialize and use the driver:

```cpp
#include "MAX5144.h"
#include <iostream>

int main() {
    try {
        // Initialize MAX5144 with SPI bus 1, channel 1, and GPIO 17 for CS
        MAX5144 dac(1, 1, 17);

        // Set DAC output to 4854
        dac.setDacOutput(4854);

        std::cout << "DAC output successfully set!" << std::endl;
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```

### **CMake Configuration**
The `CMakeLists.txt` ensures proper setup for the project:
```cmake
cmake_minimum_required(VERSION 3.10)
project(MAX5144-SPI-C-Driver)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-g")

# Include directories
include_directories(include)

# Main executable
add_executable(TemperatureControlProject src/main.cpp src/MAX5144.cpp)
target_link_libraries(TemperatureControlProject wiringPi)
```

---

## **Tips for Beginners**

### **CMake**
CMake can be intimidating for beginners due to its verbose error messages. Follow these tips:
1. Ensure all paths (e.g., `include_directories`) are correct.
2. Pay attention to `target_link_libraries` to link WiringPi properly.
3. If errors arise, try running:
   ```bash
   cmake --debug-output ..
   ```

---

## **Contributing**
We welcome contributions! Please fork this repository, create a feature branch, and submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Let me know if you need further refinements!
