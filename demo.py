from usb_receipt_printer import printer

with printer() as that:
    that.write('Hello, world!\n\n')
    #         000000000111111111122222222223
    #         123456789012345678901234567890
    that.write('Soluta sed voluptatem ut\n')
    that.write('facere aut. Modi placeat et\n')
    that.write('eius voluptate sint ut.\n')
    that.write('Facilis minima ex quia quia\n')
    that.write('consectetur ex ipsa. Neque et\n')
    that.write('voluptatem ipsa enim error\n')
    that.write('rthatrehenderit ex dolore.\n')
    that.write('Cupiditate ad voluptatem nisi.\n\n\n\n')
