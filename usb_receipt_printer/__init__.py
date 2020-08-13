from contextlib import contextmanager

import usb.core
import usb.util

@contextmanager
def printer():
    dev = usb.core.find(idVendor=0x0416, idProduct=0x5011)
    # Was it found?
    if dev is None:
        raise ValueError('Device not found')

    # Disconnect it from kernel
    needs_reattach = False
    if dev.is_kernel_driver_active(0):
        needs_reattach = True
        dev.detach_kernel_driver(0)

    # Set the active configuration. With no arguments, the first
    # configuration will be the active one
    dev.set_configuration()

    # get an endpoint instance
    cfg = dev.get_active_configuration()
    intf = cfg[(0,0)]

    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match = \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT)

    assert ep is not None
    yield ep
    dev.reset()
    if needs_reattach:
        dev.attach_kernel_driver(0)
        print("Reattached USB device to kernel driver")