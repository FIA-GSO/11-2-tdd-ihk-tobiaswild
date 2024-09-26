# Grenzwertanalyse

Tipp: benutzen Sie einen [Tabellengenerator für Markdown](https://www.tablesgenerator.com/markdown_tables)

## Muster

### prozent_berechnen

| # | gesamt | wert   | erwartetes Ergebnis |
|---|--------|--------|---------------------|
| 1 | 100    | 0      | 0                   |
| 2 | 100    | 50     | 50                  |
| 3 | 100    | 100    | 100                 |
| 4 | 100    | 101    | ValueError          |
| 5 | 100    | -1     | ValueError          |
| 6 | -1     | 100    | ValueError          |
| 7 | "test" | 0      | TypeError           |
| 8 | 100    | "test" | TypeError           |

### note_berechnen

| # | prozent | erwartetes Ergebnis |
|---|---------|---------------------|
| 1 | 0       | ungenügend          |
| 2 | 50      | befriedigend        |
| 3 | 100     | sehr gut            |
| 4 | 101     | ValueError          |
| 5 | -1      | ValueError          |
| 6 | "test"  | TypeError           |
