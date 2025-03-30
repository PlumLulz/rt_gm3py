# keygen for the Iskratel RT-GM3 with SSIDs RT-GPON-HHHH and RT-5GPON-HHHH
# from /usr/sbin/fad found in firmware for the RT-GM3 on 4PDA.to forum
# serial numbers all seem to start with 31 and are 10 digits long.
# much thanks to hydddra for giving me access to 4PDA.

import argparse

def rt_gm3(sn):
	cs1 = '23456789abdefghiajk'
	cs2 = 'ABDEFGHAJK'
	salt = 'rostelecom'

	digits = list(sn[::-1])
	values = []
	values.append(int(digits[0]) + ord(salt[0]))

	for i in range(1, 10):
		values.append(values[i-1] + int(digits[i]) + ord(salt[i]))

	pwd = []
	for i in range(1, 10):
		pwd.append(cs1[values[i] % 19])

	pwd.insert(0, cs2[values[0] % 19])

	print("".join(pwd))

parser = argparse.ArgumentParser(description='Keygen for the Iskratel RT-GM3 with SSIDs RT-GPON-HHHH and RT-5GPON-HHHH')
parser.add_argument('sn', help='Serial Number')
args = parser.parse_args()

rt_gm3(args.sn)