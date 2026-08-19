# Dwustopniowy system detekcji i klasyfikacji awarii UAV

Praca magisterska — detekcja i klasyfikacja awarii bezzałogowego statku
powietrznego (stałopłat Carbon Z T-28) na podstawie wielosensorowych danych
telemetrycznych ze zbioru **ALFA** (AIR Lab Failure and Anomaly Dataset, CMU).

## Zawartość

| Plik | Opis |
|---|---|
| `Drone_anomaly_clean.ipynb` | Główny notebook: etapy 1–4 (klasyfikacja lotów → okna czasowe → detekcja anomalii → kaskada) |
| `Drone_anomaly.ipynb` | Wersja robocza (historia eksperymentów) |
| `inventory01.py` | Skrypt inwentaryzacji lotów |

## Dane

Zbiór ALFA **nie jest wersjonowany** w repozytorium (1,2 GB). Pierwsza sekcja
notebooka pobiera go automatycznie z figshare (artykuł 12707963) i rozpakowuje
do `data/alfa/processed`.

## Środowisko

Python 3.10+, pakiety: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `requests`.

## Najważniejsze wyniki

- detekcja awarii w oknach 10 s: **25/34 awarii**, mediana opóźnienia **7,6 s**, 1 fałszywy alarm / 10 lotów normalnych
- klasyfikacja typu awarii (ENGINE vs CONTROL_SURFACE) na oknach: balanced accuracy **0,98**
- system dwustopniowy end-to-end: **24/34** awarii wykrytych i poprawnie sklasyfikowanych
