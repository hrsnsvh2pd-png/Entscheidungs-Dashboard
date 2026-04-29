# Entscheidungs-Dashboard

[![Grafana](https://img.shields.io/badge/Grafana-OSS-orange?logo=grafana)](https://grafana.com/)
[![Database](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)](https://sqlite.org/)
[![Weather](https://img.shields.io/badge/Data-Open--Meteo-00AEEF)](https://open-meteo.com/)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

Ein datenbasiertes Entscheidungsunterstützungssystem für den **vorausschauenden Betrieb von Wärmepumpen** auf Basis von Wetterprognosen, PV-Ertrag und Betriebsdaten.

**Prinzip**

> Algorithmus schlägt vor – Nutzer entscheidet.

---

<img width="582" height="780" alt="Dashboard" src="https://github.com/user-attachments/assets/dd1bec68-48f9-4458-85aa-330077538c63">

---

Das Entscheidungs-Dashboard ergänzt mein weiteres Projekt:

👉 https://github.com/hrsnsvh2pd-png/Entscheidungs-Dashboard

---

# Features

- 48-Stunden Entscheidungsprognose für Wärmepumpenbetrieb  
- Integration von Wetterprognosen und PV-Nutzungsfenstern  
- transparente Entscheidungslogik (keine Blackbox)  
- Visualisierung über Grafana OSS  
- vollständig lokal betreibbar  
- Nutzung vorhandener Wärmepumpen-Betriebsdaten  

---

# Kernidee

Algorithmus schlägt vor – Nutzer entscheidet.

Statt komplexer Automatisierung liefert das System **klare Handlungsempfehlungen für die nächsten 48 Stunden**:

- Heizen verschieben
- PV nutzen
- Heizen vorziehen
- keine Veränderung

---

# Ziel

- bessere Nutzung von PV-Ertrag
- Reduktion ineffizienter Heizphasen
- transparente Entscheidungsgrundlage
- keine Blackbox-Automation

---

# Projekt enthält

- Grafana Dashboard (JSON)
- SQLite Datenbankstruktur
- Importskripte (Wetter + Betriebsdaten)
- Installationsanleitung
- txt-Dateien mit SQL-Statements zum Anlegen der fehlenden view in viessmann_events.db

---

# 1. Vorbemerkung

> „Für das Vergangene gibt der Kaufmann nichts.“  
> — Eugen Schmalenbach  
> *Die Werte von Anlagen und Unternehmungen in der Schätztechnik*,  
> Zeitschrift für handelswirtschaftliche Fragen (ZfhF), 1917/1918

Die effiziente Steuerung einer Wärmepumpe ist in der Praxis oft überraschend reaktiv:  
Entscheidungen basieren meist auf aktuellen Temperaturen oder Bauchgefühl – obwohl eigentlich eine vorausschauende Betrachtung von Wetter, PV-Ertrag und Gebäudeverhalten notwendig wäre.

Genau hier setzt dieses Projekt an.

---

# Idee

Das Entscheidungs-Dashboard ist ein bewusst **einfach gehaltener, aber datengetriebener Entscheidungsassistent für Wärmepumpenbetrieb**.

Statt eine komplexe KI-Steuerung zu versuchen, setzt es auf ein pragmatisches Prinzip:

**Algorithmus schlägt vor – Nutzer entscheidet.**

Ziel ist es, mit einem transparenten und nachvollziehbaren Ansatz einen großen Teil des praktischen Optimierungspotenzials nutzbar zu machen, ohne die Kontrolle aus der Hand zu geben.

Die verarbeiteten Daten stehen in einer separaten SQLite-Datenbank (`entscheidungs_dashboard.db`).  
Ergänzende Verschleiß- und Betriebsdaten werden synchron (stündlich) aus der `viessmann_events.db` (`vieventlog`) gelesen.

---

# Funktionsweise

<img width="1013" height="807" alt="Funktionsweise" src="https://github.com/user-attachments/assets/1acc07ef-7d90-4513-b512-f599b4323eab">
<br>

Das Dashboard verarbeitet **stündlich aktualisierte Wetterprognosedaten (Open-Meteo)** und kombiniert diese mit Betriebsdaten der Wärmepumpe.

Auf dieser Basis werden für einen Zeitraum von **48 Stunden** vier klare Handlungsempfehlungen abgeleitet:

- Heizen verschieben
- PV-Energie nutzen
- Heizen vorziehen
- Keine Änderung

Wenn die Bedingungen für **Solarthermienutzung** erfüllt sind  
(z. B. ausreichend Sonneneinstrahlung und geeignete Pufferspeichertemperatur),  
wird die aktive Handlungsempfehlung durch **„Solarthermie“** übersteuert.

Zusätzlich werden unterstützende Informationen bereitgestellt:

- Komfortzeitfenster (wann Heizen sinnvoll ist)
- Zeit bis zum nächsten PV-Nutzungsfenster
- Temperaturtrend-Entwicklung
- Einfluss solarthermischer Komponenten
- relevante Betriebsdaten der Wärmepumpe
- Sonneneinstrahlung zur Bewertung der Solarthermienutzbarkeit

Damit entsteht **kein Automatismus**, sondern eine **Entscheidungsunterstützung mit Kontext**.

---

# Entscheidungsprinzip

Das System folgt einer bewusst einfachen, robusten Regelstruktur:

- zweistufiger Entscheidungsprozess
- algorithmische Empfehlung
- nutzerbasierte finale Entscheidung

Damit bleibt die Kontrolle immer beim Betreiber – bei gleichzeitig deutlich besserer Informationsbasis.

---

# Datenbasis

Das Dashboard basiert auf:

- Wetterprognosen von  **Open-Meteo**  (stündlich aktualisiert)
- lokalen Betriebsdaten der Wärmepumpe
- einer SQLite-Datenbank zur lokalen Verarbeitung
- Visualisierung über **Grafana OSS**

Die Datenverarbeitung ist so aufgebaut, dass **unnötige API-Calls an die Viessmann Cloud vermieden werden**.

---

# Integration Viessmann / vieventlog

Für die Wärmepumpendaten wird optional das Open-Source-Projekt **vieventlog** verwendet.

Ein besonderer Dank gilt dem Entwickler für die Bereitstellung dieses Projekts für die Community.

Alternativ wäre auch ein direkter Zugriff über die **Viessmann Cloud API** möglich – dieser Weg ist hier jedoch nicht implementiert.

---

# Repository

GitHub Repository:

https://github.com/hrsnsvh2pd-png/Entscheidungs-Dashboard

Dieses Repository enthält:

- Grafana Dashboard (JSON)
- leere SQLite Datenbank (Minimalstruktur)
- Skripte für Datenimport (Wetter & Betriebsdaten)
- ausführliche Installationsbeschreibung
- txt-Dateien mit SQL-Statements zum Generieren der fehlenden view in viessmann_events.db

---

# Lizenz

Alle Inhalte stehen unter der

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

https://creativecommons.org/licenses/by/4.0/legalcode

---

# Projektziel

Dieses Dashboard ist ein praktischer Versuch, die Lücke zwischen

- theoretisch optimaler Wärmepumpensteuerung

und

- realer, nutzergetriebener Bedienung

zu verkleinern.

Es ersetzt keine vollautomatische Optimierung –  
aber es macht Entscheidungen deutlich besser begründet und nachvollziehbarer.

---

# Feedback willkommen

Ich freue mich über Rückmeldungen, Kritik und Ideen aus der Community – insbesondere zu

- Erweiterungen
- Optimierungslogik
- praktischen Erfahrungen im Betrieb.

---

# 2. Installation

1. Dateien aus dem Repository herunterladen  
2. Grafana installieren  
3. Dashboard JSON importieren  
4. SQLite Datenbank konfigurieren
5. Fehlende Views in der viessmann_events.db generieren (2 views). 
6. Import-Skripte anpassen  
7. CRON Jobs einrichten  

Eine ausführliche Installationsbeschreibung befindet sich in der Datei:

**Entscheidungs-Dashboard.pdf → Kapitel Installation**

---

# 3. Lizenz- und Haftungsbestimmungen

## 3.1 Nutzung von Grafana

Dieses Dashboard wurde für die Nutzung mit Grafana OSS entwickelt, einem Produkt der Grafana Labs.

Grafana OSS ist lizenziert unter der:

**GNU Affero General Public License v3.0 (AGPLv3)**

Quellcode:

https://github.com/grafana/grafana

Lizenztext:

https://www.gnu.org/licenses/agpl-3.0.txt

Dieses Repository enthält **keine modifizierte Version von Grafana**.  
Jeder Nutzer ist verpflichtet, eine eigene Grafana-Installation bereitzustellen.

---

## 3.2 Abhängigkeit von vieventlog

Zur Nutzung des Dashboards muss auf Daten aus der Datei **viessmann_events.db** zugegriffen werden, die durch die Software **vieventlog** erzeugt wird.

vieventlog ist ein Open-Source-Projekt von **Matthias Schneider**.

Repository:

https://github.com/mschneider82/vieventlog

Lizenz:

MIT License  
https://mit-license.org

Dieses Projekt ist **unabhängig von vieventlog** und steht in keiner organisatorischen Verbindung zu dessen Autor.

---

## 3.3 Lizenz dieses Repositories

Die enthaltenen Dateien (Dashboard-JSON, Datenbank, Skripte) stehen unter:

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

https://creativecommons.org/licenses/by/4.0/legalcode

Erlaubt:

- Nutzung
- Weitergabe
- Bearbeitung
- erneute Veröffentlichung

**Namensnennung erforderlich.**

© 2026 Hans-Hermann Gröger

---

## 3.4 Haftungsausschluss

Die Bereitstellung erfolgt **unentgeltlich und ohne Gewähr**.

Der Autor haftet nicht für Schäden, die aus der Nutzung der Repository-Dateien entstehen, soweit gesetzlich zulässig.

Der Nutzer ist selbst verantwortlich für:

- Installation
- Konfiguration
- Datensicherung
- Systemsicherheit

---

## 3.5 Kein Support

Ein Anspruch auf Support, Wartung oder Weiterentwicklung besteht nicht.

---

## 3.6 Keine Verbindung zu Grafana Labs

Dieses Projekt steht in **keiner Verbindung zu Grafana Labs** und wird von diesem Unternehmen weder unterstützt noch zertifiziert.

Alle Produkt- und Markennamen sind Eigentum ihrer jeweiligen Inhaber.

**English Version:**

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

Users are responsible for compliance with applicable laws and licenses.

5. No Affiliation

This project is not affiliated with, endorsed by, sponsored by, or otherwise associated with Grafana Labs.

All product names, trademarks, and registered trademarks mentioned are the property of their respective owners.
   
