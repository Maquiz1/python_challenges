# Write a Python function to play a sound and print a message at a set time
# INPUT: alarm time,sound file ,message

import sched
import time
import winsound as ws
import playsound


def set_alarm(alarm_time, wav_file, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, playsound.PlaySound, argument=(wav_file, playsound.SND_FILENAME))
    print('Alarm set for', time.asctime(time.localtime(alarm_time)))
    s.run()


set_alarm(time.time() + 3, 'alarm.wav', 'Wake up!')


