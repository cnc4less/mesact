import os, configparser, subprocess
from libmesact import loadini
from libmesact import utilities

def checkconfig(parent):
	config = configparser.ConfigParser()
	if os.path.isfile(os.path.expanduser('~/.config/measct/mesact.conf')):
		config.read(os.path.expanduser('~/.config/measct/mesact.conf'))
		if config.has_option('NAGS', 'MESAFLASH'):
			if config['NAGS']['MESAFLASH'] == 'True':
				parent.checkMesaflashCB.setChecked(True)
				checkmf(parent)
		if config.has_option('STARTUP', 'CONFIG'):
			if config['STARTUP']['CONFIG'] != 'False':
				loadini.openini(parent, config['STARTUP']['CONFIG'].lower())
				#loadini.openini(self, 'mesa-5i25-7i76')

	else:
		print(f'{os.path.expanduser("~/.config/measct/mesact.conf")} not found')
		config.add_section('NAGS')
		config['NAGS']['MESAFLASH'] = 'True'
		if not os.path.isdir(os.path.expanduser('~/.config/measct')):
			os.makedirs(os.path.expanduser('~/.config/measct'))
		with open(os.path.expanduser('~/.config/measct/mesact.conf'), 'w') as configfile:
			config.write(configfile)


def checkmf(parent):
	# only check to see if it's installed here
	try:
		subprocess.check_output('mesaflash', encoding='UTF-8')
	except FileNotFoundError:
		#parent.errorMsgOk(('Mesaflash not found go to\n'
		#	'https://github.com/LinuxCNC/mesaflash\n'
		#	'for installation instructions.'), 'Notice! Can Not Flash Firmware')
		t = ('Mesaflash not found go to\n'
			'https://github.com/LinuxCNC/mesaflash\n'
			'for installation instructions.\n'
			'This check can be turned off\n'
			'in the Options tab')
		parent.errorMsgOk(t,'Mesaflash')
		#parent.machinePTE.appendPlainText(t)
		parent.firmwareCB.setEnabled(False)
		parent.readpdPB.setEnabled(False)
		parent.readhmidPB.setEnabled(False)
		parent.flashPB.setEnabled(False)
		parent.reloadPB.setEnabled(False)
		parent.verifyPB.setEnabled(False)
		parent.statusbar.showMessage('Mesaflash not found!')


def getpref(parent):
	pass

'''
		try:
			version = subprocess.check_output(['mesaflash', '--version'], encoding='UTF-8')[-6:]
			print(int(version.replace('.', '')))
			if int(version.replace('.', '')) >= 343:
				parent.machinePTE.appendPlainText(f'Mesaflash Version: {version}')
				# fixme
		except:
			t = ('Mesaflash version is less than 3.4.2\n'
				'The Mesa 7i96S requires Mesaflash 3.4.2 or later.\n'
				'Go to https://github.com/LinuxCNC/mesaflash\n'
				'for installation/update instructions.')
			parent.machinePTE.appendPlainText(t)


'''
