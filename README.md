# Entscheidungs-Dashboard
Dieses Dashboard gibt vorausschauende Handlungsempfehlungen für den Betrieb einer Wärmepumpe auf Basis von: 

- Temperaturtrend <br>
- PV-Prognose <br>
- Betriebszustand der Heizungsanlage. <br>

Es berücksichtigt ferner die Nutzbarkeit von Solarthermie.

<img width="582" height="780" alt="image" src="https://github.com/user-attachments/assets/dd1bec68-48f9-4458-85aa-330077538c63" /> <br>
<br>
Das Entscheidungs-Dashboard ergänzt mein Alternatives Dashboard (vgl. https://github.com/hrsnsvh2pd-png/Alternatives-Dashboard  ) <br>
<br>

## 1. Vorbemerkung
„Für das Vergangene gibt der Kaufmann nichts.“ - Eugen Schmalenbach, Die Werte von Anlagen und Unternehmungen in der Schätztechnik, Zeitschrift für handelswirtschaftliche Fragen (ZfhF) 1917/1918, S. 1 ff.

Dieser Satz bringt Dilemma und Grenzen der betriebswirtschaftlichen Forschung gleichermaßen auf den Punkt. Denn nur die Zukunft lässt sich gestalten. Dies gilt allerdings auch für sicherlich sehr viele der existierenden Dashboards zur Wärmepumpenanalyse und -steuerung, die regelmäßig alle gleichermaßen daran kranken, dass sie bestenfalls die aktuellen Zustände darstellen. Um eine Wärmepumpe jedoch optimal zu steuern, bedarf es allerdings einer vorausschauenden Berücksichtigung von Live-Wetterdaten, da Umgebungstemperatur und Sonnenstrahlung technisch bedingt die maßgeblichen Parameter für die technische und ökonomische Effizienz aller Wärmepumpen sind. Anbieter wie NIBE oder Stiebel-Eltron haben dies nach eigenen Aussagen bereits erkannt und lassen diesbezügliche Prognosewerte angabegemäß in ihre Wärmepumpensteuerung einfließen. Die Viessmanns-VICare-App berücksichtigt derzeit noch m.W. keine Wetterprognose-Daten.<br>
<br>
Diese Lücke zu schließen, war meine Motivation für die Entwicklung des Entscheidungs-Dashboards. Es stellt bewusst eine robuste, minimalistische Optimierungsregel dar, mit der ca. 80 - 90% des möglichen Effizienzpotenzials eralsiert werden können - die Handlunhsenpfehlungen lasssen sich alle problemlos in der Praxis mit Hilfe der VICare-App oder am Anlagen-Display umsetzen. Das Dashboard  <br>
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
Dieses Repository enthält ein Grafana-Dashboard als Classic-JSON-Datei. Das Dashboard kann direkt in eine eigene Grafana-Instanz importiert werden.

Das Dashboard basiert auf Grafana OSS, einem Produkt von Grafana Labs, lizenziert unter der GNU Affero General Public License v3.0 (AGPLv3).

Der vollständige Quellcode von Grafana ist verfügbar unter: https://github.com/grafana/grafana

Die Lizenzbedingungen sind einsehbar unter: https://www.gnu.org/licenses/agpl-3.0.txt

Dieses Dashboard nutzt Grafana unverändert, sodass eine private Nutzung ohne Offenlegungspflichten möglich ist. Jeder Benutzer muss eine eigene Grafana-Instanz herunterladen und installieren.

Das für die Anbindung der viessmann_events-Datenbank erforderliche SQLite-Plugin ist Bestandteil der Grafana-Standard-Distribution und verursacht keine zusätzlichen Lizenzanforderungen.

vieventlog Das Dashboard greift auf die Datei viessmann_events.db zu, die durch die Software vieventlog erzeugt und fortgeschrieben wird.

vieventlog ist ein Open-Source-Projekt von Matthias Schneider. Ein besonderer Dank gilt ihm für die Entwicklung und Bereitstellung dieses Projekts für die Community.

Der vollständige Quellcode ist verfügbar unter: https://github.com/mschneider82/vieventlog/releases

vieventlog ist unter der MIT-Lizenz lizenziert. Lizenzbedingungen: https://mit-license.org

Die in diesem Repository enthaltenen Grafana-Dashboard-JSON-Dateien stehen unter der Creative Commons Attribution 4.0 International (CC BY 4.0).

Die Lizenzbedingungen können hier abgerufen werden: https://creativecommons.org/licenses/by/4.0/legalcode

Dieses Dashboard ist ein eigenständiges Community-Projekt und steht in keiner offiziellen Verbindung zu vieventlog oder dessen Autor.br>
<br>

Die vollständigen Lizenz- und rechtlichen Rahmenbedingungen, unter denen der in diesem Repository enthaltene Grafana-Dashboard-JSON veröffentlich wird, stehen inder Datei LEGAL.md in diesem Repository.<br>
<br>
## 3. Konzeptioneller Ansatz
