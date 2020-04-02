#### Überlegungen
Variable schritt und die gewählte Schrittlänge zu speichern, Variable pos für die aktuelle Position.
Wann ist man fertig? Wenn pos == 100 (dann hat man es geschafft) oder wenn man in eine endlosschleife gerät.
d.h. wenn man beim zurückgehen auf ein feld kommt, auf dem man schon mal war. Man muss sich also die felder,
auf denen man schon war, merken: variable visited als set.

visited wird als set implementiert.

Die Leiterdaten werden als eine dictionary gespeichert, das den Weg von unten nach oben beschreibt. Daraus
wird ein dictionary erstellt, das den umgekehrten Weg speichert. 

Der Ablauf wird in eine Funktion gebracht, der das N übergeben wird.