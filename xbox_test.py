from pybricks.hubs import TechnicHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from pybricks.iodevices import XboxController

# Initialisation.
hub = TechnicHub()
controller = XboxController()
hub.light.off() # The controller finished connecting, so we signal that.

# Returns true if a button is pressed or a stick/trigger is moved from its neutral position.
def inputPressed():
    return controller.buttons.pressed() != set() or controller.dpad() != 0 or controller.joystick_left() != (0, 0) or controller.joystick_right() != (0, 0) or controller.triggers() != (0, 0)

while(True):
    # Turn off the LED if there are no inputs.
    if(not inputPressed()):
        hub.light.off()

    # Wait for an input.
    while(not inputPressed()):
        pass
    
    # Read the inputs, to be processed later.
    dpad = controller.dpad()
    buttonsPressed = controller.buttons.pressed()
    stick1 = controller.joystick_left()
    stick2 = controller.joystick_right()
    triggers = controller.triggers()

    # Turn the LED on in different colours depending on the input.
    if(dpad != 0):
        hub.light.on(Color.ORANGE)
    elif(buttonsPressed != set()):
        hub.light.on(Color.WHITE)
    elif(stick1 != (0, 0)):
        if(abs(stick1[1]) < 10 ):
            intensity = abs(stick1[0]) / 100
            print(intensity)
            hub.light.on(Color.YELLOW * intensity)
        elif(abs(stick1[0]) < 10):
            intensity = abs(stick1[1]) / 100
            print(intensity)
            hub.light.on(Color.BLUE * intensity)
    elif(stick2 != (0, 0)):
        if(abs(stick2[1]) < 10 ):
            intensity = abs(stick2[0]) / 100
            print(intensity)
            hub.light.on(Color.CYAN * intensity)
        elif(abs(stick2[0]) < 10):
            intensity = abs(stick2[1]) / 100
            print(intensity)
            hub.light.on(Color.VIOLET * intensity)
    elif(triggers != (0, 0)):
        if(abs(triggers[1]) < 10 ):
            intensity = abs(triggers[0]) / 100
            print(intensity)
            hub.light.on(Color.GREEN * intensity)
        elif(abs(triggers[0]) < 10):
            intensity = abs(triggers[1]) / 100
            print(intensity)
            hub.light.on(Color.RED * intensity)

    wait(10) # Calm down a bit before polling the inputs again.
