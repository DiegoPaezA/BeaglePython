#!/usr/bin/python

from PCA9548lib import PCA9548

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PCA9548 and use Channel 1 (default value)
# bmp = PCA9548(0x70)
bmp = PCA9548(0x70)

# To specify a different channel, uncomment one of the following:
# bmp = PCA9548(0x70, 1) #CH1
# bmp = PCA9548(0x70, 2) #CH2
# bmp = PCA9548(0x70, 3) #CH3
# bmp = PCA9548(0x70, 4) #CH4
# bmp = PCA9548(0x70, 5) #CH5
# bmp = PCA9548(0x70, 6) #CH6
# bmp = PCA9548(0x70, 7) #CH7
# bmp = PCA9548(0x70, 8) #CH8

