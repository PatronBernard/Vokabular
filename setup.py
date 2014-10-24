from distutils.core import setup
import py2exe

#python setup.py py2exe --includes sip
#You might have to do this too:
#http://stackoverflow.com/questions/23970240/how-to-stop-python-program-compiled-in-py2exe-from-displaying-importerror-no-mo

setup(
	windows = [

		'Vokabular.py',
		])