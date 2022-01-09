from temp_reader import read_temp
import time, telegram_send

temp = read_temp()
start_time = time.time()

while temp < 95:
    temp = read_temp()
    print("La tempratura va en {:.1f}ºC y llevamos {:.0f}s".format(temp, time.time() - start_time))	
    time.sleep(10)

boil_time = time.time()
message = "Hirvió en {:.0f}s".format(boil_time - start_time)
telegram_send.send(messages=[message])

while time.time() - boil_time < 15 * 60:
    temp = read_temp()
    print("La tempratura está en {:.1f}ºC y llevamos {:.0f}s de 900s desde que hirvió".format(temp, time.time() - start_time))
    time.sleep(10)

message = "Están listas las hallacas! nos demoramos {:.0f}s en todo el proceso".format(time.time() - start_time)
telegram_send.send(messages=[message])