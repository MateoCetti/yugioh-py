from interfaces.interface import Interface

if __name__ == "__main__":
    interface = Interface()
    running = True
    interface.start()
    while running:
        running = interface.iterate()
    interface.stop()
        
