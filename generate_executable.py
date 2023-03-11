import os
import shutil
import sys
import platform
import distro

def main():
    try:
        shutil.rmtree("iq_sim_client")
    except:
        print("no directory iq_sim_client")

    try:
        os.remove("iq_sim_client.zip")
    except:
        print("no file iq_sim_client.zip")

    if sys.platform == "linux" or sys.platform == "linux2":
        shutil.copytree("mavp2p/mavp2p_linux",
                        "iq_sim_client/mavp2p/mavp2p_linux")
        output_filename = "iq_sim_client_linux"
        distro_name = distro.name(pretty=True).replace(" ", "_").replace(".", "_")
        print(distro_name)
        output_filename = output_filename + "_" + distro_name 
    elif sys.platform == "darwin":
        print("todo")
        return
    elif sys.platform == "win32":
        shutil.copytree("mavp2p/mavp2p_windows",
                        "iq_sim_client/mavp2p/mavp2p_windows")
        output_filename = "iq_sim_client_windows"

    os.system("pyinstaller -F app.py --distpath iq_sim_client")

    shutil.copytree("imgs", "iq_sim_client/imgs")
    shutil.make_archive(output_filename, 'zip', "iq_sim_client")


if __name__ == "__main__":
    main()
