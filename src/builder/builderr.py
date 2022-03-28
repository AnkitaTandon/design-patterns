from phone import *

class phone_builder:

    def __init__(self, phone = Phone()) :
        self.phone = phone

    def set_os(self, os):
        self.phone.os = os
        return self

    def set_ram(self, ram):
        self.phone.ram = ram
        return self

    def set_processor(self, processor):
        self.phone.processor = processor
        return self

    def set_battery(self, battery):
        self.phone.battery = battery
        return self

    def set_cam(self, cam):
        self.phone.cam = cam
        return self

    def get_phone(self):
        return self.phone
