from PyQt5 import QtWidgets
from PyQt5 import QtGui
from sim_client import Ui_MainWindow
import sys
import requests
import subprocess
import os
import distro
from pymavlink import mavutil
from sys import platform


# check if distro is ubuntu 22.04 
distro = distro.name(pretty=True).replace(" ", "_").replace(".", "_")
print(distro)
if "22_04" in distro:
    print("setting qt platform to wayland")
    os.environ['QT_QPA_PLATFORM'] = "wayland"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    mavp2p_process = None
    api_ip = "intelligentquads.com"
    # TODO make node_ip querryable
    http = "https"
    iq_sim_connection_label = "IQ SIM uuid"
    connection_options = ["udpc", "udps", "tcpc", "tcps"]
    


    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QtGui.QIcon('imgs/icon.png'))
        self.setupUi(self)
        self.connect_pb.clicked.connect(self.connect)
        self.disconnect_pb.clicked.connect(self.disconnect)
        self.define_master_connection_options()
        self.setup_master_connection_combobox(self.master_connection_cb)
        self.setup_connection_combobox(self.mavlink_1_cb)
        self.setup_connection_combobox(self.mavlink_2_cb)
        self.setup_connection_combobox(self.mavlink_3_cb)
        self.master_connection_cb.currentIndexChanged.connect(self.handle_combobox_changed)
        
        
        test_env = os.getenv('TEST_ENV')
        print(f"test env {test_env}")
        if test_env == "TRUE":
            self.api_ip = "localhost"
            self.http = "http"

    def handle_combobox_changed(self):
        print("setting new default")
        # set baud rate to 57600 if serial is selected
        master_connection_selection = self.master_connection_cb.currentText()
        if "serial" in master_connection_selection:
            self.sim_uuid_le.setText("57600")
        else:
            self.sim_uuid_le.setText("")

    def define_master_connection_options(self):
        preferred_ports = ['*FTDI*',"*Arduino_Mega_2560*","*3D*","*USB_to_UART*",'*Ardu*','*PX4*','*Hex_*','*Holybro_*','*mRo*','*FMU*','*Swift-Flyer*']
        serial_list = mavutil.auto_detect_serial(preferred_list=preferred_ports)
        self.master_connection_options = [ self.iq_sim_connection_label ]
        for device in serial_list:
            self.master_connection_options.append(f"serial:{device.device}")
        
        print(self.master_connection_options)

    def setup_master_connection_combobox(self, connection_cb):
        for con_type in self.master_connection_options:
            connection_cb.addItem(con_type)

    def setup_connection_combobox(self, connection_cb):
        for con_type in self.connection_options:
            connection_cb.addItem(con_type)

    def request_connection(self, uuid):
        print(f"requesting sim data from {self.api_ip}")
        URL = f"{self.http}://{self.api_ip}/get_connection"
        PARAMS = {'uuid': uuid}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        print(data)

        return data

    def print_subprocess_cmd(self, cmd_list): 
        cmd_str = " ".join(cmd_list)
        print(f"running {cmd_str}")

    def run_mavp2p(self, master_connection_str):
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

        
        cmd = [f"{mavp2p_path}", master_connection_str, f"udpc:{client1_ip}:{client1_port}", f"udpc:{client2_ip}:{client2_port}", f"udpc:{client3_ip}:{client3_port}"]
        # print cmd
        self.print_subprocess_cmd(cmd)

        self.mavp2p_process = subprocess.Popen(cmd)

    def connect(self):
        uuid = self.sim_uuid_le.text()
        print(f"uuid {uuid}")
        self.disconnect()

        # check if connection is to sim or to other mavlink system
        master_connection_selection = self.master_connection_cb.currentText()
        print(master_connection_selection)
        if master_connection_selection == self.iq_sim_connection_label:
            print("connecting to sim")
            data = self.request_connection(uuid)
            master_con_str = f"tcpc:{data['ip']}:{data['port']}"
            
        else:
            print("connecting to other mavlink system")
            if "serial" in master_connection_selection:
                baud = self.sim_uuid_le.text()
                master_con_str = f"{master_connection_selection}:{baud}"

        self.run_mavp2p(master_con_str)
        

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
