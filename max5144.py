import spidev
import RPi.GPIO as GPIO
import time

class MAX5144:
    def __init__(self, spi_bus, spi_device, cs_pin):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 500000
        self.spi.mode = 0b00

        self.cs_pin = cs_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.cs_pin, GPIO.OUT)
        GPIO.output(self.cs_pin, GPIO.HIGH)

    def set_dac_output(self, value):
        assert 0 <= value < 16384, "Invalid DAC value"
        data_word = value << 2
        msb = (data_word >> 8) & 0xFF
        lsb = data_word & 0xFF

        GPIO.output(self.cs_pin, GPIO.LOW)
        self.spi.writebytes([msb, lsb])
        GPIO.output(self.cs_pin, GPIO.HIGH)
        print(f"DAC value set to: MSB = {msb:#04X}, LSB = {lsb:#04X}")

    def cleanup(self):
        self.spi.close()

class TECController:
    def __init__(self, max5144):
        self.max5144 = max5144
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)  # MAX1978控制引脚
        GPIO.output(4, GPIO.HIGH)  # 打开MAX1978

    def set_temperature(self, temperature):
        temperature_to_dac_value = {
        30: 7368,
        31: 7203,
        32: 7026,
        33: 6861,
        34: 6696,
        35: 6531,
        36: 6366,
        37: 6200,
        38: 6046,
        39: 5892,
        40: 5738,
        41: 5595,
        42: 5441,
        43: 5297,
        44: 5165,
        45: 5022,
        46: 4890,
        47: 4758,
        48: 4626,
        49: 4493,
        50: 4372,
        51: 4251,
        52: 4141,
        53: 4020,
        54: 3910,
        55: 3800,
        56: 3689,
        57: 3590,
        58: 3491,
        59: 3392,
        60: 3293,
        61: 3194,
        62: 3106,
        63: 3018,
        64: 2930,
        65: 2852,
        66: 2764,
        67: 2687,
        68: 2610,
        69: 2533,
        70: 2467,
        71: 2390,
        72: 2324,
        73: 2258,
        74: 2192,
        75: 2126,
        76: 2070,
        77: 2004,
        78: 1949,
        79: 1894,
        80: 1839,
        81: 1795,
        82: 1740,
        83: 1696,
        84: 1641,
        85: 1597,
        86: 1553,
        87: 1509,
        88: 1465,
        89: 1421,
        90: 1388,
        91: 1344,
        92: 1311,
        93: 1278,
        94: 1233,
        95: 1200,
        96: 1167,
        97: 1145,
        98: 1112,
        99: 1079,    
        }
        dac_value = temperature_to_dac_value.get(temperature)
        if dac_value is not None:
            self.max5144.set_dac_output(dac_value)
            print(f"Set temperature to {temperature}°C with DAC value {dac_value}")
        else:
            print("Temperature out of range")

    def manual_control_max1978(self):
        while True:
            command = input("Enter 'on' to turn on MAX1978, 'off' to turn off, or 'exit' to quit: ").strip().lower()
            if command == 'on':
                GPIO.output(4, GPIO.HIGH)
                print("MAX1978 turned ON")
            elif command == 'off':
                GPIO.output(4, GPIO.LOW)
                print("MAX1978 turned OFF")
            elif command == 'exit':
                print("Exiting manual control")
                break
            else:
                print("Invalid command, please enter 'on', 'off', or 'exit'")

    def cleanup(self):
        GPIO.cleanup()

def main():
    cs_pin = 17  # 根据硬件配置调整
    max5144 = MAX5144(spi_bus=1, spi_device=1, cs_pin=cs_pin)
    tec_controller = TECController(max5144)

    try:
        test_temperature = 35  # 设定一个测试温度，例如50°C
        tec_controller.set_temperature(test_temperature)
        print("TEC is heating up... Press Ctrl+C to stop.")
        tec_controller.manual_control_max1978()
    except KeyboardInterrupt:
        print("Test interrupted by user")
    finally:
        tec_controller.cleanup()
        max5144.cleanup()

if __name__ == "__main__":
    main()
