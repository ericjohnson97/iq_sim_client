import os
import shutil
from sys import platform


def main():
    try:
        shutil.rmtree("iq_sim_client")
    except:
        print("no directory iq_sim_client")

    try:
        os.remove("iq_sim_client.zip")
    except:
        print("no file iq_sim_client.zip")

    if platform == "linux" or platform == "linux2":
        shutil.copytree("mavp2p/mavp2p_linux",
                        "iq_sim_client/mavp2p/mavp2p_linux")
    elif platform == "darwin":
        print("todo")
        return
    elif platform == "win32":
        shutil.copytree("mavp2p/mavp2p_windows",
                        "iq_sim_client/mavp2p/mavp2p_windows")

    os.system("pyinstaller -F app.py --distpath iq_sim_client")

    shutil.copytree("imgs", "iq_sim_client/imgs")
    shutil.make_archive("iq_sim_client", 'zip', "iq_sim_client")


if __name__ == "__main__":
    main()
