# Assignment: Personal Finance Tracker Application

## Uppgiftsbeskrivning

Slutuppgiften går ut på att skriva en personlig ekonomiapplikation skriven i Python. Applikationen hjälper användaren att spåra sina inkomster, utgifter och budgetar samt ger varningar när budgetgränser överskrids.

En användare kan interagera med applikationen via en konsol för att lägga till transaktioner, visa ekonomisk status, och hantera budgetar. När användaren interagerar med applikationen via konsolmenyn ska inga konfigurerade budgetvarningar aktiveras.

## Kraven på applikationen för godkänd nivå

Applikationen startas, och sedan presenteras användaren med fem stycken alternativ i konsolen.

### 1. Lägg till transaktion
Användaren kan lägga till en ny inkomst eller utgift. För varje transaktion krävs:
- Typ (inkomst eller utgift)
- Belopp (kronor)
- Kategori (t.ex. "Mat", "Transport", "Lön", "Hyra")
- Beskrivning (valfritt)
- Datum (automatiskt dagens datum om inget anges)

### 2. Visa ekonomisk status
Visar aktuell ekonomisk översikt med:
- Total inkomst denna månad
- Totala utgifter denna månad
- Återstående saldo
- Utgifter per kategori

Exempel:
```
=== EKONOMISK STATUS ===
Inkomster denna månad: 25,000 kr
Utgifter denna månad: 18,500 kr
Återstående saldo: +6,500 kr

UTGIFTER PER KATEGORI:
Mat: 4,500 kr
Transport: 1,200 kr
Hyra: 12,000 kr
Övrigt: 800 kr
```

Efter detta promptas användaren om att bekräfta genom att trycka enter.

### 3. Skapa budget
Väljer man detta alternativ får man upp ytterligare en meny där man kan sätta budgetgränser för olika kategorier:

```
Konfigurera budget för:
1. Mat
2. Transport  
3. Nöje
4. Kläder
5. Övrigt
6. Tillbaka till huvudmeny
```

Efter att man valt en kategori får man ange ett månadsbelopp för budgeten. T.ex:
```
Ställ in månadsbudget för Mat (kr): 5000
Budget för Mat satt till 5,000 kr/månad.
```

Beloppet måste vara ett positivt tal, annars ska användaren få ett felmeddelande.

### 4. Visa budgetar
Listar alla konfigurerade budgetar och visar hur mycket som använts av varje budget:

```
=== AKTIVA BUDGETAR ===
Mat: 4,500/5,000 kr (90% använt)
Transport: 800/1,500 kr (53% använt)
Nöje: 2,100/2,000 kr (105% - ÖVERSKRIDEN!)
```

Efter detta promptas användaren om att trycka enter för att återgå.

### 5. Starta budgetövervakning
Startar ett övervakningsläge där applikationen kontinuerligt kontrollerar om några budgetgränser har överskridits baserat på inlagda transaktioner.

```
Budgetövervakning är aktiv, tryck på valfri tangent för att återgå till menyn.
```

Om en budget överskrids visas en varning:
```
***VARNING: BUDGET ÖVERSKRIDEN! NÖJE: 2,100/2,000 kr (105%)***
```

## Icke-funktionella krav för godkänd nivå

- Programmet ska bestå av minst 3 filer med kod som aktivt används
- Programmet ska använda sig av klasser för att representera transaktioner och budgetar
- Programmet ska vara skrivet med funktioner för olika operationer
- Programmet ska innehålla funktionell programmering (t.ex. vid filtrering/sortering av transaktioner)
- Koden ska vara välskriven med tydliga variabel- och funktionsnamn
- Koden ska vara bugfri och hantera felaktig användarinput
- Rimlig input-validering ska finnas för alla användarinmatningar

## Kraven för väl godkänd nivå

För väl godkänd nivå krävs tre ytterligare funktioner:

### 1. Transaktionshistorik och filhantering
Alla transaktioner ska sparas i en JSON-fil och laddas automatiskt vid programstart. Transaktionshistoriken ska innehålla:
- Alla inkomster och utgifter med tidsstämpel
- Möjlighet att visa transaktioner för specifika månader
- Export av transaktioner till CSV-format för extern analys

Exempel på filformat (transactions.json):
```json
{
  "transactions": [
    {
      "id": 1,
      "type": "utgift",
      "amount": 450.0,
      "category": "Mat",
      "description": "ICA handla",
      "date": "2024-10-13"
    }
  ]
}
```

### 2. Ta bort/redigera transaktioner
Lägg till möjlighet att:
- Visa en lista över alla transaktioner med ID-nummer
- Ta bort specifika transaktioner
- Redigera befintliga transaktioner

Användaren väljer transaktion genom att ange ID-nummer:
```
Välj transaktion att ta bort:
1. 2024-10-13: Mat - 450 kr (ICA handla)
2. 2024-10-12: Lön - 25000 kr (Månadslon)
3. 2024-10-11: Transport - 120 kr (Buss)
```

### 3. Månadsrapporter och statistik
Automatisk generering av månadsrapporter som sparas som textfiler. Rapporten ska innehålla:
- Sammanfattning av inkomster och utgifter
- Jämförelse med tidigare månader
- Budget-analys (över/under budget per kategori)
- Sparandetrend

Rapporter namnges dynamiskt: `rapport_2024_10.txt`

## Icke-funktionella krav för VG nivå

Alla krav för godkänd nivå plus:

- Mycket välskriven och strukturerad kod med omfattande kommentarer
- Intelligent budgethantering (t.ex. varning vid 80% av budget, inte bara vid överskridande)
- Automatisk kategorisering av transaktioner baserat på beskrivning/tidigare mönster
- Felhantering för filoperationer (korrupta filer, diskutrymme, etc.)
- Enhetstester för kritiska funktioner
- Möjlighet att ställa in olika budgetperioder (vecka/månad/kvartal)

## Tips för implementation

1. **Börja enkelt**: Implementera grundmenyn först
2. **Datastrukturer**: Tänk på hur du ska representera transaktioner och budgetar
3. **Filhantering**: Använd JSON för enkel serialisering
4. **Felhantering**: Validera all användarinput
5. **Testning**: Testa ofta med olika scenarier

## Bedömningskriterier

**Godkänd (G):**
- Alla grundfunktioner implementerade och fungerar korrekt
- Kod är strukturerad i flera filer med klasser och funktioner
- Hantering av felaktig input
- Användbar applikation som löser de beskrivna problemen

**Väl Godkänd (VG):**
- Alla G-krav uppfyllda
- Avancerade funktioner implementerade (filhantering, rapporter, redigering)
- Mycket välstrukturerad och kommenterad kod
- Robust felhantering och edge cases hanterade
- Kreativa tillägg som förbättrar användarupplevelsen

---

**Lycka till med uppgiften! Kom ihåg att bryta ner problemet i mindre delar och implementera en funktion i taget.**