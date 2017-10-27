#!/usr/bin/python
# Supports Python 3.X and Above

import time
import smbus

# ===========================================================================
# ST_VL53X0L TOF Sensor
#
# Code Created by Thomas Holecek
#
# 
# References VL53L0X API distributed by ST Micro
#
# ===========================================================================

class VL53X0L:

	i2c = None
	
	VL53L0X_REG_IDENTIFICATION_MODEL_ID				= 0x00C0
	VL53L0X_REG_IDENTIFICATION_REVISION_ID			= 0x00C2
	
	def __init__(self, address=0x29, debug=true)
	
	#setup i2c bus and sensor address
	#Assumes use of RPI device that is new enough
	#to use SMBus=1, older devices use SMBus = 0
	self.i2c = smbus.SMBus(1)
	self.address = address
	self.debug = debug
	
	#Module identification defaults
	self.idModel = 0x00
	self.idRev = 0x00
	
	
	
	
	def get_identification(self);
	
		self.idModel = self.get_register_16Bit(self.VL53L0X_REG_IDENTIFICATION_MODEL_ID)
		self.idRev = self.get_register_16Bit(self.VL53L0X_REG_IDENTIFICATION_REVISION_ID)
	
	
	
	def get_register(self, register_address):
		a1 = (register_address >> 8) & 0xFF
        a0 = register_address & 0xFF
        self.i2c.write_i2c_block_data(self.address, a1, [a0])
        data = self.i2c.read_byte(self.address)
        return data
    def get_register_16bit(self, register_address):
        a1 = (register_address >> 8) & 0xFF
        a0 = register_address & 0xFF
        self.i2c.write_i2c_block_data(self.address, a1, [a0])
        data0 = self.i2c.read_byte(self.address)
        data1 = self.i2c.read_byte(self.address)
        return (data0 << 8) | (data1 & 0xFF)
    def set_register(self, register_address, data):
        a1 = (register_address >> 8) & 0xFF
        a0 = register_address & 0xFF
        self.i2c.write_i2c_block_data(self.address, a1, [a0, (data & 0xFF)])
    def set_register_16bit(self, register_address, data):
        a1 = (register_address >> 8) & 0xFF
        a0 = register_address & 0xFF
        d1 = (data >> 8) & 0xFF
        d0 = data & 0xFF
		self.i2c.write_i2c_block_data(self.address, a1, [a0, d1, d0])
	