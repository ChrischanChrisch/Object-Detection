# Object-Detection
Object Detection Tensorflow2 in jupyter notebook.

Die ganze Ordnerstruktur clonen und unter Tensorflow ablegen. ggf. den root Ordnr Object-Detection umbenennen in "workspace".

Das Jupyter Notebook  Object_Detection.ipynb   öffnen, am besten mit dem Anaconda Prompt:

cd C:\Tensorflow2\workspace\training_demo

jupyter notebook


Bilder mit Label Daten unter Trainings_demo/Images  ablegen und loslegen. Achtet auf die Beschreibungen im Notebook, ggf. müssen Pfade angepasst werden.
Ebenso müssen die Labels angepasst werden in Schritt 2  Zeile 1.
In Schritt 4     müssen im vierten Unterschritt die config Daten überpfüt und ggf. angepasst werden. Aufjeden Fall muss pipeline_config.model.faster_rcnn.num_classes = xx  indivudell auf die  Anzahl der eigenen Object-Klassen angepasst werden. 
Für Schritt 5  muss ein pretrained model runter geladen werden. Dann den entsprechenden Namen in Zeile 3 angeben.

Ansonsten immer mit "Run" durch das Notebook klicken.
viel Spaß

