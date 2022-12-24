from pynput.mouse import Button, Listener


mouse = Listener()
def click(x,y,button,pressed):
    print(x,y,button,pressed)

with Listener(on_click=click) as Listener:
    Listener.join()