# IQ Sim Client 


## Install Dependancies

```
pip install -r requirements.txt
```

## Run

```
python app.py
```


# UI Design

The IQ Sim Client UI is designed using Qt Creator. You can download Qt Creator from [here](https://www.qt.io/download-open-source).

The sim_client.ui file is the UI design file. You can open and modify it using Qt Creator.


# Generate the Python GUI

After a GUI laypur is created in Qt Creator, you can generate the python file using the following command. This command will <u>overwrite</u> the existing sim_client.py file.

```sh
python3 -m PyQt5.uic.pyuic -x sim_client.ui -o sim_client.py
```

The sim_client file is then imported into the app.py file and all of the logic is written in the app.py file.


# Generate the Executable

Using PyInstaller, you can generate an executable file for the IQ Sim Client. 

```sh
python3 generate_executable.py
```