# Entscheidungs-Dashboard
Dieses Dashboard gibt vorausschauende Handlungsempfehlungen für den Betrieb einer Wärmepumpe auf Basis von: 

- Temperaturtrend <br>
- PV-Prognose <br>
- Betriebszustand der Heizungsanlage. <br>

Es berücksichtigt ferner die Nutzbarkeit von Solarthermie.

<img width="582" height="780" alt="image" src="https://github.com/user-attachments/assets/dd1bec68-48f9-4458-85aa-330077538c63" /> <br>
<br>
Das Entscheidungs-Dashboard ergänzt mein Alternatives Dashboard. <br> 
(vgl. https://github.com/hrsnsvh2pd-png/Alternatives-Dashboard  ) <br>
<br>

## 1. Vorbemerkung
„Für das Vergangene gibt der Kaufmann nichts.“ - Eugen Schmalenbach, Die Werte von Anlagen und Unternehmungen in der Schätztechnik, Zeitschrift für handelswirtschaftliche Fragen (ZfhF) 1917/1918, S. 1 ff.

Dieser Satz bringt Dilemma und Grenzen der betriebswirtschaftlichen Forschung gleichermaßen auf den Punkt. Denn nur die Zukunft lässt sich gestalten. Dies gilt allerdings auch für sicherlich sehr viele der existierenden Dashboards zur Wärmepumpenanalyse und -steuerung, die regelmäßig alle gleichermaßen daran kranken, dass sie bestenfalls die aktuellen Zustände darstellen. Um eine Wärmepumpe jedoch optimal zu steuern, bedarf es allerdings einer vorausschauenden Berücksichtigung von Live-Wetterdaten, da Umgebungstemperatur und Sonnenstrahlung technisch bedingt die maßgeblichen Parameter für die technische und ökonomische Effizienz aller Wärmepumpen sind. Anbieter wie NIBE oder Stiebel-Eltron haben dies nach eigenen Aussagen bereits erkannt und lassen diesbezügliche Prognosewerte angabegemäß in ihre Wärmepumpensteuerung einfließen. Die Viessmanns-VICare-App berücksichtigt derzeit noch m.W. keine Wetterprognose-Daten.<br>
<br>
Diese Lücke zu schließen, war meine Motivation für die Entwicklung des Entscheidungs-Dashboards. Es stellt bewusst eine robuste, minimalistische Optimierungsregel dar, mit der ca. 80 - 90% des möglichen Effizienzpotenzials realsiert werden können - die Handlunhsenpfehlungen lasssen sich alle problemlos in der Praxis mit Hilfe der VICare-App oder am Anlagen-Display umsetzen. Das Dashboard  <br>
<br>
- basiert auf stündlich abgerufene Wetterdaten von Meteo-Open (https://open-meteo.com/);
- umfasst einen Prognosezeitraum von 48 Stunden;
- bietet einen auf Temperaturtrend- und PV-Leistung basierenden Algorythmus, der 4  alternative Aktionen *vorschlägt*: <br>
    - Heizen verschieben,
    - PV nutzen,
    - Heizen vorziehen,
    - keine Änderungen;
- gibt ergänzende Inforationen, auf deren Grundlage der Nutzer *entscheiden kann* , was wirklich machbar und sinnvoll ist bzw. wieviel Spielraum tatsächlich besteht;
- berücksichtigt den Einfluss von Salorthermie; <br>
<br>

Die verarbeiteten Daten stehen in einer separaten SQLite-Datenbank (entscheidungs_dashboard.db), die ergänzend für die Beurteilung der vorgeschlagenen Aktion verwendeten Verschleiß- und Betriebsdaten werden synchron (stündlich) aus der viessmann_events.db (vieventlog) gelesen.<br>
<br>

## 2. Rechtliche Hinweise
Dieses Repository enthält ein Grafana-Dashboard als Classic-JSON-Datei sowie eine SQLite-Datenbank. Das Dashboard kann direkt in eine eigene Grafana-Instanz importiert werden. Die SQLite-Datenbank kann direkt auf die Festplatte kopiert werden.

Das Dashboard basiert auf Grafana OSS, einem Produkt von Grafana Labs, lizenziert unter der GNU Affero General Public License v3.0 (AGPLv3).

Der vollständige Quellcode von Grafana ist verfügbar unter: https://github.com/grafana/grafana

Die Lizenzbedingungen sind einsehbar unter: https://www.gnu.org/licenses/agpl-3.0.txt

Dieses Dashboard nutzt Grafana unverändert, sodass eine private Nutzung ohne Offenlegungspflichten möglich ist. Jeder Benutzer muss eine eigene Grafana-Instanz herunterladen und installieren.

Das für die Anbindung der viessmann_events-Datenbank erforderliche SQLite-Plugin ist Bestandteil der Grafana-Standard-Distribution und verursacht keine zusätzlichen Lizenzanforderungen.

SQLite ist eine Public Domain. Die Lizenzbedingungen sind einsehbar unter: https://sqlite.org/copyright.html

vieventlog Das Dashboard greift auf die Datei viessmann_events.db zu, die durch die Software vieventlog erzeugt und fortgeschrieben wird.

vieventlog ist ein Open-Source-Projekt von Matthias Schneider. Ein besonderer Dank gilt ihm für die Entwicklung und Bereitstellung dieses Projekts für die Community.

Der vollständige Quellcode ist verfügbar unter: https://github.com/mschneider82/vieventlog/releases

vieventlog ist unter der MIT-Lizenz lizenziert. Lizenzbedingungen: https://mit-license.org

Die in diesem Repository enthaltenen Grafana-Dashboard-JSON-Dateien und Datenbank-Dateien stehen unter der Creative Commons Attribution 4.0 International (CC BY 4.0).

Die Lizenzbedingungen können hier abgerufen werden: https://creativecommons.org/licenses/by/4.0/legalcode

Dieses Dashboard ist ein eigenständiges Community-Projekt und steht in keiner offiziellen Verbindung zu vieventlog oder dessen Autor.br>
<br>

Die vollständigen Lizenz- und rechtlichen Rahmenbedingungen, unter denen die in diesem Repository enthaltene Grafana-Dashboard-JSON-Dateien veröffentlich wird, stehen in den Dateien LEGAL.md und LICENSE.md in diesem Repository.<br>
<br>
## 3. Überblick
Nachstehend ein Überblick über die Inhalte des Entscheidungs-Dashboards <br>
<br>
<img width="1022" height="802" alt="image" src="https://github.com/user-attachments/assets/1b02b11e-8171-440b-9d67-db49d8ec79b9" />
<br>

## 4. Konzeptioneller Ansatz
Eine Wärmepumpe ist eine im Vergleich zu fossilen Brenwertgeräten vergleichsweise träge Heizquelle. Ihre (technische und ökonomische) Effizienz im Einsatz wird maßgeblich durch Umgebungstemperatur und angeforderte Wärmeleistung beeinflusst. Der Verschleiß (und damit die Lebensdauer) einer Wärmepumpe werden wiederum maßgeblich durch Laufzeit sowie Anzahl und zeitliche Abfolge der Kompressorstarts beeinflusst. Die Effizienz wird zusätzlich beeinflusst durch die Nutzung von Photovoltaik (Strompreis) sowie von Solarthermie (Stromverbrauch, Laufzeit, Kompressorstarts). <br>
<br>
Konzeptionell verfolgt das Dashboard einen physikalisch-herarchischen Ansatz: <br>
1. Entscheidungs-*Vorschlag* auf Basis eines festen Algorithmus <br>
   - Gebäudephysik (Trägheit bei Aufheizung) --> Temperaturtrend <br>
   - Nutzbarkeit von Photovoltaik --> nächstes PV-Fenster mit (einmaligem) Mindest-PV-Peak <br>

2. tatsächliche *Entscheidung* durch den Nutzer auf Basis ergänzender Informationen (Machbarkeit, bestehender Spielraum <br>
   - Komfortzeit (max. akzeptable Zeit für Abkühlung ohne Heizung)
   - Anlagenzustand (Vermeidung unnützer bzw. zusätzlicher Kompressourstarts, Berücksichtigung der Anlagen-Laufzeit <br>
   - Komfort (Warmwasser-Temperatur) <br>
3. Solarthermie <br>
Solarthermie verläuft weitestgehend komplementär zur PV-Leistung. Individuell ist sie ohne Sensoren nur sehr schwer zu prognostizieren, da ihre Wirkung u.a. neben der solareren Einstrahlung abhängig ist von Kollektortyp, Kollektortemperatur, Anlagen-Gesamtwirkungsgrad, Dachausrichtung, Dachneigung, Rohr-/Speicherverluste, Startverluste). Zudem ist ihr Einfluss vom Systemzustand (tatsächliche Pufferspeicher-Temperatur) abhängig, der faktisch nicht prognostizierbar ist. <br>
<br>
Konzeptionell erfolgt die Berücksichtigung Solarthermie-Nutzbarkeit deshalb als Hinweis in Form eines "Overrulings" des ansonsten aktiven Aktions-Vorschlags bei geeigneten Rahmenbdingungen (Pufferspeicher-Temperaturgrenzen, Stärke der Einstrahlung). <br>
<br>
Da die meisten Wärmepumpen in Verbindung mit Photovoltaik-Anlagen beschrieben werden, wird dieser Aktionsvorschlag in jedem Fall berücksichtigt. Der HInweis auf Solarthermie kann durch einfachen Eintrag in der Datenbank-Steuertabelle unterdrückt werden. (meta_config: Wert für min_solar_buffer_threshold auf 99 setzen). Das Panel für Pufferspeicher-Temperatur, word bei fehlenden Werten nicht angezeigt.<br>
<br>
<br>
Die ausführliche Beschreibung des konzeptionellen Ansatzes sowie die Beschrebung der AKtionsvorschlags-Ermittlung kann dem beiigenden Dokument "Enscheidungs-Dashoard.pdf" entnommen werden.<br>
<br>

## 5. Datenbank-Struktur
Das Dashboard verfügt über eine eigende SQLite-Datenbank mit mehreren Tabellen und Views, die als fertige Datenbank mit ausgeliefert wird (vgl. anhängende Datei...).Die Datenbank ist leer, lediglich die Steuertabelle (meta_config) enthält Einträge, damit die Datenbank unverzüglich genuzt werden kann. <br>
<br
Struktur und SQL-Statements zu ihrer Erzeugung (falls gewünscht oder notwendig) können dem beiligenden Dokument Entscheidung-Dashboard-pdf entnommenwerden. <br>
<br>

## 6. Befüllen der Datenbank
Das Dashboard basiert auf 2 Datenquellen, die stündlich (oder je nach Bedarf auch häufiger/seltener) befüllt werden:<br>
- 48-Stunden-Wettervorhersage von Open Meteo (https://open-meteo.com/) zur ABleitung des Aktionsvorschlags <br>
  Diese Wettervorhersage ist m.W. kostenlos (Begrenzung der kostenlosten API-Calls ist bei stündlichem Update unkritisch). Einzutragen sind im Download-Skript lediglich die Geodaten der zum Wärmepumpenstandort nächstgelegenen Wetterstation (zu finden unter https://open-meteo.com/en/docs?bounding_box=-90,-180,90,180)<br<
  Das Skript (Code), die genaue Bechreibung der Eintragung sowie die Einstellung des automatisch stündlich Skriptablaufs (CRON-Job) sind in der beiligenden Datei Entscheidungs-Dashboard ebshcrieben. <rb>
- Betriebsdaten der Wärmepumpe (für die ergänzenden Informationen ur tatsächlichen Entscheidungsfindung) <br>
  Hier greift das Dashboard auf die vonder Anwendung vieventlog erzeugten und regelmäßig fortgeschriebenen SQLite-Datenbank viessmann_events.db zurück. **Dies bedeutet, dass die vieventlog-Anwendung notwendig installiert werden und 7 x 24 laufen muss, damit die aktuellen Betriebsdaten zr Verfügung stehen.** <br>
Dies klingt auf den ersten Blick viellecht abschreckend, aber ohne kontinierliche Daten-Aktualisierung macht ein Dashboard eigentlich grundsätzlich keinen Sinn.<br>
<br>
Die Daten können alternativ auch ohne vieventlog per API-Call aus der Viessmann-Cloud heruntergeladen werden (aus der viessmann_event.db wird lediglich die Tabelle temperature_snapshot sowie die view temperature_snapshot_stat benötigt. Dieser Weg wird hier aber bewusst nicht empfohlen, da das Entscheidungs-Dashboard eigentlich nur optimal in Zusammenhang mit einem Dashboard für die Wärmepumpe betrieben werden kann: <br>
- mein Alternatives Dashboard (https://github.com/hrsnsvh2pd-png/Alternatives-Dashboard)
  oder
- das in vieventlog enthaltene Dashboard (https://github.com/mschneider82/vieventlog) <br>
<br>

## 7. Installation

