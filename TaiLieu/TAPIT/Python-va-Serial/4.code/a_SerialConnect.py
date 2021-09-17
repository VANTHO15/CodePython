import serial
import serial.tools.list_ports as list_ports


def get_SerialPort():
    ports = list_ports.comports()
    avaliable = []
    for port, desc, hwid in sorted(ports):
        avaliable.append({'Port': port,
                          'Name': desc,
                          'Properties': hwid})
    return avaliable


if __name__ == '__main__':
    Serial_list = (get_SerialPort())
    Serial_connect = serial.Serial(Serial_list[0]['Port'],
                                   baudrate=9600,
                                   bytesize=serial.EIGHTBITS,
                                   parity=serial.PARITY_NONE,
                                   stopbits=serial.STOPBITS_ONE,
                                   timeout=0.1)
    # while True:
    #     data = Serial_connect.read()
    #     if data == b'':
    #         continue
    #     print(data, '-', data.hex(), '-', int(data.hex(), 16))

    # import time
    # import random
    # while True:
    #     data_send = random.randint(0, 100)
    #     packet = bytearray()
    #     packet.append(data_send)
    #     Serial_connect.write(packet)
    #     data = Serial_connect.read()
    #     if data == b'':
    #         continue
    #     print('Send: ', data_send, 'Receive:', data, '-', data.hex(), '-', int(data.hex(), 16))
    #     time.sleep(0.1)

    import time
    import random

    count = 0
    timer = time.time()
    while True:
        data_send = random.randint(0, 100)
        packet = bytearray()
        packet.append(data_send)
        Serial_connect.write(packet)
        data = Serial_connect.read()
        if data == b'':
            continue
        count += 1
        print(int(data.hex(), 16))
        time.sleep(0.1)
        if time.time() - timer > 10:
            break
    print('Count: {}'.format(count))
