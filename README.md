# !!! Achtung nach Fehler enthalten!!!
# Good site to follow for setup: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/
# PC Einrichten
# 1. Anaconda installieren

Download Anaconda von https://www.anaconda.com/products/individual

Anaconda Package installieren unter C:\Anaconda.

Beim Isnstallieren, sollte das Häcken für das automatische Setzen der systemeviroment Pfade, gesetzt werden.

Unter Suche in Windows die Systemungebungsvariabel, Klicke auf Umgebungsvariablen, unter den Systemvariabeln such "Path" doppelklick darauf, sollten folgende Einträge zu finde n sein. Fehlende einfach manuell nachtragen.

![image](https://user-images.githubusercontent.com/84871742/120812007-e1b73a00-c54c-11eb-8184-27be9191347a.png)


# 2. GPU Einbinden
Dazu muss das passende Nividia Cuda-Toolkit installiert werden. Da hier später Tensorflow 2.4.1 genutzt wird muss das Cuda-Toolkit 11.0.

![image](https://user-images.githubusercontent.com/84871742/120808852-c72f9180-c549-11eb-8972-de28324aa56a.png)


Also download und installieren von CUDA-Tollkit 11.0 . Downlaod von https://developer.nvidia.com/cuda-11.0-update1-download-archive
Beim Installieren den Häcken für die Umgebungsvariablen setzen.

Download cuDNN 8.0.4 for CUDA 11.0 (Eventuell ist eine Membership notwendig.)
Jetzt können wir schonmal einen Tensorflow Ordner anlegen:

- C:\Tensorflow2
- dort einen Unterordner /CUDNN  anlegen und cudnn-11.0-windows-x64-v8.0.4.30  dort hin entpacken.
- der Pfad muss noch zu den Systmvariablen zu gefügt werden. (Suche in Windows die Systemungebungsvariabel, Klicke auf Umgebungsvariablen, unter den Systemvariabeln such "Path" doppelklick darauf, und dort ein neuen Eintrag mit z.B. "C:\Tensorflow2\CUDNN/bin")

Danach sollten folgende Einträge zu finden sein.

![image](https://user-images.githubusercontent.com/84871742/120811715-92710980-c54c-11eb-9575-4cf58be77133.png)


# 3. Tensorflow2 API

Clone Tensorflow Repository  https://github.com/tensorflow/models

Zum Beispiel durch Button "Code" dann "Download Zip".
Entpacken des Zip Ordners nach C:\Tensorflow2

3.a Protobuf Dateien Compilieren

Dazu auf https://github.com/protocolbuffers/protobuf/releases gehen und die entsprechende protoc-*-*.zip release (e.g. protoc-3.12.3-win64.zip for 64-bit Windows) runterladen.

Die Dateien von protoc-*-*.zip  entpacken in einen Ordner der Wahl (z.B. C:\Tensorflow2\protoc)
Dieser Pfad muss dann zu den Systmvariablen zu gefügt werden. (Suche in Windows die Systemungebungsvariabel, Klicke auf Umgebungsvariablen, unter den Systemvariabeln such "Path" doppelklick darauf, und dort ein neuen Eintrag mit z.B. "C:\Tensorflow2\protoc")

Es sollte der Eintrag zu finden sein:

![image](https://user-images.githubusercontent.com/84871742/120811826-b46a8c00-c54c-11eb-9b88-338ecf18a53a.png)

Weitere Umgebungsvariablen die fehlen könnten, sind eventuele später nachzutragen:
- C:/Tensorflow2/models/research/
- C:/Tensorflow2/models/research/slim
- C:/Tensorflow2/models/research/object_detection

Jetzt können wir ein Terminal öffene cmd oder anaconda-prompt und folgende Befehle ausführen:

- cd C:/Tensorflow2/models/research/

- for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.

Danach sollte im Ordner C:/Tensorflow2/models/research/object_detection\protos\   für jeder -protoc Datei  auch eine .py Datei vorhanden sein.

3.b Object_detection API installieren

gehe zu “C:\Tensorflow2\models-master\research\object_detection\packages\tf2\”   und kopiere die setup.py  nach “C:\Tensorflow2\models-master\research\"
In der kopierten setup.py ändern wir unter REQUIRED_PACKAGES dann noch die Zeile  'pycocotools'  zu #'pycocotools'  damit wird das Packet nicht installiert. Das machen wir später extra.

Jetzt können wir ein Terminal öffene cmd oder anaconda-prompt und folgende Befehle ausführen:

- conda create --name tf2_env python==3.8

- activate tf2_env

- pip install tensorflow==2.4.1

- cd C:/Tensorflow2/models-master/research/

- python -m pip install .


3.c pycocotolls installieren

Diese werden zum ausführlichen Aufnehmen von Evaluierungsdaten benötigt.
Dazu clone das offizele Reprository von https://github.com/cocodataset/cocoapi,  und Entpacke es z.B. nach C:/Tensorflow2/Cocoapi-master

in der setup.py DAtei sollte noch die Zeile 
 - extra_compile_args=[] # originally was ['-Wno-cpp', '-Wno-unused-function', '-std=c99']

editiert werden, so dass sie wie gezeigt, aussieht. Wichtig ist das # zum auskommentieren der restlichen Zeile.

Dann können folgende Befehle in cmd oder anaconda-prompt ausgeführt werden.

- activate tf2_env

- cd C:\Tensorflow2\Cocoapi-master\PythonAPI

- python setup.py build_ext --inplace

2.d Hinzufügen unserer Einviroment zum juypter notebook.

Einfach den Befehl in cmd oder anaconda-prompt ausführen:

- python -m ipykernel install --user --name=tf2_env

# Object-Detection
Object Detection Tensorflow2 in jupyter notebook.

Die ganze Ordnerstruktur clonen und unter Tensorflow ablegen. ggf. den root Ordner Object-Detection umbenennen in "workspace".

Der Tensorflow2 Ordner sollte nun wie folgt aussehen:
![image](https://user-images.githubusercontent.com/84871742/120813189-f516d500-c54d-11eb-8487-50f1719ff142.png)


Das Jupyter Notebook  Object_Detection.ipynb   öffnen, am besten mit dem Anaconda Prompt:

- cd C:\Tensorflow2\workspace\training_demo

- jupyter notebook

Unter dem Menu "Kernel" sollte auch unsere Enviroment "tf2_env" zu finden sein. 

Bilder mit Label Daten unter Trainings_demo/Images  ablegen und loslegen (Wie Bilder gelabelt werden können ist im nächsten Kaptile kurz beschrieben). Achtet auf die Beschreibungen im Notebook, ggf. müssen Pfade angepasst werden.
Ebenso müssen die Labels angepasst werden in Schritt 2  Zeile 1.
In Schritt 4     müssen im vierten Unterschritt die config Daten überpfüt und ggf. angepasst werden. Aufjeden Fall muss pipeline_config.model.faster_rcnn.num_classes = xx  indivudell auf die  Anzahl der eigenen Object-Klassen angepasst werden. 
Für Schritt 5  muss ein pretrained model runter geladen werden. Dann den entsprechenden Namen in Zeile 3 angeben.

Ansonsten immer mit "Run" durch das Notebook klicken.
viel Spaß

# Bilder Labeln
Download die neueste Version von https://tzutalin.github.io/labelImg/

Entpacken alles nach z.B: C:\Tensorflow\Labeling

In dem Ordner oder Unterordner die Anwendung Labelimg.exe ausführen.
Mit Open dir zum  Ordner  "C:\Tensorflow2\workspace\training_demo\images" navigieren.

![image](https://user-images.githubusercontent.com/84871742/120816030-ac145000-c550-11eb-8cdb-24e121409835.png)


Tipp: Im Ordner  "C:\Tensorflow\Labeling"  ist irgendwo eine Datei "predefined_classes.txt" zu finden, die kann man gut an seine Klassen anpassen. 

Nun nur Bild für Bild durchklicken und mit "create RectBox"  ![image](https://user-images.githubusercontent.com/84871742/120815690-5b045c00-c550-11eb-8276-af7702ca5ab8.png)

ein Recteck um jedes Object zeichnen und die ObjectKlasse aussuchen.



