from PyQt5 import QtWidgets
from PyQt5 import QtGui
from sim_client import Ui_MainWindow
import sys
import requests
import subprocess

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    mavp2p_process = None
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QtGui.QIcon('imgs/icon.png'))
        self.setupUi(self)
        self.connect_pb.clicked.connect(self.connect)   
        self.disconnect_pb.clicked.connect(self.disconnect)

    def request_port(self, uuid):
        print("requesting sim data")
        URL = "http://164.92.100.229:5000/get_port"
        PARAMS = {'uuid':uuid}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        print(data)

        return data['port']

    def run_mavp2p(self, port):
        # tcpc:164.92.113.203:30771 udpc:127.0.0.1:14550
        self.mavp2p_process = subprocess.Popen(["./mavp2p_linux/mavp2p", f"tcpc:164.92.113.203:{port}", "udpc:127.0.0.1:14550" ])

    def connect(self):
        uuid = self.sim_uuid_le.text()
        print(f"uuid {uuid}")
        self.disconnect()
        port = self.request_port(uuid)
        self.run_mavp2p(port)

    def disconnect(self):
        if self.mavp2p_process: 
            print("disconnecting")
            self.mavp2p_process.terminate()
            self.mavp2p_process = None
        
        print("done")
        return
    

def main():

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
    window.disconnect()


if __name__ == '__main__':
    main()