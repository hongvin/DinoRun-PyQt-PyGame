# DinoRun-PyQt-PyGame
Integration between Pygame and PyQt5 for Dino Run Game

# Concept
## Concept of the game and the design flow.
This game is purely designed with PyGame library. To link two different GUIs is not possible. As such, a simple trick is done. It is started with initializing the PyGame library to run a GUI (pygame.init()).  Since the GUI created by PyGame is supposed to be ‘embedded’ into PyQt, the PyGame’s GUI is ‘hidden’ by setting it’s windows coordinate out of the screen, using os library with the command `os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-300,-300)`.

As such, the PyGame window shall started at x=-300 and y=-300, which is out of the screen, or ‘hidden’ from user. The next step is to capturing every frame created by PyGame and show it in the PyQt windows. So, at the end of the gameplay function (situated in class App), the four lines below is used.

```python
data=screen.get_buffer().raw
image=QtGui.QImage(data,width,height,QtGui.QImage.Format_RGB32)
pixmap = QPixmap.fromImage(image)
win.setPixmap(pixmap)
```
First, the data variable get the PyGame’s screen raw buffer. By utilizing ```QtGui.QImage```, the raw buffer is converted into RGB32 format image. With the help of ```QPixmap```, the image is then set to map the label and shown in the label.

The second problem is the keyboard event. Since the game is developed in PyGame, thus the keyboard event is defined in PyGame. By the help of PyQt key press event, every key is captured and stored in act variable which is then used to compare and made the right move.

The OpenCV is implemented. The technique used is morphological transformations. It is used to detect an object and track. It tends to come in pairs. Erosion is used to erode the edge and Dilation is used to do the opposite of erosion. This is used to analyses sequential video frames and outputs the movement of targets between the frame.

## How to play the game?
Choose the desired game mode and press space to start the game. Use space bar or up arrow to jump and down arrow to duck. 


Main game reference from **Rohit Rane**
