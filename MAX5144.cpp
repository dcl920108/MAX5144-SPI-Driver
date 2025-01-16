#include "MAX5144.h"
#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <iostream>
#include <stdexcept>

MAX5144::MAX5144(int spiNumber, int spiChannel, int csPin, int speed, int mode)
    : csPin(csPin), spiNumber(spiNumber), spiChannel(spiChannel) {
    // Initialize WiringPi
    wiringPiSetup();

    // Configure GPIO pin for CS (Chip Select)
    pinMode(csPin, OUTPUT);
    digitalWrite(csPin, HIGH); // Set CS to HIGH initially (inactive)

    // Setup SPI communication with specified parameters
    if (wiringPiSPIxSetupMode(spiNumber, spiChannel, speed, mode) < 0) {
        throw std::runtime_error("SPI initialization failed!");
    }

    std::cout << "SPI initialized successfully on SPI" << spiNumber
              << " channel " << spiChannel << std::endl;
}

void MAX5144::setDacOutput(int value) {
    // Ensure the value is within the 14-bit range (0–16383)
    if (value < 0 || value > 16383) {
        throw std::invalid_argument("DAC value out of range! Valid range: 0–16383.");
    }

    // Prepare the 16-bit data word to send
    int dataWord = value << 2; // Left-align the 14-bit DAC value
    unsigned char buffer[2] = {
        static_cast<unsigned char>((dataWord >> 8) & 0xFF), // MSB
        static_cast<unsigned char>(dataWord & 0xFF)         // LSB
    };

    // Activate the DAC (CS LOW)
    digitalWrite(csPin, LOW);

    // Transfer data over SPI
    if (wiringPiSPIxDataRW(spiNumber, spiChannel, buffer, 2) < 0) {
        throw std::runtime_error("SPI data transfer failed!");
    }

    // Deactivate the DAC (CS HIGH)
    digitalWrite(csPin, HIGH);

    // Log success
    std::cout << "DAC output set to: " << value << std::endl;
}

MAX5144::~MAX5144() {
    // Destructor to release resources if needed (currently empty)
}
