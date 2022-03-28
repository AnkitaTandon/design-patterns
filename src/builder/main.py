from builderr import *
from phone import *

if __name__ == "__main__":
    builder = phone_builder()
    phone = builder.get_phone()
    print(phone)

    phone = builder.set_os("android").set_ram("8GB").set_cam(13).get_phone()
    
    builder2 = phone_builder(phone)
    print(builder2.set_battery("XYZ").get_phone())
