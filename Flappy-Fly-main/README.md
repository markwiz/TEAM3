# Flappy Plane

## Projekti ülevaade
"Flappy Plane" on lihtne 2D mäng, kus mängija juhib lennukit, mis peab navigeerima läbi pilvelõhkujate. Mängu eesmärk on läbida võimalikult palju takistusi.

## Funktsionaalsus
- Lennuki juhtimine tühiku klahviga
- Takistuste (pilvelõhkujate) genereerimine
- Punktisüsteem ja kõrgeima tulemuse salvestamine
- Animeeritud taustaobjektid (pilved)
- Lennuki mootorilõõma efekt hüppamisel

## Mängu juhised
1. Käivita mäng failist `mäng.py`
2. Vajuta tühikuklahvi mängu alustamiseks
3. Kasuta tühikuklahvi lennuki lennutamiseks
4. Väldi kokkupõrget pilvelõhkujate ja maapinnaga
5. Iga läbitud takistus annab ühe punkti
6. Mängu lõppedes vajuta tühikuklahvi uuesti alustamiseks

## Projekti struktuur
- `mäng.py` - peamine mängufail, sisaldab mängu tsüklit
- `constants.py` - mängu konstantide definitsioonid
- `plane.py` - lennuki klass ja funktsioonid
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
TTHK TEAM3
