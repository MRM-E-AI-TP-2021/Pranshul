import Serial
with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
    x = ser.read()
    s = ser.read(10)
    line = ser.readline()
