
class Phone:
    def __init__(self) :
        self.os = None
        self.ram = None
        self.processor = None
        self.battery = None
        self.cam = None

    def __str__(self):
        return ("The Phone details are - \n OS: "+ str(self.os) + "\n Processor: " + str(self.processor) + "\n Battery: " \
                    + str(self.battery) + "\n RAM: " + str(self.ram) + "\n Camera: " + str(self.cam) + "\n")
        
