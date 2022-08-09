from PyQt5 import QtWidgets
from PyQt5 import QtGui
from sim_client import Ui_MainWindow
import sys
import requests
import subprocess
import os
from sys import platform


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    mavp2p_process = None
    api_ip = "intelligentquads.com"
    # TODO make node_ip querryable
    node_ip = "164.92.113.203"
    http = "https"

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QtGui.QIcon('imgs/icon.png'))
        self.setupUi(self)
        self.connect_pb.clicked.connect(self.connect)
        self.disconnect_pb.clicked.connect(self.disconnect)
        test_env = os.getenv('TEST_ENV')
        print(f"test env {test_env}")
        if test_env == "TRUE":
            self.api_ip = "localhost"
            self.http = "http"

    def request_port(self, uuid):
        print(f"requesting sim data from {self.api_ip}")
        URL = f"{self.http}://{self.api_ip}/get_port"
        PARAMS = {'uuid': uuid}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        print(data)

        return data['port']

    def run_mavp2p(self, port):
        # tcpc:164.92.113.203:30771 udpc:127.0.0.1:14550
        client1_ip = self.mavlink1_ip.text()
        client1_port = self.mavlink1_port_le.text()

        client2_ip = self.mavlink2_ip.text()
        client2_port = self.mavlink2_port_le.text()

        client3_ip = self.mavlink3_ip.text()
        client3_port = self.mavlink3_port_le.text()

        if platform == "linux" or platform == "linux2":
            mavp2p_path = "./mavp2p/mavp2p_linux/mavp2p"

        elif platform == "darwin":
            print("todo")
            return
        elif platform == "win32":
            mavp2p_path = "./mavp2p/mavp2p_windows/mavp2p"

        self.mavp2p_process = subprocess.Popen(
            [f"{mavp2p_path}", f"tcpc:{self.node_ip}:{port}", f"udpc:{client1_ip}:{client1_port}", f"udpc:{client2_ip}:{client2_port}", f"udpc:{client3_ip}:{client3_port}"])

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
