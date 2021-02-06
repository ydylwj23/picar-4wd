import picar_4wd as fc
import random

speed = 30

# 0: forward 1: left 2: right
dir = 0

def main():
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)

        global dir

        if tmp != [2,2,2,2]:
            if dir == 0:
                if random.random() < 0.5:
                    fc.turn_right(speed)
                    dir = 2
                else:
                    fc.turn_left(speed)
                    dir = 1
            elif dir == 1:
                fc.turn_left(speed)
            else :
                fc.turn_right(speed)
        else:
            dir = 0
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
