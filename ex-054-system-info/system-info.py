# course: python self training
# exercise: 18
# date: Oct 11 2020
# username: shinigami
# name: Cristiano Cavo
# description: write a cli program that returns some system infos
# filename: electronic-rhymary.py

import platform

def sysInfo():
	print("kernel:",platform.system())
	print("release:",platform.release())
	print("machine:",platform.machine())
	print("architecture:",platform.architecture())
	print("version:",platform.version())

sysInfo()