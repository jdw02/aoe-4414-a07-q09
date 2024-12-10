# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# 
# Parameters:
#  tx_w: Transmitter Power in Watts (W)
#  tx_gain_db: Transmitter Gain in Decibels (dB)
#  freq_hz: Frequency of transmission in Hertz (Hz)
#  dist_km: Distance Between Transmitter and Receiver in Kilometers(km)
#  rx_gain_db: Receiver Gain in Decibels (dB)
#  n0_j: Noise Spectral Density in Joules (J)
#  bw_hz: Bandwidth in Hertz (Hz)

# Output:
# Maximum achievable bitrate
#
# Written by Jayden Warren
# Other contributors: Brad Denby
#
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
c =  2.99792458e8 #speed of light

# helper functions


# initialize script arguments
tx_w = float('nan') # Transmitter Power in Watts (W)
tx_gain_db = float('nan') # Transmitter Gain in Decibels (dB)
freq_hz = float('nan') # Frequency of transmission in Hertz (Hz)
dist_km = float('nan') # Distance Between Transmitter and Receiver in Kilometers(km)
rx_gain_db = float('nan') # Receiver Gain in Decibels (dB)
n0_j = float('nan') # Noise Spectral Density in Joules (J)
bw_hz = float('nan') # Bandwidth in Hertz (Hz)

# parse script arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
   print(\
    'Usage: '\
    'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
   )
   exit()

# write script below this line
LineLoss = 10**(-1/10) # Line Loss
AtmLoss = 10**(0/10) # Atmospheric Loss
Wavelength = c/freq_hz; # Wavelength
S = dist_km*10**3

C = tx_w*LineLoss*tx_gain_db*((Wavelength/(4*math.pi*S))**2)*AtmLoss*rx_gain_db
N = n0_j*bw_hz
r_max = bw_hz*math.log((1+C/N),2)

print(math.floor(r_max))