# Entscheidungs-Dashboard
Ein datenbasiertes Entscheidungsunterstützungssystem zur optimierten Steuerung von Wärmepumpen auf Basis von Wetterprognosen, PV-Ertrag und Betriebsdaten.<br>

<img width="582" height="780" alt="image" src="https://github.com/user-attachments/assets/dd1bec68-48f9-4458-85aa-330077538c63" /> <br>
<br>
Das Entscheidungs-Dashboard ergänzt mein Alternatives Dashboard. <br> 
(vgl. https://github.com/hrsnsvh2pd-png/Alternatives-Dashboard  ) <br>
<br>
Das Dashboard kombiniert
- stündliche Wetterprognosen (Open-Meteo)
- Wärmepumpen-Betriebsdaten (via lokaler Datenbank)
- Visualisierung in Grafana OSS
- einfache, transparente Entscheidungslogik

### Kernidee

Algorithmus schlägt vor – Nutzer entscheidet.<br>

Statt komplexer Automatisierung liefert das System klare Handlungsempfehlungen für die nächsten 48 Stunden: <br>

- Heizen verschieben
- PV nutzen
- Heizen vorziehen
- keine Veränderung

### Ziel

 - bessere Nutzung von PV-Ertrag
 - Reduktion ineffizienter Heizphasen
 - transparente Entscheidungsgrundlage
 - keine Blackbox-Automation

### Projekt enthält

 - Grafana Dashboard (JSON)
 - SQLite Datenbankstruktur
 - Importskripte (Wetter + Betriebsdaten)
 - Installationsanleitung



## 1. Vorbemerkung
„Für das Vergangene gibt der Kaufmann nichts.“ - Eugen Schmalenbach, Die Werte von Anlagen und Unternehmungen in der Schätztechnik, Zeitschrift für handelswirtschaftliche Fragen (ZfhF) 1917/1918, S. 1 ff.

Die effiziente Steuerung einer Wärmepumpe ist in der Praxis oft überraschend reaktiv: Entscheidungen basieren meist auf aktuellen Temperaturen oder Bauchgefühl – obwohl eigentlich eine vorausschauende Betrachtung von Wetter, PV-Ertrag und Gebäudeverhalten notwendig wäre.

Genau hier setzt dieses Projekt an.<br>
<rb>

### Idee
Das Entscheidungs-Dashboard ist ein bewusst einfach gehaltener, aber datengetriebener Entscheidungsassistent für Wärmepumpenbetrieb. <br>

Statt eine komplexe KI-Steuerung zu versuchen, setzt es auf ein pragmatisches Prinzip:<br>

Algorithmus schlägt vor – Nutzer entscheidet. <br>

Ziel ist es, mit einem transparenten und nachvollziehbaren Ansatz einen großen Teil des praktischen Optimierungspotenzials nutzbar zu machen, ohne die Kontrolle aus der Hand zu geben.
<br>

Die verarbeiteten Daten stehen in einer separaten SQLite-Datenbank (entscheidungs_dashboard.db), die ergänzend für die Beurteilung der vorgeschlagenen Aktion verwendeten Verschleiß- und Betriebsdaten werden synchron (stündlich) aus der viessmann_events.db (vieventlog) gelesen.<br>



### Funktionsweise
<br>
<img width="1013" height="807" alt="image" src="https://github.com/user-attachments/assets/1acc07ef-7d90-4513-b512-f599b4323eab" />
<br>
Das Dashboard verarbeitet stündlich aktualisierte Wetterprognosedaten (Open-Meteo) und kombiniert diese mit Betriebsdaten der Wärmepumpe.>br

Auf dieser Basis werden für einen Zeitraum von 48 Stunden vier klare Handlungsempfehlungen abgeleitet:

 - Heizen verschieben
 - PV-Energie nutzen
 - Heizen vorziehen
 - Keine Änderung
<br>
Soweit die Grenzen für eine Solarthermie-Nutzung (Sonneneinstrahlung, Pufferspeichertemperatur) erreicht werden, wird die aktive Handlungsempfehlung durch "Solarthermie" overruled. <br>
<br>
Zusätzlich werden unterstützende Informationen bereitgestellt, z. B.:

 - Komfortzeitfenster (wann Heizen sinnvoll ist)
 - Zeit bis zum nächsten PV-Nutzungsfenster
 - Temperaturtrend-Entwicklung
 - Einfluss solarthermischer Komponenten
 - relevante Betriebsdaten der Wärmepumpe
 - Sonnenseinstrahlung (für Solarthermienutzbarkeit)
<br>
Damit entsteht kein Automatismus, sondern eine Entscheidungsunterstützung mit Kontext. <br>

### Entscheidungsprinzip
Das System folgt einer bewusst einfachen, robusten Regelstruktur:

 - 2-stufiger Entscheidungsprozess
 - Algorithmische Empfehlung
 - Nutzerbasierte finale Entscheidung

Damit bleibt die Kontrolle immer beim Betreiber – bei gleichzeitig deutlich besserer Informationsbasis.
Datenbasis <br>

Das Dashboard basiert auf:

 - Wetterprognosen von Open-Meteo (stündlich aktualisiert)
 - lokalen Betriebsdaten der Wärmepumpe
 - einer SQLite-Datenbank zur lokalen Verarbeitung
 - Visualisierung über Grafana OSS
<br>
Die Datenverarbeitung ist so aufgebaut, dass unnötige API-Calls an die Viessmann Cloud vermieden werden.<br>

### Integration Viessmann / vieventlog
Für die Wärmepumpendaten wird optional das Open-Source-Projekt
vieventlog verwendet. <br>

Ein besonderer Dank gilt dem Entwickler für die Bereitstellung dieses Projekts für die Community.<br>

Alternativ wäre auch ein direkter Zugriff über die Viessmann Cloud API möglich – dieser Weg ist hier jedoch nicht implementiert.<br>

### Projekt
Das Projekt ist hier veröffentlicht:<br>

  https://github.com/hrsnsvh2pd-png/Entscheidungs-Dashboard
<br>

Enthalten sind:
 - Grafana Dashboard (JSON)
 - leere SQLite-Datenbank (mit Minimalstruktur)
 - Skripte für Datenimport (Wetter & Betriebsdaten)
 - ausführliche Installationsbeschreibung <br>

### Lizenz
Alle Inhalte stehen unter der<br>
Creative Commons Attribution 4.0 International (CC BY 4.0) <br>
https://creativecommons.org/licenses/by/4.0/legalcode <br>

### Ziel des Projekts
Dieses Dashboard ist ein praktischer Versuch, die Lücke zwischen:
 - theoretisch optimaler Wärmepumpensteuerung <br>
und
 - realer, nutzergetriebener Bedienung

zu verkleinern. <br>

Es ersetzt keine vollautomatische Optimierung – aber es macht Entscheidungen deutlich besser begründet und nachvollziehbarer. <br>

### Feedback willkommen

Ich freue mich über Rückmeldungen, Kritik und Ideen aus der Community – insbesondere zu Erweiterungen, Optimierungslogik und praktischen Erfahrungen im Betrieb.


## 2. Installation
Die Installation des Entscheidungs-Dashboards läuft wie folgt ab: <br>
1. Auslieferung
   Die Auslieferung umfasst
   - Dashboard-JSON zum Upload in Grafana
   - Leere SQLite-Datenbankdatei entscheidungs_dashboard.db (Ausnahme Tabelle meta_config)
   - Skript-Dateien für den Import der Wetterdaten und Systemparameter
   - Dokumentation und ausführliche Hinweise: Entscheidungs-Dashboard.pdf <br>
2. Dateien auf den Rechner kopieren
3. Grafana installieren
   vgl. dazu die ausführliche Anleitung im Dokument Entscheidungs-Dashboard.pdf <br>
5. Dashboard JSON in GRAFANA importieren
   vgl. dazu die ausführliche Anleitung im Dokument Entscheidungs-Dashboard.pdf <br>
   Bitte beachten: <br>
   - Bei der Anlage der "neu Datasource" ist der Pfad zur eintscheidungs_dashboard.db einzutragen
   - Variable ""Anlage": Diese Variable **muss** aktualisiert werden, das sonst keine Betriebsdateb angezeigt werden.     Hier ist im Feld "Query" folgendes SQL-Statement einzutragen: <br>
   select  installation_id from temperature_snapshots group by  installation_id <br>
   - Link "Dashboard": Falls ein zusätzliches Dashboard genutzt wird. ist hier der http-Link zum Dashboard einzutragen <br>
6. Die Skript-Dateien anpassen und CRON-Jobs einrcihten
   Vgl. dazu die ausführliche Anleitung in der Datei Entscheidungs-Dashboard.pdf <br>
7. Skripte testen <br>
8. Dashboard starten und Zeitfilter einrichten
   Hinweis: Der Zeitfilter **muss** unbedingt eingestellt werden auf
   - From: now
   - To: now+48h (ohne Leerzeichen dazwischen) <br>
   Sonst wird der Prognosezeitraum im Dashboaerd nicht ordentlich angezeigt.
<br>

## 3. Lizenz- und Haftungsbestimmungen
Deutschsprachige Version: <br>
<br>

3.1 Nutzung von Grafana

Dieses Dashboard wurde für die Nutzung mit Grafana OSS entwickelt, einem Produkt der Grafana Labs.

Grafana OSS ist lizenziert unter der
GNU Affero General Public License v3.0 (AGPLv3).

Der Quellcode ist öffentlich verfügbar unter:
https://github.com/grafana/grafana

Die Lizenzbedingungen sind abrufbar unter:
https://www.gnu.org/licenses/agpl-3.0.txt

Dieses Repository enthält keine modifizierte Version von Grafana.
Jeder Nutzer ist verpflichtet, eine eigene Grafana-Installation bereitzustellen.

Eine Verpflichtung zur Offenlegung eigener Anpassungen entsteht nur im Rahmen der AGPL-Bestimmungen und betrifft ausschließlich Modifikationen an der AGPL-lizenzierten Software selbst.

3.2 Abhängigkeit von vieventlog

Zur Nuzung des Dashboards muss auf Daten aus der Datei viessmann_events.db zugegriffen werden, die durch die Software
vieventlog erzeugt und fortgeschrieben wird.

vieventlog ist ein Open-Source-Projekt von Matthias Schneider.

Der vollständige Quellcode ist verfügbar unter:
https://github.com/mschneider82/vieventlog

vieventlog steht unter der MIT License.

Die MIT Lizenzbedingungen sind abrufbar unter:
https://mit-license.org

Dieses Projekt ist unabhängig von vieventlog und steht in keiner geschäftlichen oder organisatorischen Verbindung zu dessen Autor.

3.3 Lizenz dieses Repositories

Die in diesem Repository enthaltenen Grafana-Dashboard-JSON-, Datenbank- und Skript-Dateien (zusammen: Repository-Dateien) stehen unter der Creative Commons Attribution 4.0 International (CC BY 4.0).

Die Lizenzbedingungen können hier abgerufen werden:
https://creativecommons.org/licenses/by/4.0/legalcode

Innerhalb der Lizenz ist Folgendes erlaubt:
	•	Nutzung der Dashboard-Dateien
	•	Weitergabe an Dritte
	•	Bearbeitung / Anpassung der Dateien
	•	Redistribution / erneute Veröffentlichung

Namensnennung des Urhebers ist erforderlich.

© 2026 Hans-Hermann Gröger

3.4 Haftungsausschluss

Die Bereitstellung der Repository-Dateien erfolgt unentgeltlich.

Eine Haftung für Sach- oder Rechtsmängel ist ausgeschlossen, sofern nicht Vorsatz oder grobe Fahrlässigkeit vorliegt.

Für Schäden, die aus der Nutzung oder Nichtnutzung der bereitgestellten Inhalte entstehen, wird – außer in Fällen zwingender gesetzlicher Haftung – keine Haftung übernommen.

Der Nutzer ist selbst verantwortlich für:
- Installation
- Konfiguration
- Datensicherung
- Systemsicherheit

3.5 Kein Support

Ein Anspruch auf Support, Wartung oder Weiterentwicklung besteht nicht.

3.6 Keine Verbindung zu Grafana Labs

Dieses Projekt steht in keiner Verbindung zu Grafana Labs und wird von diesem Unternehmen weder unterstützt noch zertifiziert.

Alle Produkt- und Markennamen sind Eigentum ihrer jeweiligen Inhaber.

English Version:

1. Grafana Dependency

This dashboard was developed for use with Grafana OSS, a product of Grafana Labs.

Grafana OSS is licensed under the
GNU Affero General Public License v3.0 (AGPLv3).

The full source code of Grafana is available at:
https://github.com/grafana/grafana

The AGPLv3 license text is available at:
https://www.gnu.org/licenses/agpl-3.0.txt

This repository does not contain, distribute, or modify Grafana itself.
Users must install and maintain their own Grafana instance.

Under the AGPL, disclosure obligations apply only to modifications of AGPL-licensed software. This repository contains configuration and dashboard files only and does not modify Grafana.

2. Database Dependency

The dashboard needs to import data from the file viessmann_events.db, which is generated and maintained by
vieventlog.

vieventlog is an open-source project developed by Matthias Schneider.

The source code is available at:
https://github.com/mschneider82/vieventlog

vieventlog is licensed under the MIT License.

The MIT license text is available at:
https://mit-license.org

This project is independent from vieventlog and is not affiliated with its author.

3. License of This Repository

All Grafana dashboard JSON files, database files and script files (together: Repository Files) contained in this repository are licensed under:

Creative Commons Attribution 4.0 International (CC BY 4.0)

Full license text:
https://creativecommons.org/licenses/by/4.0/legalcode

You are free to:
- Use
- Share
- Modify
- Redistribute

Attribution to the original author is required.

© 2026 Hans-Hermann Gröger

4. Disclaimer

THE REPOSITORY FILES ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.

TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, THE AUTHOR SHALL NOT BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT, OR OTHERWISE, ARISING FROM OR IN CONNECTION WITH THE SOFTWARE OR ITS USE.

The user is solely responsible for:
- Installation
- Configuration
- Data backup
- System security

Compliance with applicable laws and licenses

5. No Affiliation

This project is not affiliated with, endorsed by, sponsored by, or otherwise associated with Grafana Labs.

All product names, trademarks, and registered trademarks mentioned are the property of their respective owners.
   
