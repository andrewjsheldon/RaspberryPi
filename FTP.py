import ConfigParser

def ask_user(question):
	cfg = ConfigParser.ConfigParser()
	cfg.read('settings.cfg')
	ftp = cfg.getint('Athlete', 'FTP')
	
	updFTP = None
	print "Current FTP is",ftp
	updFTP = str(raw_input(question + " (y/n): ")).lower().strip()
	try:
		if updFTP == "y":
			try:
				ftp = int(raw_input("Enter new FTP: "))
				cfg.set('Athlete', 'FTP',str(ftp))
				with open('settings.cfg', 'w') as configfile:
					cfg.write(configfile)
				return ftp
			except ValueError:
				print("FTP must be an integer")	
		if updFTP == "n":
			ftp = ftp
			return ftp
		else:
			print("FTP must be an integer")
			return ask_user("Do you want to update your FTP?")
			
	except Exception as error:
		print("FTP must be an integer")
		print(error)
		return ask_user("Do you want to update your FTP?")
		
ftp = ask_user("Do you want to update your FTP?")	

z1_start = 0
z1_end = ftp*0.55

z2_start = ftp*0.55
z2_end = ftp*0.75

z3_start = ftp*0.75
z3_end = ftp*0.90

z4_start = ftp*0.90
z4_end = ftp*1.05

z5_start = ftp*1.05
z5_end = ftp*1.2


print "FTP is :",ftp

print "Zone 1 is :",z1_start,"to",z1_end
print "Zone 2 is :",z2_start,"to",z2_end
print "Zone 3 is :",z3_start,"to",z3_end
print "Zone 4 is :",z4_start,"to",z4_end
print "Zone 5 is :",z5_start,"to",z5_end
