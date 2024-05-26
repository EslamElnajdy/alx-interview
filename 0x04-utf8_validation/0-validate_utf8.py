#!/usr/bin/python3
"""
module
"""


def validUTF8(data):
    """
    validUTF8 - fn
    data: params[]
    return: boolean
    """
     # Number of bytes to process in the current UTF-8 character
    num_bytes = 0
    
    # Masks for checking the leading bits
    mask1 = 1 << 7
    mask2 = 1 << 6
    
    for num in data:
        # Get the binary representation of the integer
        byte = num & 0xFF
        
        if num_bytes == 0:
            # Determine how many bytes are in this UTF-8 character
            if (byte & mask1) == 0:
                # 1 byte character
                continue
            elif (byte & (mask1 | mask2)) == mask1:
                # Invalid byte (should not start with 10xxxxxx)
                return False
            elif (byte & (mask1 | mask2)) == (mask1 | mask2):
                # Determine the number of bytes in the character
                num_bytes = 1
                while byte & mask1:
                    num_bytes += 1
                    byte <<= 1
                if num_bytes == 1 or num_bytes > 4:
                    return False
        else:
            # Check if it's a valid continuation byte
            if (byte & (mask1 | mask2)) != mask1:
                return False
        
        num_bytes -= 1
    
    return num_bytes == 0
