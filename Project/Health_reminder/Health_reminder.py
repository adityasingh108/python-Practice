from pygame import mixer
from datetime import datetime
from time import time


def Music_player(file, stopper):
      mixer.init()
      mixer.music.load(file)
      mixer.music.play()
      while True:
            a= input("")
            if a == stopper:
                  mixer.music.stop()
                  break




def Loggig_the_data(msg):
      with open("mylog.txt","a") as f:
            f.write(f"{msg} {datetime.now()}\n")


if __name__=="__main__":
      water_drinking = time()
      eye_exercise = time()
      physical_exercise = time()
      water_secs =3
      eye_second =9
      physical_second =5
      while True:

            # a = input("Enter q to stop the the program ")
            # if a != 'q':
            if time() - water_drinking > water_secs:
                  print("It's time to drink the water &Enter drank to stop the alarm")
                  Music_player("water.mp3", "drank")
                  Loggig_the_data("water drink at:")
            if time() - eye_exercise > eye_second:
                  print("It's Time to eyes exercise & Enter done the stop the alarm")
                  Music_player("eyes.mp3", "done")
                  Loggig_the_data("Eye exercise at")
            if time() - physical_exercise - physical_second:
                  print("It's time to Do physical activity & done to stop the alarm")
                  Music_player("physical.mp3", "done")
                  Loggig_the_data("Do exercise at ")



