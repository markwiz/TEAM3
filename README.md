# team-3
Tiimi liikmed: Mark Kuusik, Freddie Turulinn, Orvet Priimägi

Flappy birdi taoline mäng

Objekt, mis liigub ise edasi. Kasutaja juhib seda space vajutades. Ette tulevad takistused, mille vahelt peab läbi minema, ehk siis liikuda saab üles alla. Iga kord objekti vahelt läbi minnes saab 1 punkti. Kui kasutaja läheb vastu takistust, siis mäng lõpeb. Kui kasutaja jõuab kaugemale ja skoor on tõusnud, siis mängu pilt läheb kiiremaks. Eesmärgiks on jõuda nii kaugele, kui võimalik.

Rollid on jaotatud võrdselt omavahel, koodimine, disain ja dokumentatsioon.

1.	Algusvaade:

 Keskel suur pealkiri: "Flappy Plane"
All keskel tekst: "Vajuta SPACE, et alustada"
o	Väike hall „lennuk“ keskel ekraani.
2.	Mänguvaade:
o	Pilvelõhkujad paarikaupa liikumas.
o	Mängija kontrollitav „lennuk“.
o	Ülemises vasakus nurgas tekst: "Score: 0"
o	Ülemises vasakus nurgas all tekst: "High: 0"
3.	Mängu Lõpu Vaade:
o	Kasti sees suur tekst: "GAME OVER"
o	Kasti sees allpool: "Score: [Mängija lõplik punktisumma]"
o	Kasti sees allpool: "High Score: [Kõrgeim punktisumma]"
o	Kasti sees all keskel: "Vajuta SPACE, et uuesti alustada"
Kasutajalugu 1: Mängu alustamine
•	Kasutaja: Uus mängija
•	Eesmärk: Soovin alustada mängu.
•	Vaade: Algusvaade (kirjeldatud ülal)
•	Tegevused: 
1.	Mängija näeb algusvaadet koos pealkirja ja alustamisjuhisega.
2.	Mängija vajutab klaviatuuril SPACE-klahvi.
3.	Mäng kuvab mänguvaate koos „lennuki“, pilvelõhkujate ja punktisummaga. Mäng on alanud.
Kasutajalugu 2: „Lennuki“ juhtimine ja punktide kogumine
•	Kasutaja: Aktiivne mängija
•	Eesmärk: Soovin lennutada „lennukit“ takistuste vahelt läbi ja koguda punkte.
•	Vaade: Mänguvaade (kirjeldatud ülal)
•	Tegevused: 
1.	Mängija näeb „lennukit“ liikumas paremale ja langevat gravitatsiooni mõjul.
2.	Mängija vajutab SPACE-klahvi.
3.	„Lennuk“ tõuseb ülespoole.
4.	Mängija kordab SPACE-klahvi vajutamist, et hoida „lennukit“ õhus ja manööverdada see läbi pilvelõhkujate vahede.
5.	Kui „lennuk“ läbib edukalt kahe pilvelõhkuja vahe, suureneb punktisumma ülemises vasakus nurgas.
6.	Pilvelõhkujad liiguvad pidevalt vasakule.
Kasutajalugu 3: Mängu lõppemine ja uuesti proovimine
•	Kasutaja: Mängija, kes on mängu kaotanud.
•	Eesmärk: Soovin näha oma tulemust ja võimalust uuesti mängida.
•	Vaade: Mängu Lõpu Vaade (kirjeldatud ülal)
•	Tegevused: 
1.	Kui „lennuk“ põrkab vastu pilvelõhkujat või maandub maale, lakkab mänguvaade liikumast.
2.	Mäng kuvab Mängu Lõpu Vaate koos lõpliku punktisumma ja kõrgeima punktisummaga.
3.	Mängija näeb juhist "Vajuta SPACE, et uuesti alustada".
4.	Mängija vajutab SPACE-klahvi.
5.	Mäng laeb uuesti mänguvaate algseisuga (punktisumma nullis, pilvelõhkujad algpositsioonides). Mäng algab uuesti.

![image](https://github.com/user-attachments/assets/0fddd1ea-72df-49ee-aa6d-f5a083d8dba1)
