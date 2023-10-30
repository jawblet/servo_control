import serial
import lewansoul_lx16a
import time

print("test...")

SERIAL_PORT = '/dev/cu.usbserial-1110'
controller = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT, 115200, timeout=1),
)

# id1 = controller.get_servo_id()

# controller.set_servo_id(1, 5)

servo1 = controller.servo(4)
servo2 = controller.servo(5)

# controller.move(4, 500) # move servo ID=1 to position 100

# print(id1, id2)

### SEATED POSITION
servo1.move_prepare(200)
servo2.move_prepare(100)
controller.move_start()

time.sleep(0.1)
