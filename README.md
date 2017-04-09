# EuroparlProc

Utility to process Europarl files needed for https://github.com/MULCIA/PLNLangDetection

## Languages supported

Danish, German, Greek, English, Spanish, Finnish, French, Italian, Dutch and Portuguese.

## Run

To run, needed a directory for each language supported. In the same directory run:

`$ python3 proc.py`

The result is 2 files: train.txt and eval.txt with same structure, an example is given below:

`
Merci Madame la Commissaire-0 0 0 0 0 0 1 0 0 0
Propongo allora di approvare in toto la relazione Cappato perfezionandola ulteriormente approvando l'emendamento n 44 invece del n 35-0 0 0 0 0 0 0 1 0 0
Situatie in Albanië na de verkiezingen-0 0 0 0 0 0 0 0 1 0
De conformidad con el orden del día se procede al debate conjunto de las seis preguntas orales siguientes-0 0 0 0 1 0 0 0 0 0
Ich stimme dieser Beurteilung zu und bekräftige noch einmal daß sich der Ratsvorsitz verpflichtet diese Lösung allerorts voranzutreiben-0 1 0 0 0 0 0 0 0 0
La Commission ne soutient pas non plus les amendements 5 10 11 16 17 ou 18-0 0 0 0 0 0 1 0 0 0
Por eso nos hemos abstenido en la votación final-0 0 0 0 1 0 0 0 0 0
Deze vraagstukken moeten worden aangepakt als we willen komen tot een probleemloze mobiliteit van werknemers-0 0 0 0 0 0 0 0 1 0
São estas as respostas concretas às questões concretas-0 0 0 0 0 0 0 0 0 1
Ud over de kvantitative gevinster i forhold til Rådets tidligere forslag er der også kvalitative fordele for Portugal-1 0 0 0 0 0 0 0 0 0
La votazione si svolgerà dopo la discussione-0 0 0 0 0 0 0 1 0 0
Jeg vil begynde med en anden af de personer som er berørt af denne oplysning-1 0 0 0 0 0 0 0 0 0
Daremo il nostro appoggio esclusivamente agli specifici punti della relazione cui ho accennato-0 0 0 0 0 0 0 1 0 0
 I have voted against the Report on Turkey-0 0 0 1 0 0 0 0 0 0
Je ne retrouve pas cette ambition dans les documents qui nous sont proposés-0 0 0 0 0 0 1 0 0 0
Työjärjestyksen mukaisesti kysymyksiin 48 49 ja 50 joiden esittäjät ovat jäsenet Fitzsimons Korakas ja Thors vastataan kirjallisesti-0 0 0 0 0 1 0 0 0 0
`

In the end line, there is a vector to indicate the language of the previous text in the same order than in Languages supported.