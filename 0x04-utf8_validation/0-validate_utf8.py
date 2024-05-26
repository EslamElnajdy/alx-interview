#!/usr/bin/python3
"""
"""


def validUTF8(data):
    """
    validUTF8 - fn
    data: params[]
    return: boolean
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits of the byte
    mask1 = 0b10000000
    mask2 = 0b11000000

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF
        
        if num_bytes == 0:
            # Determine how many bytes in the current UTF-8 character
            if (byte & 0b10000000) == 0:
                # 1-byte character
                continue
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            # Check if it is a valid continuation byte
            if (byte & mask2) != mask1:
                return False
        
        # Decrease the number of bytes left to process
        num_bytes -= 1

    # If there are no more expected bytes, return True
    return num_bytes == 0
