# Accountable

Accountable ist ein leichtgewichtiges Lernwerkzeug, das lokale Aufgabenverwaltung mit punktueller KI-Unterstützung verbindet.

## MVP Features

### 1. Lokale To-Do/Notiz-Funktion
- Aufgaben hinzufügen, optional einem Lehrpfad zuordnen
- Checkbox zum Abhaken
- Optionales Datum und Wiederholung

### 2. Lehrpfade / Phasen
- Lehrpfade manuell anlegen (Name, Ziel, Beschreibung)
- Jede Phase enthält eine Aufgabenliste
- Subjektiver Abschluss über den Button "Ich habe es verinnerlicht"

### 3. Tagesansicht
- Zeigt heutige fällige Aufgaben
- Aktive Phasen mit Fortschritt
- Reflexionsfrage des Tages

### 4. KI-Integration
- Beim Erstellen eines neuen Lehrplans: Thema/Ziel eingeben → KI generiert Basisplan (Phasen + Aufgaben)
- Bei Reflexionen: KI liefert Zusammenfassung oder Mustererkennung
- Button „Neue Aufgabe vorschlagen“ für kontextbasierte KI-Ideen

## UX-Fluss
- **Home (Heute):** tägliche Aufgaben, aktive Phasen, Reflexionsfrage
- **Add Task / Lehrplan:** Modal mit KI-Vorschlagsknopf
- **Lehrpfade:** Kartenansicht aller Tracks → Phasenübersicht → Aufgaben & Reflexion
- **Reflexion:** Text- oder Audioeingabe mit optionaler KI-Zusammenfassung

## Architektur
- **Frontend:** Flutter (Android & iOS)
- **Datenhaltung:** lokal (SQLite oder Hive)
- **KI-API:** OpenAI oder Claude, nur bei Bedarf aufgerufen
- **Benachrichtigungen:** `flutter_local_notifications`
- Clean, modulare Architektur mit separaten KI-Services

## MVP-Fahrplan
1. Woche 1–2: Basis-App (To-Do, Lehrpfade, Phasen)
2. Woche 3: Tagesansicht + Reflexionssystem
3. Woche 4: KI-Integration für Planerstellung & Reflexionsauswertung
4. Woche 5: Benachrichtigungen, Bugfixes, kleiner Launch (Android)
5. Woche 6–8: Feedback sammeln, evtl. iOS-Port, KI-Features erweitern


## Entwicklung
Dieses Repository enthält jetzt erste Kernmodule (Datenbank, Modelle, KI-Stub).

### Voraussetzungen
- Python 3.10+

### Tests
```bash
pytest
```

### CLI ausprobieren
```bash
python -m accountable.cli add-task "Beispielaufgabe" --due-date 2024-01-01
python -m accountable.cli list-due --date 2024-01-01
```
