import sys
import glob
import serial

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

if __name__ == '__main__':

    rep=""
    ports=serial_ports()
    print(ports)
    print()
    while rep not in ports:
        rep = input('  Enter a COM port (eg COM1) and press enter:  ')

    ser = serial.Serial(rep, 115200, bytesize = serial.EIGHTBITS , timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    print()
    port2 = serial_ports()
    print(port2)
    print("succesfully connected to: "+rep)
    print()
    print("waiting for data:")

    while True:
        print()
        s = ser.readline(100)       # read up to one hundred bytes
        sd = s.decode('latin-1')
        sd = sd.replace("/nAngle pitch :", "")
        sd = sd.replace("  Angle roll  :", "")
        sd = sd.replace(' ', "")
        sd = sd.replace('\r\n', "")
        sd2 = sd.split("/")
        print(sd2)
