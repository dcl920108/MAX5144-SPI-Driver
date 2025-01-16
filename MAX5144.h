#ifndef MAX5144_H
#define MAX5144_H

/**
 * @class MAX5144
 * @brief A class to control the MAX5144 DAC via SPI.
 */
class MAX5144 {
public:
    /**
     * @brief Constructor to initialize MAX5144.
     * @param spiNumber SPI bus number (e.g., 0 for /dev/spidev0.x).
     * @param spiChannel SPI channel (e.g., 0 or 1 for /dev/spidevX.x).
     * @param csPin GPIO pin used for chip select (in BCM format).
     * @param speed SPI communication speed (default: 500000 Hz).
     * @param mode SPI mode (default: 0).
     */
    MAX5144(int spiNumber, int spiChannel, int csPin, int speed = 500000, int mode = 0);

    /**
     * @brief Destructor to clean up resources.
     */
    ~MAX5144();

    /**
     * @brief Sets the DAC output value.
     * @param value DAC output value (0-16383).
     */
    void setDacOutput(int value);

private:
    int csPin;       // GPIO pin for chip select
    int spiNumber;   // SPI bus number
    int spiChannel;  // SPI channel
};

#endif // MAX5144_H
