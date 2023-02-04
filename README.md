# airTrackerEval

Dieses Ropository beinhaltet die gemessenen Kohlenstoffdioxid-Konzentrationen über 1.5 Monate in einer Kita in der Ostschweiz, Skripte um diese Daten aufzubereiten und die daraus erstellten Plots.

## datasets
Beinhaltet die gesamelten Rohdaten. Die Wochenenden sind in einem Unterordner aussortiert, da zu dieser Zeit keine Personen in der Kita waren. Die Einträge für Kohlenstoffdioxid, Druck und Temperatur sind tasächlich gemessene Werte, die Luftfeuchtigkeit ist ein Dummy-Wert, der im auf Grund der Architektur des Messgerätes eingefügt wird. Die Temperatur-Werte sind durch die Abwärme der CPU erhöht.

## plots
Beinhaltet die Plots aus den gesammelten Rohdaten

## sampledDownDataSets
Beinhaltet aufbereitete Datensets und die plots dazu

## downSampeling.py
Skript um die Daten herunter zu skalieren

## main.py
Hat einige Skripte, um die plots zu generieren.
