#!/usr/bin/env python

from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
import subprocess
from killerbee import *
from StringIO import StringIO
import sys,os,signal,time
from killerbee import *

txcount = 0
rxcount = 0
stumbled = {}

class ZBStumblerThread(QtCore.QThread):
        def __init__(self,Channel):
                super(ZBStumblerThread,self).__init__()
		self.channel=Channel
		print "[*] initializing zbstumbler thread"

        def __del__(self):
                self.wait()

        def close(self):
                self.terminate()

	def display_details(self,routerdata):
   		global args
    		string=""
    		stackprofile_map = {0:"Network Specific",1:"ZigBee Standard",2:"ZigBee Enterprise"}
    		stackver_map = {0:"ZigBee Prototype",    1:"ZigBee 2004",2:"ZigBee 2006/2007"}
    		spanid, source, extpanid, stackprofilever, channel = routerdata
    		stackprofile = ord(stackprofilever) & 0x0f
    		stackver = (ord(stackprofilever) & 0xf0) >>4
	    	string="\t[+]  New Network: PANID 0x%02X%02X  Source 0x%02X%02X"%(ord(spanid[0]), ord(spanid[1]), ord(source[0]), ord(source[1]))+"\n"

    		try:
        		extpanidstr=""
        		for ind in range(0,7):
            			extpanidstr += "%02x:"%ord(extpanid[ind])
        		extpanidstr += "%02X"%ord(extpanid[-1])
        		string=string+("\t\tExt PANID: " + extpanidstr)+"\n"
    		except IndexError:
        		string=string+("\t\tExt PANID: Unknown")+"\n"

    		try:
       			string+= "\t\tStack Profile: %s"%stackprofile_map[stackprofile]+"\n"
        		stackprofilestr = stackprofile_map[stackprofile]
    		except KeyError:
        		string+= "\t\tStack Profile: Unknown (%d)"%stackprofile+"\n"
        		stackprofilestr = "Unknown (%d)"%stackprofile

    		try:
        		string+="\t\tStack Version: {0}".format(stackver_map[stackver])+"\n"
        		stackverstr = stackver_map[stackprofile]
    		except KeyError:
        		string+=("\t\tStack Version: Unknown ({0})".format(stackver)+"\n")
        		stackverstr = "Unknown (%d)"%stackver

    		string+=("\t\tChannel: {0}".format(channel)+"\n")
                self.emit(SIGNAL('stumbler_update(QString)'), QtCore.QString(string))
 


	def response_handler(self,stumbled, packet, channel):
    		global args
    		d154 = Dot154PacketParser()
    		# Chop the packet up
    		pktdecode = d154.pktchop(packet)
    		# Byte-swap the frame control field
    		fcf = struct.unpack("<H", pktdecode[0])[0]
    		# Check if this is a beacon frame
    		if (fcf & DOT154_FCF_TYPE_MASK) == DOT154_FCF_TYPE_BEACON:
	                self.emit(SIGNAL('stumbler_update(QString)'), QtCore.QString("\t[+]  Received frame is a beacon."))
        		#print "Received frame is a beacon."
        		# The 6th element offset in the Dot154PacketParser.pktchop() method
        		# contains the beacon data in its own list.  Extract the Ext PAN ID.
        		spanid = pktdecode[4][::-1]
        		source = pktdecode[5][::-1]
        		beacondata = pktdecode[6]
        		extpanid = beacondata[6][::-1]
        		stackprofilever = beacondata[4]
        		key = ''.join([spanid, source])
        		value = [spanid, source, extpanid, stackprofilever, channel]
        		if not key in stumbled:
                        	self.emit(SIGNAL('stumbler_update(QString)'), QtCore.QString("\t[+]  Beacon represents a new network."))
            			#print hexdump(packet)
            			#print pktdecode
            			stumbled[key] = value
            			self.display_details(value)
        		return value
    		notbeacon="\t[+]  Received frame is not a beacon (FCF={0}).".format(pktdecode[0].encode('hex'))
                self.emit(SIGNAL('stumbler_update(QString)'), QtCore.QString(notbeacon))
   	 	return None

	def interrupt(self,signum, frame):
    		global txcount, rxcount
    		global kb
    		global args
    		kb.close()
   	 	print("\n{0} packets transmitted, {1} responses.".format(txcount, rxcount))
    		sys.exit(0)

	def run(self):
		channel=self.channel
    		global txcount,rxcount
    		# Beacon frame
    		beacon = "\x03\x08\x00\xff\xff\xff\xff\x07"
    		# Immutable strings - split beacon around sequence number field
    		beaconp1 = beacon[0:2]
    		beaconp2 = beacon[3:]
    		#signal.signal(signal.SIGINT, self.interrupt)
    		kb = KillerBee()
    		inf="\t[+]  zbstumbler: Transmitting and receiving on interface \'{0}\'".format(kb.get_dev_info()[0])
                self.emit(SIGNAL('stumbler_update(QString)'), QtCore.QString(inf))
    		# Sequence number of beacon request frame
    		seqnum = 0
    		kb.set_channel(channel)
    		count=0
		while count<1:
    			# Loop injecting and receiving packets
    			if seqnum > 255:
        			seqnum = 0

			self.emit(SIGNAL('stumbler_update(QString)'), QtCore.QString("\t[+]  Transmitting beacon request"))
    			beaconinj = ''.join([beaconp1, "%c" % seqnum, beaconp2])
    			start = time.time()

    			try:
        			txcount+=1
        			kb.inject(beaconinj)
    			except Exception, e:
        			print("ERROR: Unable to inject packet: {0}".format(e))
        			sys.exit(-1)

    			while (start+2.0 > time.time()):
        			# Does not block
        			recvpkt = kb.pnext()
        			# Check for empty packet (timeout) and valid FCS
        			if recvpkt != None and recvpkt[1]:
            				rxcount += 1
            				rf=str("\t[+]  Received frame.")#, time.time()-start
                        		self.emit(SIGNAL('stumbler_update(QString)'), QtCore.QString(rf))
            				networkdata = self.response_handler(stumbled, recvpkt[0], channel)
        			kb.sniffer_off()
        			seqnum += 1
				count=count+1
			kb.close()
			self.close()
                        self.emit(SIGNAL('stumbler_update(QString)'), QtCore.QString("Complete"))

