# EuroparlProc

Utility to process [Europarl](http://www.statmt.org/europarl/) files needed for https://github.com/MULCIA/PLNLangDetection

## Languages supported

Danish, German, Greek, English, Spanish, Finnish, French, Italian, Dutch and Portuguese.

## Run

To run, needed a directory for each language supported. In the same directory run:

`$ python3 proc.py`

The result is 2 files: train.txt and eval.txt with same structure, an example is given below:

    Chers collègues je vous remercie pour l'excellent travail que vous avez réalisé dans ce dossier-0 0 0 0 0 0 1 0 0 0
    Tot besluit van het debat is er een ontwerpresolutie) ingediend overeenkomstig artikel 108 lid 5 van het Reglement-0 0 0 0 0 0 0 0 1 0
    Mrs Oviir your fan club has stayed to the end-0 0 0 1 0 0 0 0 0 0
    Por último hemos presentado dos enmiendas sobre el intercambio de información y la consideración de métodos
    alternativos-0 0 0 0 1 0 0 0 0 0
    Vielen Dank Herr Barnier-0 1 0 0 0 0 0 0 0 0

In the end line, there is a vector to indicate the language of the previous text in the same order than in Languages supported.