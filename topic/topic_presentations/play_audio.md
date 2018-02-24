
### The music module is closely tied to pygame.mixerpygame module for loading and playing sounds. Use the music module to control the playback of music in the sound mixer.

This will load a music filename/file object and prepare it for playback:


- ```pygame.mixer.music.play()```This will play the loaded music stream. If the music is already playing it will be restarted.

- ```pygame.mixer.music.pause()``` Temporarily stop playback of the music stream. It can be resumed with the pygame.mixer.music.unpause() function.

- ```pygame.mixer.music.unpause()``` This will resume the playback of a music stream after it has been paused.

- ```pygame.mixer.music.stop()```Stops the music playback if it is currently playing.


But the first need to installing pygame.

``````
$ pip install pygame
``````


```python
import pygame
from pygame import mixer

pygame.mixer.init()
pygame.mixer.music.load("directory/audio_name.mp3")
    
def PlayMusic():

    userChoice = input("What do you want to do? \n1) Play \n2) Pause \n3) Unpause \n4) Stop \n5) Quit \n")
    
    # Check and see what the typed.
    # If the user typed 1
    if userChoice == "1":
        # Store what the user typed into a variable
        pygame.mixer.music.play()
        print ("Your are now playing the music")
        PlayMusic()
        
    # If the user typed 2
    elif userChoice == "2":
        # Store what the user typed into a variable
        pygame.mixer.music.pause()
        print ("Your are now Pause the music, please type 3 to continue")
        PlayMusic()
        
    # If the user typed 3
    elif userChoice == "3":
        # Store what the user typed into a variable
        pygame.mixer.music.unpause()
        print ("Your are now continue to playing the music")
        PlayMusic()
        
    # If the user typed 4
    elif userChoice == "4":
        # Store what the user typed into a variable
        pygame.mixer.music.stop()
        print ("Your are now stoping the music")
        PlayMusic()
        
    elif userChoice == "5":
        # Store what the user typed into a variable
        pygame.mixer.music.stop()
        print ("Thank you for playing this music")
        
    # If the user typed anything else  
    else:
        # Tell the user what they did wrong.
        print("Error: You entered invalid information, please try again")
        # Run the script again.
        PlayMusic()
        
PlayMusic()
```
