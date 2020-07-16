import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_mainwin
import sys

#wh_info = 'https://discordapp.com/api/webhooks/' ¯\_(ツ)_/¯

def connect_whook():                                                                                     
    wh_info = requests.get(ui.url_line.text()).json()
    ui.name_line.setText(str(wh_info['name']))


def send_msg():
	requests.post(ui.url_line.text(), json={
		'username': ui.name_line.text(),
		'avatar_url': ui.avatar_line.text(),
		'content': ui.msg_box.toPlainText(),
		'tts': 'false'
		})
	ui.msg_box.clear()


def send_msg_tts():
	requests.post(ui.url_line.text(), json={
		'username': ui.name_line.text(),
		'avatar_url': ui.avatar_line.text(),
		'content': ui.msg_box.toPlainText(),
		'tts': 'true'
		})
	ui.msg_box.clear()


app = QtWidgets.QApplication(sys.argv)
mainwin = QtWidgets.QDialog()
ui = Ui_mainwin()
ui.setupUi(mainwin)
mainwin.show()

#main code
ui.connect_btn.clicked.connect(connect_whook)
ui.send_btn.clicked.connect(send_msg)
ui.sendtts_btn.clicked.connect(send_msg_tts)

sys.exit(app.exec_())
