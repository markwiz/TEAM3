# Flappy fly

## Projekti ülevaade
"Flappy Fly" on lihtne 2D mäng, kus mängija juhib kärbest, mis peab navigeerima läbi pilvelõhkujate. Mängu eesmärk on läbida võimalikult palju takistusi.

## Funktsionaalsus
- Kärpse juhtimine tühiku klahviga
- Takistuste (pilvelõhkujate) genereerimine
- Punktisüsteem ja kõrgeima tulemuse salvestamine
- Animeeritud taustaobjektid (pilved)
- Kärbsel efekt lendamisel

## Mängu juhised
1. Käivita mäng failist `mäng.py`
2. Vajuta tühikuklahvi mängu alustamiseks
   ![start](https://github.com/markwiz/TEAM3/blob/main/start.png)
4. Kasuta tühikuklahvi kärpse lennutamiseks
5. Väldi kokkupõrget pilvelõhkujate ja maapinnaga
6. Iga läbitud takistus annab ühe punkti
7. Mängu lõppedes vajuta tühikuklahvi uuesti alustamiseks

## Projekti struktuur
- `mäng.py` - peamine mängufail, sisaldab mängu tsüklit
- `constants.py` - mängu konstantide definitsioonid
- `plane.py` - kärpse klass ja funktsioonid
- `skyscraper.py` - takistuste (pilvelõhkujate) klass
- `cloud.py` - taustaobjektide (pilvede) klass
- `ground.py` - maapinna klass

## Tehnilised nõuded
- Python 3.x
- Pygame teek

## Installeerimine
1. Veendu, et sul on installeeritud Python 3.x
2. Installi Pygame käsuga: `pip install pygame`
3. Käivita mäng käsuga: `python mäng.py`

## Autorid
Mark Kuusik, Freddie Anton Turulinn, Orvet Priimägi
